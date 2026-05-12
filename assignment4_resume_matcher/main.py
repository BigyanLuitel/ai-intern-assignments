from extractor import extract_text_from_pdf, extract_text_from_text, clean_text
from matcher import calculate_match_score, extract_skills, get_missing_skills

def run_matcher(resume_path: str, jd_path: str):
    print("\n" + "="*50)
    print("         NLP RESUME MATCHER")
    print("="*50)

    # Step 1 - Extract text
    print("\n[1] Extracting text...")
    raw_resume = extract_text_from_pdf(resume_path)
    raw_jd = extract_text_from_text(jd_path)

    # Step 2 - Clean text
    print("[2] Cleaning and processing text...")
    clean_resume = clean_text(raw_resume)
    clean_jd = clean_text(raw_jd)

    # Step 3 - Match score
    print("[3] Calculating match score...")
    score = calculate_match_score(clean_resume, clean_jd)

    # Step 4 - Extract skills
    print("[4] Extracting and grouping skills...")
    resume_skills = extract_skills(raw_resume)
    jd_skills = extract_skills(raw_jd)
    missing_skills = get_missing_skills(resume_skills, jd_skills)

    # Step 5 - Print results
    print("\n" + "="*50)
    print(f"  MATCH SCORE: {score}%")
    print("="*50)

    print("\n RESUME SKILLS FOUND:")
    for category, skills in resume_skills.items():
        print(f"  {category}: {', '.join(skills)}")

    print("\n JOB DESCRIPTION SKILLS FOUND:")
    for category, skills in jd_skills.items():
        print(f"  {category}: {', '.join(skills)}")

    print("\n  MISSING SKILLS:")
    if missing_skills:
        for category, skills in missing_skills.items():
            print(f"  {category}: {', '.join(skills)}")
    else:
        print("  None — great match!")

    print("\n" + "="*50)

if __name__ == "__main__":
    resume_path = "BIGYAN_LUITEL.pdf"
    jd_path = "sample_jd.txt"
    run_matcher(resume_path, jd_path)