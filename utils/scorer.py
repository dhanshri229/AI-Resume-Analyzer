def calculate_score(skills, education, experience):

    score = 0

    score += min(len(skills) * 5, 50)

    score += min(len(education) * 10, 20)

    if experience != "Fresher":
        score += 20
    else:
        score += 10

    if score > 100:
        score = 100

    return score