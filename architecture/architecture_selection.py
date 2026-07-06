def choose(problem):

    problem = problem.lower()

    if "pdf" in problem:
        return "Single Agent"

    elif "medical" in problem:
        return "Expertise Separation"

    elif "ocr" in problem:
        return "Pipeline"

    elif "customer support" in problem:
        return "Supervisor"

    elif "review" in problem:
        return "Debate"

    return "Single Agent"


while True:

    problem = input("Problem: ")

    if problem == "exit":
        break

    print("Recommended Architecture:", choose(problem))