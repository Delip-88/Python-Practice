import random

# List of questions with options and answers

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Jupiter", "B. Mars", "C. Venus", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"],
        "answer": "A"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. H2O", "B. CO2", "C. O2", "D. N2"],
        "answer": "A"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["A. K2", "B. Kangchenjunga", "C. Mount Everest", "D. Lhotse"],
        "answer": "C"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Oxygen", "C. Osmium", "D. Opium"],
        "answer": "B"
    },
    {
        "question": "Who was the first President of the United States?",
        "options": ["A. Thomas Jefferson", "B. Abraham Lincoln", "C. George Washington", "D. John Adams"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Neptune"],
        "answer": "B"
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["A. Amazon River", "B. Nile River", "C. Yangtze River", "D. Mississippi River"],
        "answer": "B"
    }
]

# Shuffle the questions
random.shuffle(questions)

score = 0
print("Welcome to the Quiz!\n")

# Loop through each question
for index, question in enumerate(questions, start=1):  # start=1 for user-friendly numbering
    print(f"Question {index}: {question['question']}")
    for option in question['options']:
        print(option)
    user_ans = input("Enter your answer: ").strip().upper()
    
    # Check the answer
    if user_ans == question['answer']:
        score += 1
        print("It's correct.")
    else:
        print(f"It's wrong. The correct answer is {question['answer']}.")
    
    print("______________\n")

# Display the total score
print(f"Your total score is: {score}/{len(questions)}")

