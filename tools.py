from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool

load_dotenv()

# Load Serper API key
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# Initialize Serper tool
tool = SerperDevTool()