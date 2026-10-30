import streamlit as st
import pandas as pd
import os
from datetime import datetime

from utils.pdf_reader import extract_text

from utils.parser import (
    extract_name,
    extract_email,
    extract_phone,
    extract_skills,
    extract_education,
    extract_experience
)

from utils.scorer import calculate_score
from utils.charts import skill_chart, score_chart


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main{
    background-color:#f7f9fc;
}

h1{
    color:#1f4e79;
}

.sidebar .sidebar-content{
    background-color:#ffffff;
}

.card{
    padding:20px;
    border-radius:15px;
    background:white;
    box-shadow:0px 0px 10px #ddd;
}

</style>
""", unsafe_allow_html=True)



# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("📄 Resume Analyzer")

    st.write(
        """
        AI based Resume Analysis System
        
        Features:
        - Resume Parsing
        - ATS Score
        - Skill Analysis
        - AI Suggestions
        - Report Download
        """
    )


    job_role = st.selectbox(
        "Select Target Job Role",
        [
            "Data Analyst",
            "Data Scientist",
            "Software Developer",
            "Python Developer",
            "Web Developer",
            "Machine Learning Engineer"
        ]
    )


    st.divider()

    st.info(
        "Upload your resume PDF and get AI based feedback."
    )




# ---------------- HEADER ----------------


st.title("🚀 AI Resume Analyzer")

st.subheader(
    "Analyze your resume and improve your job chances"
)



# ---------------- UPLOAD SECTION ----------------


uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)



if uploaded_file:


    with open(
        "uploaded_resume.pdf",
        "wb"
    ) as f:
        f.write(
            uploaded_file.getbuffer()
        )


    st.success(
        "Resume uploaded successfully ✅"
    )



    # ---------------- TEXT EXTRACTION ----------------


    resume_text = extract_text(
        "uploaded_resume.pdf"
    )


    if resume_text:


        st.subheader(
            "📌 Resume Information"
        )


        col1,col2 = st.columns(2)


        with col1:

            name = extract_name(
                resume_text
            )

            email = extract_email(
                resume_text
            )

            phone = extract_phone(
                resume_text
            )


            st.markdown(
                f"""
                <div class='card'>

                <h3>Personal Details</h3>

                <b>Name:</b> {name}

                <br><br>

                <b>Email:</b> {email}

                <br><br>

                <b>Phone:</b> {phone}

                </div>
                """,
                unsafe_allow_html=True
            )



        with col2:


            skills = extract_skills(
                resume_text
            )


            education = extract_education(
                resume_text
            )


            experience = extract_experience(
                resume_text
            )


            st.markdown(
                f"""
                <div class='card'>

                <h3>Professional Details</h3>

                <b>Skills:</b>

                {skills}

                <br><br>

                <b>Education:</b>

                {education}

                <br><br>

                <b>Experience:</b>

                {experience}

                </div>
                """,
                unsafe_allow_html=True
            )



        # ---------------- SCORE ----------------


        score = calculate_score(
            resume_text,
            job_role
        )


        st.subheader(
            "📊 Resume Score"
        )


        st.metric(
            "ATS Compatibility Score",
            f"{score}%"
        )


        st.progress(
            score/100
        )
            # ---------------- SKILL ANALYSIS ----------------


        st.subheader(
            "🛠 Skill Analysis"
        )


        if skills:


            skill_fig = skill_chart(
                skills
            )


            st.plotly_chart(
                skill_fig,
                use_container_width=True
            )


        else:

            st.warning(
                "No skills detected"
            )



        # ---------------- SCORE VISUALIZATION ----------------


        st.subheader(
            "📈 Score Analysis"
        )


        score_fig = score_chart(
            score
        )


        st.plotly_chart(
            score_fig,
            use_container_width=True
        )



        # ---------------- AI SUGGESTIONS ----------------


        st.subheader(
            "🤖 AI Resume Suggestions"
        )


        suggestions = []


        if score < 50:

            suggestions.append(
                "Improve your resume by adding more technical skills."
            )


        if len(experience) < 20:

            suggestions.append(
                "Add more project and internship experience."
            )


        if len(skills) < 3:

            suggestions.append(
                "Include more relevant skills for your target role."
            )


        if score >= 80:

            suggestions.append(
                "Great resume! Keep improving your profile."
            )



        for suggestion in suggestions:

            st.info(
                suggestion
            )



        # ---------------- REPORT GENERATION ----------------


        st.subheader(
            "📄 Generate Report"
        )


        report = f"""

AI Resume Analyzer Report
=========================

Date:
{datetime.now().strftime("%d-%m-%Y")}


Target Role:
{job_role}


Candidate Name:
{name}


Email:
{email}


Phone:
{phone}


Skills:
{skills}


Education:
{education}


Experience:
{experience}


ATS Score:
{score}%


Suggestions:

"""



        for s in suggestions:

            report += "\n- " + s



        st.download_button(

            label="Download Resume Report",

            data=report,

            file_name="Resume_Analysis_Report.txt",

            mime="text/plain"

        )



else:


    st.info(
        "Please upload your resume PDF to start analysis."
    )