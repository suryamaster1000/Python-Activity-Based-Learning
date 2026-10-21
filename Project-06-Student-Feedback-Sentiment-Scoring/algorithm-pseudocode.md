# Project 06 — Algorithm and Pseudocode

## Algorithm

1. Start the program and define positive and negative keyword lists.
2. Ask for the number of feedback responses; repeat until the count is at least 1.
3. For each response:
   - Read the comment.
   - Convert it to lowercase and replace basic punctuation with spaces.
   - Split the comment into words.
   - Count words that match the positive and negative lists.
   - Calculate score = positive matches − negative matches.
   - Classify the score as positive, negative, or neutral.
   - Store the original comment and results in a tuple.
4. Display each comment's keyword counts, score, and classification.
5. Display the overall response and keyword totals.
6. End the program.

## Pseudocode

~~~text
START
  DEFINE positive_words
  DEFINE negative_words
  INPUT feedback_count
  WHILE feedback_count < 1
    DISPLAY request for at least one response
    INPUT feedback_count
  END WHILE

  SET result list and summary counters

  FOR each feedback response
    INPUT comment
    CONVERT comment to lowercase
    REPLACE basic punctuation with spaces
    SPLIT comment into words
    SET positive_matches = 0
    SET negative_matches = 0

    FOR each word
      IF word is in positive_words
        INCREASE positive_matches
      END IF
      IF word is in negative_words
        INCREASE negative_matches
      END IF
    END FOR

    score = positive_matches - negative_matches
    IF score > 0
      sentiment = POSITIVE
    ELSE IF score < 0
      sentiment = NEGATIVE
    ELSE
      sentiment = NEUTRAL
    END IF

    STORE (comment, counts, score, sentiment)
    UPDATE summary counters
  END FOR

  DISPLAY detailed results
  DISPLAY overall summary
END
~~~

## Important limitation

The rule matches words, not meaning. Negation (such as “not good”), sarcasm, and context are not understood by this program.
