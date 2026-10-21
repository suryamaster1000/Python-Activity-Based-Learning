print("STUDENT FEEDBACK SENTIMENT SCORING")
print("-----------------------------------")

positive_words = [
    "good", "great", "excellent", "helpful", "clear",
    "interesting", "enjoy", "easy", "supportive", "satisfied"
]

negative_words = [
    "bad", "poor", "confusing", "unclear", "boring",
    "difficult", "hard", "slow", "weak", "problem"
]

feedback_count = int(input("Enter number of feedback responses: "))

while feedback_count < 1:
    print("Please enter at least one feedback response.")
    feedback_count = int(input("Enter number of feedback responses: "))

results = []

positive_feedback_count = 0
negative_feedback_count = 0
neutral_feedback_count = 0
total_positive_matches = 0
total_negative_matches = 0

for i in range(feedback_count):
    print("\nEnter feedback", i + 1)
    feedback = input("Feedback: ").strip()

    # Replace basic punctuation so words at sentence boundaries are counted.
    feedback_text = feedback.lower()
    feedback_text = feedback_text.replace(".", " ")
    feedback_text = feedback_text.replace(",", " ")
    feedback_text = feedback_text.replace("!", " ")
    feedback_text = feedback_text.replace("?", " ")
    feedback_text = feedback_text.replace(";", " ")
    feedback_text = feedback_text.replace(":", " ")
    feedback_text = feedback_text.replace("(", " ")
    feedback_text = feedback_text.replace(")", " ")
    feedback_text = feedback_text.replace('"', " ")
    feedback_text = feedback_text.replace("'", " ")

    words = feedback_text.split()
    positive_matches = 0
    negative_matches = 0

    for word in words:
        if word in positive_words:
            positive_matches = positive_matches + 1
        if word in negative_words:
            negative_matches = negative_matches + 1

    score = positive_matches - negative_matches

    if score > 0:
        sentiment = "POSITIVE"
        positive_feedback_count = positive_feedback_count + 1
    elif score < 0:
        sentiment = "NEGATIVE"
        negative_feedback_count = negative_feedback_count + 1
    else:
        sentiment = "NEUTRAL"
        neutral_feedback_count = neutral_feedback_count + 1

    result = (feedback, positive_matches, negative_matches, score, sentiment)
    results.append(result)

    total_positive_matches = total_positive_matches + positive_matches
    total_negative_matches = total_negative_matches + negative_matches

print("\nFEEDBACK ANALYSIS REPORT")
print("------------------------")

for i in range(len(results)):
    result = results[i]
    print("\nFeedback", i + 1, ":", result[0])
    print("Positive keyword matches:", result[1])
    print("Negative keyword matches:", result[2])
    print("Sentiment score:", result[3])
    print("Classification:", result[4])

print("\nOVERALL SUMMARY")
print("----------------")
print("Feedback responses analysed:", len(results))
print("Positive responses:", positive_feedback_count)
print("Negative responses:", negative_feedback_count)
print("Neutral responses:", neutral_feedback_count)
print("Positive keyword matches:", total_positive_matches)
print("Negative keyword matches:", total_negative_matches)
print("\nAnalysis complete. Read the original comments as well as their scores.")
