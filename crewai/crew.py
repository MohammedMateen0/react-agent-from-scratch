from crewai import Agent,Task,Crew,LLM

llm=LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
    temperature=0
)
researcher=Agent(
    role="Restaurant Researcher",
    goal="Find the best restaurants in Hyderabad",
    backstory='''
    You are an experienced food critic with
    10 years of experience reviewing restaurants.
    ''',
    llm=llm,
    verbose=True
)
research_task=Task(
    description="Find the best restaurants in Hyderabad.",
    expected_output="A ranked list of the top 5 restaurants.",
    agent=researcher
)
crew=Crew(
    agents=[researcher],
    tasks=[research_task],
    llm=llm,
    verbose=True,
)

result=crew.kickoff()
print(result)