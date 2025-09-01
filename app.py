import streamlit as st
import os
from crewai import Crew, Process
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from utils import read_all_pdf_pages
from agents import agents
from tasks import tasks
import json
import tempfile

# Load environment variables
load_dotenv(find_dotenv())
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(
    model="gpt-4o",  
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")  # Make sure your key is set
)

# Streamlit UI
st.set_page_config(page_title="Smart Resume Analyzer | AI Agents", layout="wide")

st.title("📄 Smart Resume Analyzer System | AI Agents")
st.markdown("Analyze resumes with multi-agents & semantic matching")

# File uploader
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_desire = st.text_input("Enter Desired Job Role:")

if uploaded_file and job_desire:
    if st.button("🚀 Run Analysis"):
        with st.spinner("Analyzing Resume... Please wait ⏳"):
            # Save uploaded PDF temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                temp_pdf_path = tmp_file.name

            # Extract resume text
            resume = read_all_pdf_pages(temp_pdf_path)

            # Create agents & tasks
            job_requirements_researcher, resume_swot_analyser = agents(llm)
            research, resume_swot_analysis = tasks(llm, job_desire, resume)

            # Run CrewAI pipeline
            crew = Crew(
                agents=[job_requirements_researcher, resume_swot_analyser],
                tasks=[research, resume_swot_analysis],
                verbose=1,
                process=Process.sequential
            )

            result = crew.kickoff()

            # Show result
            st.subheader("📊 Resume SWOT Analysis Report")
            try:
                parsed_result = json.loads(result)  # if result is JSON
                st.json(parsed_result)
            except:
                st.write(result)  # fallback if plain text





            st.subheader("📊 Resume SWOT Analysis Report")
            try:
                parsed_result = json.loads(result)  # if result is JSON
                # Convert JSON nicely into markdown
                markdown_output = ""
                for key, value in parsed_result.items():
                    markdown_output += f"### {key}\n"
                    if isinstance(value, list):
                        for item in value:
                            markdown_output += f"- {item}\n"
                    else:
                        markdown_output += f"{value}\n\n"
                st.markdown(markdown_output)
            except:
                st.markdown(result)  # fallback if plain text

