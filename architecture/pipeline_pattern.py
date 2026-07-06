def extractor(text):
    return text.upper()


def summarizer(text):
    return text[:40]


def reviewer(text):
    return f"Reviewed: {text}"


document = "This is a very long document about AI Agents and LangGraph."

step1 = extractor(document)

step2 = summarizer(step1)

step3 = reviewer(step2)

print(step3)