from crewai import Task
from tools import tool
from agents import blog_researcher, blog_writer

# --------------------------------------------------
# Research Task
# --------------------------------------------------

research_task = Task(
    description=(
        "Research the topic {topic}. "
        "Identify the latest trends, important developments, "
        "advantages, disadvantages, market opportunities, "
        "and potential risks. "
        "Make sure the information is accurate and relevant."
    ),
    
    expected_output=(
        "A comprehensive research report about {topic}, "
        "covering the latest trends, key developments, "
        "advantages, disadvantages, market opportunities, "
        "and potential risks."
    ),
    
    tools=[tool],
    agent=blog_researcher
)

# --------------------------------------------------
# Writing Task
# --------------------------------------------------

write_task = Task(
    description=(
        "Write an insightful article about {topic} using the "
        "research provided by the researcher. "
        "Focus on the latest trends and explain how they are "
        "impacting the industry. "
        "The article should be engaging, informative, "
        "easy to understand, and well structured."
    ),
    
    expected_output=(
        "A well-written Markdown article about {topic}, "
        "including an introduction, major trends, "
        "industry impact, benefits, challenges, "
        "and a conclusion."
    ),
    
    tools=[tool],
    agent=blog_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)