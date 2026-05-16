# Assignment 4: NLP Resume Matcher

## Overview

A Python tool that compares a resume (PDF) against a job description (TXT) using NLP techniques. It calculates a match score and identifies skill gaps between the candidate and the job requirements.

## How It Works

1. **Text Extraction** — Extracts raw text from resume PDF and job description TXT file using pdfplumber and Python's built-in file reader
2. **Text Cleaning** — Removes stopwords and punctuation using NLTK, converts to lowercase
3. **Match Score** — Converts cleaned text into TF-IDF vectors and calculates cosine similarity between them
4. **Skill Extraction** — Scans both documents for predefined skill keywords grouped by category
5. **Missing Skills** — Compares resume skills against JD skills and highlights gaps

## Project Structure

assignment4_resume_matcher/
├── extractor.py # Text extraction and cleaning
├── matcher.py # TF-IDF, cosine similarity, skill grouping
├── main.py # Entry point, coordinates all modules
├── sample_resume.pdf # Sample resume for testing
├── sample_jd.txt # Sample job description for testing
├── requirements.txt # Project dependencies
└── README.md # Project documentation

## Installation

### 1. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### 1. Add your files

- Place your resume PDF in the project folder
- Create a `sample_jd.txt` file with the job description

### 2. Update file paths in main.py

```python
resume_path = "your_resume.pdf"
jd_path = "sample_jd.txt"
```

### 3. Run the matcher

```bash
python main.py
```

## Sample Output
