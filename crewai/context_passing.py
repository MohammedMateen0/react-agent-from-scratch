from crewai import Agent,Task,Process,LLM,Crew 

llm=LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
    temperature=0
)

researcher=Agent(
    role="Restaurent Researcher.",
    goal="Find the best restaurants in Hyderabad.",
    backstory="Expert food researcher.",
    llm=llm,
    verbose=True
)
analyst=Agent(
    role="Food Analyst",
    goal="Compare restaurants objectively.",
    backstory="Expert in restaurant comparison.",
    llm=llm,
    verbose=True
)
writer=Agent(
    role="Food writer",
    goal="Write a professional report",
    backstory="Write restaurant reports.",
    llm=llm,
    verbose=True
)
research_task=Task(
    description="Research the best restaurants in Hyderabad.",
    expected_output="Top 5 restaurants with ratings, cuisine, price and location.",
    agent=researcher
)
analysis_task=Task(
    description="Analyze the researched restaurants and rank them.",
    expected_output="Comparison table with pros and cons.",
    agent=analyst,
    context=[research_task]
)
report_task=Task(
    description="Write a professional report from the analysis.",
    expected_output="Executive summary and recommendations.",
    agent=writer,
    context=[
        research_task,
        analysis_task
    ]
)
crew=Crew(
    agents=[
        researcher,
        analyst,
        writer
    ],
    tasks=[
        research_task,
        analysis_task,
        report_task
    ],
    process=Process.sequential,
    llm=llm,
    verbose=True
)
result = crew.kickoff()

print("\n===== FINAL OUTPUT =====")
print(result)

print("\n===== RESEARCH TASK =====")
print(research_task.output)

print("\n===== ANALYSIS TASK =====")
print(analysis_task.output)

print("\n===== REPORT TASK =====")
print(report_task.output)
