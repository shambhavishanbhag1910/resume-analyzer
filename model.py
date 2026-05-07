def predict_role(resume):

    resume = resume.lower()

    if "machine learning" in resume:
        return "AI Engineer"

    elif "sql" in resume:
        return "Data Analyst"

    elif "react" in resume:
        return "Frontend Developer"

    elif "docker" in resume:
        return "DevOps Engineer"

    return "Unknown"