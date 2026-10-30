import matplotlib.pyplot as plt

def skill_chart(skills):

    if len(skills)==0:
        skills=["No Skill"]
        values=[1]
    else:
        values=[1]*len(skills)

    fig,ax=plt.subplots(figsize=(8,4))

    ax.bar(skills,values)

    ax.set_title("Extracted Skills")

    plt.xticks(rotation=45)

    return fig


def score_chart(score):

    labels=["Score","Remaining"]

    values=[score,100-score]

    fig,ax=plt.subplots(figsize=(5,5))

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Resume Score")

    return fig