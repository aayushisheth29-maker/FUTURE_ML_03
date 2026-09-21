# Resume and Candidate Screening using Machine Learning

## 📌 Project Overview

This project focuses on automating parts of the resume screening process using Natural Language Processing (NLP) and machine learning techniques.

The system cleans resume text, extracts relevant skills, compares them with the required skills for a target job, ranks candidates based on their skill match, and identifies skill gaps.

## 🎯 Objective

The main objectives of this project are:

- Parse and clean resume data
- Extract relevant skills from resumes
- Match candidate skills with job requirements
- Calculate candidate skill-match scores
- Rank candidates based on skill matching
- Identify missing skills for each candidate
- Visualise the top candidate rankings

## 📂 Dataset

The project uses a resume dataset containing resume text and job categories.

The dataset contains:

- 2,484 resumes
- 24 job categories
- Resume text and category information

The raw resume dataset is kept locally and is **not uploaded to this public repository**.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- NLTK
- PyPDF2
- python-docx

## 🔍 Methodology

### 1. Resume Cleaning

Resume text is converted to lowercase, unnecessary spaces are removed, and unwanted characters are cleaned.

### 2. Skill Extraction

A predefined skill dictionary is used to identify relevant technical and professional skills from each resume.

### 3. Skill Matching

The extracted skills are compared with the required skills for a target Data Scientist position.

### 4. Candidate Ranking

Candidates are ranked according to their percentage of matched required skills.

### 5. Skill Gap Identification

The system identifies required skills that are missing from each candidate's extracted skill set.

### 6. Visualisation

A bar chart is generated to visualise the skill-match scores of the top 10 candidates.

## 🎯 Target Job

**Data Scientist**

### Required Skills

- Python
- SQL
- Machine Learning
- Data Analysis
- Data Science
- Pandas
- NumPy
- Scikit-learn

## 📊 Sample Results

The system successfully generated candidate rankings based on skill matching.

The highest sample match score was **87.5%**.

The generated visualisation is:

`candidate_ranking.png`

## 📈 Project Output

The project produces:

- Cleaned resume data
- Extracted candidate skills
- Skill-match scores
- Ranked candidates
- Identified skill gaps
- Candidate ranking visualisation

## 📁 Project Structure

```text
FUTURE_ML_03/
│
├── data/
│   └── .gitkeep
│
├── candidate_ranking.png
├── task3_screening.py
├── README.md
├── requirements.txt
└── .gitignore
