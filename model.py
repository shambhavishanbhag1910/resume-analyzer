skills_db = [
    "python",
    "machine learning",
    "sql",
    "excel",
    "docker",
    "flask",
    "react"
]

def extract_skills(resume):

    found_skills = []

    resume = resume.lower()

    for skill in skills_db:
        if skill in resume:
            found_skills.append(skill)

    return found_skills


def predict_role(resume):

    resume = resume.lower()

    if "machine learning" in resume:
        return "AI Engineer"

    elif "sql" in resume:
        return "Data Analyst"

    elif "react" in resume:
        return "Frontend Developer"

    return "Unknown"