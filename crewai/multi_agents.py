from crewai import Task,Crew,Agent,Process,LLM

llm=LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
    temperature=0
)
researcher=Agent(
    role="Restaurant Researcher",
    goal="Find the best restaurants in Hyderabad",
    backstory="Expert food researcher.",
    llm=llm,
    verbose=True
)
analyst=Agent(
    role="Food Analyst",
    goal="Compare restaurants objectively",
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
    description="""Find 10 restaurants.

Collect

• Rating
• Cuisine
• Price
• Location""",
    expected_output="A list of the top 5 restaurants.",
    agent=researcher
)
analysis_task=Task(
    description="""Compare them.

Rank using

• Rating

• Price

• Ambience

• Value

Return a table.""",
    expected_output="Restaurant comparison.",
    agent=analyst
)
report_task=Task(
    description="""Create

Executive Summary

Detailed Analysis

Recommendation

Conclusion""",
    expected_output="Final restaurant report.",
    agent=writer
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