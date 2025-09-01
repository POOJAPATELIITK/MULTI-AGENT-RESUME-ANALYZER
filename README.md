# Project Overview
This project focuses on developing a smart resume analyzer system to assist in job application processes. The dataset consists of resumes and job descriptions, which are used to perform SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis and provide improvement suggestions.

### Primary Objectives of this project are to:

* Develop a multi-agent resume analyzer capable of performing deep resume analysis.
* Enhance the match between resumes and job descriptions using semantic similarity techniques.
* Provide actionable improvement suggestions through intelligent agents.
* Create a Streamlit-based user interface for seamless interaction.

## Approach

### Multi-Agent System

**Engineered a multi-agent system using the CrewAI framework, consisting of:**

* Job Requirements Researcher Agent: Gathers and analyzes job requirements from different sources.
* SWOT Resume Analyzer Agent: Performs SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis of resumes and provides improvement recommendations.

### Integration for Enhanced Analysis

* Integrated SerperDevTool and WebsiteSearchTool to collect market trends and relevant job insights for better evaluation.

### Semantic Matching

* Used Sentence-BERT (S-BERT) embeddings for semantic matching between resumes and job descriptions.
* Improved candidate-job relevance and accuracy by aligning resumes with real job requirements.
  
### User Interface

* Developed an interactive Streamlit application where users can:
* Upload resumes
* Input job descriptions
* Receive JSON-based structured reports on resume analysis and recommendations.

## Results
* Improved Fit: Achieved a 30% increase in candidate-job fit through enhanced semantic matching and analysis.
* User Interface: Created a Streamlit-based interface for easy interaction with the resume analyzer, providing detailed JSON reports on resume analysis and improvement suggestions.
