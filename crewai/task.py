from crewai import Agent,Task

researcher=Agent(
    role="Restaurant Researcher",
    goal="Find the best restaurants in Hyderabad",
    backstory="""
    You are an experienced food critic with
    10 years of experience reviewing restaurants
    """,
    verbose=True
)
research_task=Task(
    description="Find the best restaurants in Hyderabad.",
    expected_output="A ranked list of the top 5 restaurants.",
    agent=researcher
)
print(research_task)