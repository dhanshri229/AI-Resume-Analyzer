import re


# ---------------- SKILLS DATABASE ----------------

SKILLS = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Tableau",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "Machine Learning",
    "Deep Learning",
    "Statistics",
    "Data Analysis",
    "Git",
    "GitHub",
    "HTML",
    "CSS",
    "JavaScript",
    "Java",
    "C++",
    "MySQL",
    "SQLite",
    "PostgreSQL",
    "Streamlit",
    "Flask",
    "Django",
    "TensorFlow",
    "Scikit-learn"
]



# ---------------- EMAIL EXTRACTION ----------------

def extract_email(text):

    match = re.search(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    if match:
        return match.group(0)

    return "Not Found"




# ---------------- PHONE EXTRACTION ----------------

def extract_phone(text):

    match = re.search(
        r'(\+91[\-\s]?)?[6-9]\d{9}',
        text
    )

    if match:
        return match.group(0)

    return "Not Found"




# ---------------- NAME EXTRACTION ----------------

def extract_name(text):

    lines = text.split("\n")

    ignore_words = [
        "resume",
        "curriculum vitae",
        "cv",
        "profile",
        "objective"
    ]


    for line in lines:

        line = line.strip()


        if (
            len(line) > 2
            and len(line) < 40
            and not any(ch.isdigit() for ch in line)
            and line.lower() not in ignore_words
        ):

            return line


    return "Unknown"




# ---------------- SKILL EXTRACTION ----------------

def extract_skills(text):

    found = []

    text = text.lower()


    for skill in SKILLS:

        if skill.lower() in text:

            found.append(skill)


    return sorted(list(set(found)))




# ---------------- EDUCATION EXTRACTION ----------------

def extract_education(text):

    education = []


    keywords = [

        "BCA",
        "MCA",
        "B.Tech",
        "M.Tech",
        "BSc",
        "MSc",
        "Bachelor",
        "Master",
        "Diploma",
        "HSC",
        "SSC",
        "BE",
        "ME"

    ]


    text = text.lower()


    for word in keywords:

        if word.lower() in text:

            education.append(word)


    if education:
        return list(set(education))


    return ["Not Found"]




# ---------------- EXPERIENCE EXTRACTION ----------------

def extract_experience(text):

    text = text.lower()


    exp = re.findall(
        r'(\d+)\+?\s*(?:year|years)',
        text
    )


    if exp:

        return exp[0] + " Years"


    keywords = [
        "internship",
        "intern",
        "experience",
        "work experience"
    ]


    for word in keywords:

        if word in text:

            return "Experience Mentioned"



    return "Fresher"