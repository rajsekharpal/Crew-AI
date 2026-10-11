from crewai import Agent
from tools import tool
import os
from dotenv import load_dotenv

load_dotenv()

# Load Google API key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Gemini model
llm = "gemini/gemini-3.5-flash"

# --------------------------------------------------
# Researcher Agent
# --------------------------------------------------

blog_researcher = Agent(
    role="Blog Researcher",
    
    goal=(
        "Research the topic {topic} and identify the latest "
        "important information, trends, advantages, disadvantages, "
        "market opportunities, and potential risks."
    ),
    
    backstory=(
        "You are an expert technology researcher specializing in "
        "AI, Data Science, Machine Learning, and Generative AI. "
        "You are skilled at finding accurate and useful information "
        "and presenting it clearly."
    ),
    
    verbose=True,
    memory=True,
    tools=[tool],
    llm=llm,
    allow_delegation=False
)

# --------------------------------------------------
# Writer Agent
# --------------------------------------------------

blog_writer = Agent(
    role="Technology Blog Writer",
    
    goal=(
        "Write an engaging and easy-to-understand article about "
        "{topic} using the research provided by the researcher."
    ),
    
    backstory=(
        "You are an experienced technology writer who can simplify "
        "complex technical concepts into engaging and educational "
        "articles. Your writing is clear, accurate, and accessible."
    ),
    
    verbose=True,
    memory=True,
    tools=[tool],
    llm=llm,
    allow_delegation=False
)