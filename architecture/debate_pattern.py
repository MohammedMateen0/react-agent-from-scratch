def solver(question):

    return "Answer: 450"


def critic(answer):

    if "450" in answer:
        return "Looks correct."

    return "Incorrect."


def judge(answer, review):

    return f"{answer}\nReview: {review}"


question = "25 * 18"

answer = solver(question)

review = critic(answer)

final = judge(answer, review)

print(final)