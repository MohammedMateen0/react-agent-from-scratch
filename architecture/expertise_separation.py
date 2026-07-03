from crewai import Agent,Task,Crew,Process,LLM
llm=LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)
food_agent=Agent(
    role="Food Expert",
    goal="Recommend restaurants",
    backstory="Expert on Hyderabad cuisine.",
    llm=llm,
    verbose=True
)
hotel_agent=Agent(
    role="Hotel Expert",
    goal="Recommend hotels",
    backstory="Expert on Hyderabad hotels.",
    llm=llm,
    verbose=True
)
travel_agent=Agent(
    role="Travel Expert",
    goal="Recommend tourist attractions and transport",
    backstory="Expert travel planner",
    llm=llm,
    verbose=True
)
food_task=Task(
    description='''
    Recommend the best restaurants
    for a tourist visiting Hyderabad.
    ''',
    expected_output="Restaurant recommendations",
    agent=food_agent
)
hotel_task=Task(
    description='''
    Recommend hotels under ₹5000/night.
''',
    expected_output="Hotel recommendations",
    agent=hotel_agent
)
travel_task=Task(
    description='''
    Recommend tourist places
    and transport options.
    ''',
    expected_output="Travel plan",
    agent=travel_agent
)
crew=Crew(
    agents=[
        food_agent,
        hotel_agent,
        travel_agent
    ],
    tasks=[
        food_task,
        hotel_task,
        travel_task
    ],
    process=Process.sequential,
    llm=llm,
    verbose=True
)
result=crew.kickoff()
print(result)