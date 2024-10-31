from transformers import pipeline

# Load the question answering pipeline
qa_pipeline = pipeline('question-answering', model="deepset/roberta-base-squad2")

# Define the contexts and questions
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
            }
        ]
    }
]

# Welcome message
print("Welcome to the Trivia Game!")

# Loop for multiple rounds
while True:

    # Display genre options
    print("\nAvailable Genres:")
    for i, context in enumerate(contexts_and_questions):
        print(f"{i+1}. {context['genre']}")

    # Get user choice for genre
    while True:
        try:
            genre_choice = int(input("\nChoose a genre (1-{} or 0 to exit): ".format(len(contexts_and_questions))))
            if 0 <= genre_choice <= len(contexts_and_questions):
                break
            else:
                print("Invalid choice. Please enter a number between 1 and {} or 0 to exit.".format(len(contexts_and_questions)))
        except ValueError:
            print("Invalid input. Please enter a number.")

    if genre_choice == 0:
        break

    # Get context based on user choice
    chosen_context = contexts_and_questions[genre_choice - 1]
    print("\nContext:", chosen_context["context"])

    # Ask if user wants pre-defined question or their own
    question_type = input("\nDo you want to answer a pre-defined question (y/n) or ask your own (o)? ").lower()

    # Answer pre-defined questions
    if question_type in ("y", "yes"):
        for question in chosen_context["questions"]:
            answer = qa_pipeline({"question": question["question"], "context": chosen_context["context"]})
            user_score = 1 if answer["answer"] == question["expected_answer"] else 0
            print(f"\nQuestion: {question['question']}")
            print(f"Model Answer: {answer['answer']}")
            print(f"Expected Answer: {question['expected_answer']}")
            print(f"Your Score: {user_score}")

    # Handle user-defined questions
    elif question_type in ("o", "other"):
        user_question = input("\nAsk your question: ")
        answer = qa_pipeline({"question": user_question, "context": chosen_context["context"]})
        print(f"\nModel Answer: {answer['answer']}")

    # Provide feedback and continue
    print("\nWould you like to continue playing? (y/n)")
    if input().lower() not in ("y", "yes"):
        break

# Game over
print("\nThank you for playing!")