# Overview
Roberta base for QA is a model that can be used to ask and answer questions based on context. Let's create a trivia game with that!

# Instructions
- Go to [this page](https://huggingface.co/deepset/roberta-base-squad2) and read about roberta base for QA. Understand this model and what it does. You can utilize the inference API on the right to test things out.
- With the premade context found below, create a python trivia game where you test whether this model can answer your questions about the different contexts.
- The user should be able to do the following:
  - Choose the genre they want. You should be able to get all the list of genres from the provided array.
  - Give the user the ability to choose one of the already available questions, or simply ask their own questions.
  - After a question is asked, check the answer. Does it provide correct answers? We have added expected answers, to make it easier for you to compare. 
  - Document the models responses, does it return the correct answer? If yes, give it a score of one, otherwise give it a 0.
- Add more trivia questions.
- At the end look at the final results, how did the model perform?
- What could this model be useful for? Discuss that between you.

```python
contexts_and_questions = [
    {
        "context": "The Great Wall of China is one of the most impressive architectural feats in history. Built to protect the Chinese states from invasions and raids, the wall stretches over 13,000 miles. Construction began during the 7th century BC and continued for centuries, with most of the existing wall being built during the Ming dynasty (1368–1644). The wall is made of various materials, including stone, brick, tamped earth, and wood.",
        "genre": "History",
        "questions": [
            {
                "question": "What was the primary purpose of the Great Wall of China?",
                "expected_answer": "To protect the Chinese states from invasions and raids."
            },
            {
                "question": "During which dynasty was most of the existing wall built?",
                "expected_answer": "The Ming dynasty."
            }
        ]
    },
    {
        "context": "Photosynthesis is the process by which green plants, algae, and some bacteria convert light energy, usually from the sun, into chemical energy stored in glucose. This process occurs in the chloroplasts of plant cells and involves the absorption of carbon dioxide from the atmosphere and water from the soil. The end products of photosynthesis are glucose and oxygen, which are crucial for the survival of many living organisms on Earth.",
        "genre": "Science",
        "questions": [
            {
                "question": "What are the end products of photosynthesis?",
                "expected_answer": "Glucose and oxygen."
            },
            {
                "question": "Where in the plant cell does photosynthesis occur?",
                "expected_answer": "In the chloroplasts."
            }
        ]
    },
    {
        "context": "In the magical land of Zoraxia, there existed a tree that bore golden apples, which granted the power of flight to anyone who consumed them. The tree was hidden deep in the Enchanted Forest, guarded by a fierce dragon named Drakon. Legends say that only the bravest of warriors could defeat Drakon and claim the golden apples, but many who tried were never seen again.",
        "genre": "Fiction",
        "questions": [
            {
                "question": "What power did the golden apples grant to anyone who consumed them?",
                "expected_answer": "The power of flight."
            },
        ]
    }
]
```