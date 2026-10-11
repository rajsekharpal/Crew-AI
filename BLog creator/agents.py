from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_GEMINI_MODEL"] = "gemini-3.5-flash"

llm = "gemini-3.5-flash"

## Create a senior blog content researcher
blog_researcher = Agent(
    role='Blog Researcher from youtube video',
    goal="Get the relevent video content for the topic{topic} from youtub channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science,Machine Learning and GenAI and providing suggestion"
    ),tools=[yt_tool],
    llm = llm,
    allow_delegation=True
)

## Creating the senior blog writer agent with yt tool

blog_writer=Agent(
    role="Blog writer",
    goal="Narrate compelling tech stories about the video {topic} from youtube channel",
    verbose=True,
    memory=True,
    backstory=(
        "with a flair for simplify complex topics,you craft"
        "engaging narratives that capture and educate,bringing new"
        "discoveries to light in an accessible manner"

    ),
    tools = [yt_tool],
    llm=llm,
    alow_delegation = False
)