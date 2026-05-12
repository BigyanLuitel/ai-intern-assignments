from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILL_GROUPS = {
    "Programming Languages": ["python", "java", "javascript", "typescript", "c", "cpp", "ruby", "swift"],
    "Web Frameworks": ["django", "flask", "fastapi", "react", "angular", "vue", "nodejs"],
    "AI/ML": ["langchain", "langgraph", "tensorflow", "pytorch", "scikit", "keras", "rag", "llm", "nlp"],
    "Databases": ["postgresql", "mysql", "sqlite", "mongodb", "chromadb", "pinecone", "redis"],
    "DevOps & Tools": ["git", "docker", "kubernetes", "aws", "azure", "render", "linux"],
    "Data Science": ["pandas", "numpy", "matplotlib", "seaborn", "scipy"],
}

def calculate_match_score(resume_text: str, jd_text: str) -> float:
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)

def extract_skills(text: str) -> dict:
    found_skills = {}
    text_lower = text.lower()
    for category, skills in SKILL_GROUPS.items():
        matched = [skill for skill in skills if skill in text_lower]
        if matched:
            found_skills[category] = matched
    return found_skills

def get_missing_skills(resume_skills: dict, jd_skills: dict) -> dict:
    missing = {}
    for category in jd_skills:
        if category in resume_skills:
            missing_in_category = [skill for skill in jd_skills[category] if skill not in resume_skills[category]]
        else:
            missing_in_category = jd_skills[category]
        if missing_in_category:  # only add if something is actually missing
            missing[category] = missing_in_category
    return missing