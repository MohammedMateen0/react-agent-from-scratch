def food_agent(question):
    return "Food recommendation"
def hotel_agent(question):
    return "Hotel recommendation"
def travel_agent(question):
    return "Travel recommendation"

def supervisor(question):
    q=question.lower()
    if "restaurant" in q or "foos" in q or "biryani" in q:
        return food_agent(question)
    elif "hotel" in q:
        return hotel_agent(question)
    elif "travel" in q or "metro" in q:
        return travel_agent(question)
while True:
    question=input("Ask: ")
    if question.lower()=="exit":
        break
    print(supervisor(question))