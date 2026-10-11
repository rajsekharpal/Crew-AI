from crewai import Crew, Process
from task import research_task, write_task
from agents import blog_writer, blog_researcher

# --------------------------------------------------
# Create Crew
# --------------------------------------------------

crew = Crew(
    agents=[
        blog_researcher,
        blog_writer
    ],
    
    tasks=[
        research_task,
        write_task
    ],
    
    process=Process.sequential,
    
    verbose=True
)

# --------------------------------------------------
# Start Crew
# --------------------------------------------------

result = crew.kickoff(
    inputs={
        "topic": "AI in healthcare"
    }
)

print(result)