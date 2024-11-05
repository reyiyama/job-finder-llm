# JobFinder: Empowering Job Seekers and Employers with Intelligent Job Matching

Welcome to **JobFinder**, a sophisticated web application built with Flask, designed to streamline the job search and posting process. JobFinder not only allows job seekers to browse and search for job listings but also empowers employers to post new job adverts with intelligent category recommendations powered by machine learning.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
  - [For Job Seekers](#for-job-seekers)
  - [For Employers](#for-employers)
- [Demo Screenshots](#demo-screenshots)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Step-by-Step Guide](#step-by-step-guide)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Navigating the Application](#navigating-the-application)
- [Project Structure](#project-structure)
- [Machine Learning Integration](#machine-learning-integration)
  - [Models Used](#models-used)
  - [How Category Recommendation Works](#how-category-recommendation-works)
- [Templates and Static Files](#templates-and-static-files)
- [Known Issues and Troubleshooting](#known-issues-and-troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact Information](#contact-information)

## Introduction

JobFinder is designed to bridge the gap between job seekers and employers by providing an intuitive platform for job discovery and job posting. By integrating machine learning, JobFinder offers category recommendations for new job postings, ensuring that job adverts reach the most relevant candidates.

Whether you're a job seeker looking for your next opportunity or an employer aiming to find the perfect candidate, JobFinder is tailored to meet your needs with ease and efficiency. Below is the data flow diagram showing the multiple components of this application.

![FlaskAppStructureFlowchart](https://github.com/user-attachments/assets/207b269c-12bd-434a-a8bf-e6478e747487)


## Features

### For Job Seekers

- **Browse All Job Listings:** Access a comprehensive list of available job postings on the homepage.
- **View Job Details:** Click on job titles to view detailed descriptions, qualifications, salary ranges, and more.
- **Browse by Category:** Explore jobs categorized by industry sectors for targeted job hunting.
- **Responsive Design:** Enjoy a user-friendly interface optimized for various devices.

### For Employers

- **Post New Job Listings:** Easily create and submit new job adverts with essential details.
- **Intelligent Category Recommendation:** Receive machine learning-powered suggestions for job categories based on the job description.
- **Override Recommendations:** Manually select or override the suggested categories to best fit your job posting.
- **Preview Before Posting:** Review the job advert before final submission to ensure accuracy.

## Demo Screenshots

*Note: Since this is a text-based README, please refer to the `screenshots/` directory in the repository for visual demonstrations of the application.*

- **Homepage:**

  <img width="478" alt="Screenshot 2024-11-05 at 3 23 13 PM" src="https://github.com/user-attachments/assets/f4916b78-e183-4a11-8f7c-fde08a3ef67b">


- **Job Details:**

  <img width="847" alt="Screenshot 2024-11-05 at 3 24 04 PM" src="https://github.com/user-attachments/assets/071c7a63-af01-42c2-ad7c-0812842da98d">


- **Browse by Category:**

  <img width="847" alt="Screenshot 2024-11-05 at 3 24 04 PM" src="https://github.com/user-attachments/assets/071c7a63-af01-42c2-ad7c-0812842da98d">

- **Post a Job:**

  <img width="465" alt="Screenshot 2024-11-05 at 3 25 13 PM" src="https://github.com/user-attachments/assets/f60c5ffe-e53f-4d22-9032-095a0cf33ddd">




## Technology Stack

- **Backend Framework:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Machine Learning:** gensim (FastText), scikit-learn (Logistic Regression)
- **Data Handling:** NumPy, joblib
- **Visualization (Optional):** graphviz

## Installation

### Prerequisites

- **Python 3.7 or higher**
- **pip** package manager
- **Virtual Environment** (Recommended)
- **Graphviz** (Optional, for visualizations)
- **Git** (For cloning the repository)

### Step-by-Step Guide

1. **Clone the Repository**

   Open your terminal and run:

   ```bash
   git clone https://github.com/yourusername/jobfinder.git
   cd jobfinder
   ```

2. **Set Up a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

3. **Install Required Packages**

   Install the packages listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   *Note: Ensure that you have the necessary system dependencies for some packages, especially `gensim` and `graphviz`.*

4. **Set Up Machine Learning Models**

   Ensure the following pre-trained models are placed inside the `models/` directory:

   - `desc_FT.model`
   - `desc_FT.model.wv.vectors_ngrams.npy`
   - `descFT_LR.pkl`

   *These models are essential for the category recommendation feature.*

5. **Verify the Installation**

   Run the following command to ensure all dependencies are correctly installed:

   ```bash
   python -c "import flask; import gensim; import joblib; import numpy"
   ```

   If no errors are returned, you're good to go!

## Usage

### Running the Application

1. **Start the Flask Server**

   In your terminal, run:

   ```bash
   python app.py
   ```

   You should see output similar to:

   ```
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```

2. **Access the Application**

   Open your web browser and navigate to `http://127.0.0.1:5000/`

### Navigating the Application

- **Homepage (`/`):** View all available job listings. Click on job titles to view details.
- **Browse by Category (`/browse_jobs`):** See jobs organized by categories. Click on categories to filter jobs.
- **Job Details (`/job/<int:job_id>`):** Read full job descriptions and details.
- **Post a Job (`/create_job`):** Employers can create new job listings. Fill in the form, and the system will recommend a job category.
- **Category Recommendation:** As you type the job description, the application suggests a category based on the input.

## Project Structure

```
jobfinder/
│
├── app.py                         # Main Flask application
├── models/                        # Machine Learning models
│   ├── desc_FT.model
│   ├── desc_FT.model.wv.vectors_ngrams.npy
│   ├── descFT_LR.pkl
│
├── static/                        # Static files (CSS, images)
│   ├── style.css                  # Main stylesheet
│
├── templates/                     # HTML templates
│   ├── browse_jobs.html
│   ├── category_jobs.html
│   ├── create_job.html
│   ├── index.html
│   ├── job_detail.html
│
├── requirements.txt               # Python dependencies
├── README.md                      # Project README file
└── screenshots/                   # Screenshots of the application
```

## Machine Learning Integration

### Models Used

- **FastText Model (`desc_FT.model`):**
  - Generates vector representations of job descriptions.
  - Captures semantic relationships between words.

- **Logistic Regression Classifier (`descFT_LR.pkl`):**
  - Predicts the job category based on the vectorized description.
  - Trained on labeled job description data.

### How Category Recommendation Works

1. **Input Processing:**
   - Employer enters the job description into the form.

2. **Text Vectorization:**
   - The `get_average_vector` function splits the description into words.
   - For each word, it retrieves the corresponding vector from the FastText model.
   - Calculates the mean vector to represent the entire description.

3. **Category Prediction:**
   - The averaged vector is passed to the Logistic Regression classifier.
   - The classifier outputs the most probable job category.

4. **Recommendation Display:**
   - The predicted category is displayed on the form.
   - Employers can accept the recommendation or select a different category.

### Handling Model Loading

- Models are loaded at the start of the application.
- Error handling is implemented to catch issues during model loading.
- If models fail to load, the application sets the model variables to `None` and proceeds without the recommendation feature.

## Templates and Static Files

- **Templates (`templates/`):**
  - Utilize Jinja2 templating for dynamic content rendering.
  - Include placeholders for variables passed from Flask views.

- **Static Files (`static/`):**
  - Contains `style.css` for styling the application.
  - Images and additional assets can be added as needed.

## Known Issues and Troubleshooting

- **Category Prediction Not Displaying:**
  - The predicted category may not appear due to JavaScript issues or model loading errors.
  - *Solution:* Ensure models are correctly loaded and check the browser console for JavaScript errors.

- **Model Compatibility Errors:**
  - Errors like "X has 200 features, but expected 5356 features" may occur.
  - *Solution:* Verify that the vector dimensions match between the FastText model and the classifier. Retrain models if necessary.

- **Data Persistence:**
  - New job postings are stored in an in-memory list and will not persist after restarting the application.
  - *Solution:* Implement a database system (e.g., SQLite, PostgreSQL) for persistent storage.

- **Graphviz Errors (if using visualization):**
  - Errors may occur if Graphviz is not properly installed or configured.
  - *Solution:* Install Graphviz system binaries and ensure they are added to your system's PATH.

## Future Enhancements

- **Persistent Data Storage:**
  - Integrate a relational database to store job postings and user data persistently.

- **User Authentication:**
  - Implement login and registration for job seekers and employers for a personalized experience.

- **Enhanced Category Prediction:**
  - Improve the machine learning models for higher accuracy.
  - Allow real-time prediction as the employer types the job description.

- **Responsive and Modern UI:**
  - Redesign the frontend for better aesthetics and mobile responsiveness.

- **Advanced Search Functionality:**
  - Enable job seekers to search jobs by keywords, location, salary range, etc.

- **Notification System:**
  - Implement email notifications for new job postings and applications.

- **Application Tracking:**
  - Allow job seekers to apply for jobs and track their application status.

## Contributing

We welcome contributions to enhance JobFinder!

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Make Your Changes**

   - Follow best coding practices.
   - Ensure your code is well-documented.

4. **Run Tests**

   - Verify that your changes do not break existing functionality.

5. **Commit and Push**

   ```bash
   git commit -m "Add your feature"
   git push origin feature/YourFeature
   ```

6. **Submit a Pull Request**

   - Provide a clear description of your changes.
   - Wait for the project maintainers to review your submission.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Flask Documentation:** For providing clear and comprehensive guides.
- **gensim and scikit-learn Communities:** For powerful machine learning tools.
- **Bootstrap:** For frontend design inspiration.

## Contact Information

For any inquiries or feedback, please contact:

- **Email:** amayvishiyer@gmail.com
- **GitHub:** [reyiyama](https://github.com/reyiyama)

---

*Thank you for choosing JobFinder. We hope this application aids you in your job search or helps you find the perfect candidate for your job opening!*
