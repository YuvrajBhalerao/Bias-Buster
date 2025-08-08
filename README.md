_____________________________________________________
Bias Buster: AI-Powered Dataset Fairness Analysis 🤖
_____________________________________________________

Bias Buster is a web application designed to promote fairness in machine learning by providing an accessible tool for detecting and mitigating hidden biases within datasets. Developed for the Push AI Hackathon, this project addresses the critical need for equitable AI systems by empowering developers to easily analyze their data before model training.
____________________________________________________________________________________________________________

🎯 The Problem & Our Mission

The Problem: Datasets, particularly smaller ones, often contain unexamined statistical biases. These can lead to machine learning models that are not only inaccurate but also unfair and discriminatory.

Our Mission: To provide an intelligent, automated tool that makes dataset fairness analysis accessible to everyone. We aim to bridge the gap between raw data and a fair, model-ready dataset.
____________________________________________________________________________________________________________

✨ Key Features

Effortless Analysis 🚀: Simply upload your CSV file to initiate a comprehensive bias scan.

Automated Detection Engine ⚙️: The core of Bias Buster analyzes your data for three critical issues:

Class Imbalance: Flags categorical features where one class is significantly underrepresented.

Feature Skewness: Identifies numerical columns with asymmetrical distributions that could mislead a model.

Missing Data: Reports the percentage of null or missing values in each column.

Actionable Recommendations 💡: The tool doesn't just find problems; it provides clear, context-aware suggestions (e.g., "Use SMOTE for imbalance," "Apply a Log Transform for skewness") to help you fix them.

Interactive Dashboard 📊: Visualizes all findings with dynamic, easy-to-understand charts, making complex results simple to interpret.
____________________________________________________________________________________________

🛠️ Technology & Methodology

Our application is built on a modern tech stack designed for efficiency and clarity. The analysis follows a three-stage pipeline:

Data Ingestion: A user-provided CSV is validated and loaded into a Pandas DataFrame.

Bias Detection: The core engine scans the DataFrame for imbalance, skewness, and missing data using established statistical metrics.

Suggestion Generation: A rules-based engine maps detected issues to proven data science solutions.

Backend: Python, Flask

Data Analysis: Pandas, Scikit-learn, Imbalanced-learn

Frontend: HTML5, Tailwind CSS, Vanilla JavaScript

Visualization: Chart.js
________________________________________________________________________________________________

🚀 Local Installation

To run the application on your machine, follow these steps:

Clone the repository and navigate into the project directory.

Create and activate a virtual environment.

macOS/Linux: python3 -m venv venv and source venv/bin/activate

Windows: python -m venv venv and .\venv\Scripts\activate

Install the required packages: pip install -r requirements.txt

Start the development server: flask run

Open your browser and go to http://127.0.0.1:5000.
________________________________________________________________________________________________

📄 License

This project is distributed under the MIT License.
