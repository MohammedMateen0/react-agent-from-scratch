from crewai import Agent

researcher=Agent(
    role="Restaurant Researcheer",
    goal="Find the best restaurants in Hyderabad",
    backstory="You are an experienced food critic with 10 years of experience reviewing restaurants.",
    verbose=True
)
print(researcher)