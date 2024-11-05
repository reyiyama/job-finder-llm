from flask import Flask, render_template, request, redirect, url_for, jsonify
import joblib
from gensim.models import FastText
import numpy as np

app = Flask(__name__)

# Load models
try:
    ft_model = FastText.load("./models/desc_FT.model")
    classifier = joblib.load("./models/descFT_LR.pkl")
    #the multinomial bayes model did not work well in being able to predict the category
    naive_bayes_classifier = joblib.load("./models/multinomial_naive_bayes_model.pkl")  # Loading the Naive Bayes model
except Exception as e:
    print(f"Error loading models: {e}")
    ft_model = None
    classifier = None
    naive_bayes_classifier = None  # Setting to None if there's an error

# Dummy data for job listings
job_data = [
    {
        'id': 1,
        'title': 'Software Developer',
        'description': 'Develop and maintain software applications.',
        'salary': '80k-100k',
        'category': 'Engineering'
    },
    {
        'id': 2,
        'title': 'Marketing Manager',
        'description': 'Plan and oversee advertising campaigns. Analyze market trends.',
        'salary': '70k-90k',
        'category': 'Marketing'
    },
    {
        'id': 3,
        'title': 'Sales Representative',
        'description': 'Promote and sell products to clients. Build and maintain client relationships.',
        'salary': '50k-70k',
        'category': 'Sales'
    },
    {
        'id': 4,
        'title': 'Financial Analyst',
        'description': 'Analyze financial data. Provide insights for financial decisions.',
        'salary': '75k-95k',
        'category': 'Finance'
    },
    {
        'id': 5,
        'title': 'HR Specialist',
        'description': 'Manage recruitment processes. Handle employee relations and benefits.',
        'salary': '60k-80k',
        'category': 'Human Resources'
    },
    {
        'id': 6,
        'title': 'IT Support',
        'description': 'Provide technical support to employees. Troubleshoot software and hardware issues.',
        'salary': '65k-85k',
        'category': 'IT'
    }
]

# Predefined job categories
JOB_CATEGORIES = ["Engineering", "Marketing", "Sales", "Finance", "Human Resources", "IT"]


@app.route('/')
def index():
    return render_template('index.html', job_list=job_data)

@app.route('/browse_jobs')
def browse_jobs():
    return render_template('browse_jobs.html', JOB_CATEGORIES=JOB_CATEGORIES, job_data=job_data)

@app.route('/job/<int:job_id>')
def job_detail(job_id):
    job = next((j for j in job_data if j['id'] == job_id), None)
    if not job:
        return "Job not found", 404
    return render_template('job_detail.html', job=job)

#job categories
@app.route('/category/<string:category_name>')
def category_jobs(category_name):
    filtered_jobs = [j for j in job_data if j['category'] == category_name]
    return render_template('category_jobs.html', jobs=filtered_jobs, categories=JOB_CATEGORIES, active_category=category_name)

def get_average_vector(text, model):
    words = text.split()
    vectors = [model.wv[word] for word in words if word in model.wv.key_to_index]
    if vectors:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(model.vector_size)

#not used as whenever I tried to call this function with the multinomial bayes model, i got 
# an error whenever I tried to Post a Job which said
# 'An error occurred: X has 200 features, but MultinomialNB is expecting 5356 features as input.'  
@app.route('/predict_category')
def predict_category():
    description = request.args.get('description', '')
    if not description:
        return jsonify({'category': None})

    if not ft_model or not classifier:
        return jsonify({'error': 'Model not loaded'})

    try:
        vector = get_average_vector(description, ft_model)
        predicted_category = naive_bayes_classifier.predict([vector])[0]
        return jsonify({'category': predicted_category})

    except Exception as e:
        return jsonify({'error': str(e)})



@app.route('/create_job', methods=['GET', 'POST'])
def create_job():
    predicted_category = None
    if request.method == "POST":
        try:
            title = request.form.get('title')
            description = request.form.get('description')
            salary = request.form.get('salary')
            user_selected_category = request.form.get('user_category')

            if not ft_model or not classifier:
                raise ValueError("Models are not correctly loaded.")
            vector = get_average_vector(description, ft_model)

            # Predicting job category
            predicted_category = classifier.predict([vector])[0]

            # Using the user-selected category if provided; otherwise, use the predicted category.
            final_category = user_selected_category if user_selected_category else predicted_category

            # Appending to job_data temporarily while app is running
            # NOTE: Use a persistent storage like SQLite for more robust data storage.
            job_data.append({
                'id': len(job_data) + 1,
                'title': title,
                'description': description,
                'salary': salary,
                'category': final_category
            })

            return redirect(url_for('index'))

        except Exception as e:
            return f"An error occurred: {e}"


    # Passing JOB_CATEGORIES to the template for category dropdown population
    # also passing predicted_category
    return render_template('create_job.html', JOB_CATEGORIES=JOB_CATEGORIES, predicted_category=predicted_category)

if __name__ == '__main__':
    app.run(debug=True)


