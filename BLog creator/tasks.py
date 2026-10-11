from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer

## research Task
research_task = Task(
    description=("Identify the video {topic}."
                 "Get detailed information about the video from the channel."),
    expected_output='A comprehensive 3 paragraph long report on the {topic} of video content.',
    tools=[yt_tool],
    agent=blog_researcher

)

# writing task with language model configuration
write_task = Task(
    description=("Get the info from the youtube channel on the topic {topic}"),
    expected_output="Summerize the info from the youtube channel on the topic {topic}",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False, # if true both agent will work parallel
    output_file='new-blog-post.md'
)