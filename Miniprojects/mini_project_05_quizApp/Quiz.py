questions = {
    "What is the capital of France? ": "paris",
    "What is 5 + 7? ": "12",
    "Who wrote Hamlet? ": "shakespeare"
}

score = 0
for q, a in questions.items():
    ans = input(q).strip().lower()
    if ans == a:
        score += 1

print(f"You got {score}/{len(questions)} correct!")
