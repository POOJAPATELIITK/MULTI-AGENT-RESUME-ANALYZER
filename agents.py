# # Agents
# # 1. Job Requirements Researcher
# # 2. SWOT Analyser

# ## Importing the dependencies

from crewai import Agent
from crewai_tools import SerperDevTool, WebsiteSearchTool

# ------------------------
# Tools Setup
# ------------------------

# Search Tool
search_tool = SerperDevTool()

# Website RAG Tool with HuggingFace embeddings
web_rag_tool = WebsiteSearchTool(
    config={
        "embedding_model": {
            "provider": "huggingface",  
            "config": {
                "model": "sentence-transformers/all-MiniLM-L6-v2"
            }
        }
    }
)

# ------------------------
# Agents Definition
# ------------------------
def agents(llm):
    '''
    Has two agents:
    1. requirements_researcher - uses search_tool, web_rag_tool
    2. swot_analyser - uses llm
    '''
    # Job Requirements Researcher Agent
    job_requirements_researcher = Agent(
        role='Market Research Analyst',
        goal='Provide up-to-date market analysis of industry job requirements of the domain specified',
        backstory='An expert analyst with a keen eye for market trends.',
        tools=[search_tool, web_rag_tool],
        verbose=True,
        llm=llm,
        max_iters=1
    )
    
    # Resume SWOT Analyser Agent
    resume_swot_analyser = Agent(
        role='Resume SWOT Analyser',
        goal=('Perform a SWOT Analysis on the Resume based on the industry '
              'Job Requirements report from job_requirements_researcher and provide a JSON report.'),
        backstory='An expert in hiring so has a great idea on resumes',
        verbose=True,
        llm=llm,
        max_iters=1,
        allow_delegation=True
    )

    return job_requirements_researcher, resume_swot_analyser


# ------------------------

# ------------------------
if __name__ == "__main__":
    from langchain_groq import ChatGroq
    from langchain_openai import ChatOpenAI
    import os
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    
    llm = ChatOpenAI(
    model="gpt-4o",  
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")  
)

    researcher, swot = agents(llm)
    print("Agents initialized successfully!")

