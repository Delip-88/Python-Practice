import random

# List of questions with options and answers
# questions = [
#     {
#         "question": "Which is the oldest national park in Nepal?",
#         "options": ["A. Sagarmatha National Park", "B. Rara National Park", "C. Chitwan National Park", "D. Makalu Barun National Park"],
#         "answer": "C"
#     },
#     {
#         "question": "In which year was the first successful ascent of Mount Everest, the highest peak in Nepal and the world, achieved?",
#         "options": ["A. 1952", "B. 1953", "C. 1954", "D. 1955"],
#         "answer": "B"
#     },
#     {
#         "question": "What is the national bird of Nepal?",
#         "options": ["A. Himalayan Monal", "B. Peacock", "C. Great Hornbill", "D. Indian Roller"],
#         "answer": "A"
#     },
#     {
#         "question": "Which is the longest river that flows entirely within Nepal?",
#         "options": ["A. Koshi River", "B. Karnali River", "C. Gandaki River", "D. Bagmati River"],
#         "answer": "A"
#     },
#     {
#         "question": "Who composed the current national anthem of Nepal ('Sayaun Thunga Phulka')?",
#         "options": ["A. King Tribhuvan", "B. King Mahendra", "C. Amber Gurung", "D. Chakrapani Chalise"],
#         "answer": "C"
#     },
#     {
#         "question": "Which ancient city in Nepal is known as the 'City of Devotees'?",
#         "options": ["A. Bhaktapur", "B. Patan", "C. Lumbini", "D. Janakpur"],
#         "answer": "A"
#     },
#     {
#         "question": "In which district of Nepal is the world's deepest gorge, the Kali Gandaki Gorge, located?",
#         "options": ["A. Mustang", "B. Dolpa", "C. Solukhumbu", "D. Manang"],
#         "answer": "A"
#     },
#     {
#         "question": "What is the average elevation of the Kathmandu Valley, where the capital city is located?",
#         "options": ["A. Around 1,000 meters", "B. Around 1,400 meters", "C. Around 1,800 meters", "D. Around 2,200 meters"],
#         "answer": "B"
#     },
#     {
#         "question": "Who was the first Nepali to climb Mount Everest without supplemental oxygen?",
#         "options": ["A. Babu Chiri Sherpa", "B. Pasang Lhamu Sherpa", "C. Ang Rita Sherpa", "D. Tenzing Norgay Sherpa"],
#         "answer": "A"
#     },
#     {
#         "question": "Which ancient trade route passed through Nepal, connecting India and Tibet?",
#         "options": ["A. Silk Road", "B. Spice Route", "C. Salt Route", "D. Tea Horse Road"],
#         "answer": "D"
#     }
# ]


questions = [
    {
        "question": "Which is the only mammal capable of flight?",
        "options": ["A. Bat", "B. Eagle", "C. Penguin", "D. Dolphin"],
        "answer": "A"
    },
    {
        "question": "Who painted the famous painting 'Starry Night'?",
        "options": ["A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Claude Monet"],
        "answer": "A"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["A. Monaco", "B. Vatican City", "C. Liechtenstein", "D. San Marino"],
        "answer": "B"
    },
    {
        "question": "Who wrote the novel '1984'?",
        "options": ["A. George Orwell", "B. Aldous Huxley", "C. J.D. Salinger", "D. Ray Bradbury"],
        "answer": "A"
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["A. Sahara Desert", "B. Arabian Desert", "C. Gobi Desert", "D. Antarctic Desert"],
        "answer": "A"
    },
    {
        "question": "Which metal is liquid at room temperature?",
        "options": ["A. Silver", "B. Mercury", "C. Gold", "D. Copper"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'The Great Gatsby'?",
        "options": ["A. F. Scott Fitzgerald", "B. Ernest Hemingway", "C. John Steinbeck", "D. Virginia Woolf"],
        "answer": "A"
    },
    {
        "question": "Which planet has the most moons in our solar system?",
        "options": ["A. Jupiter", "B. Saturn", "C. Neptune", "D. Uranus"],
        "answer": "A"
    },
    {
        "question": "What is the largest species of big cat?",
        "options": ["A. Lion", "B. Tiger", "C. Cheetah", "D. Jaguar"],
        "answer": "B"
    },
    {
        "question": "Who was the first person to set foot on the Moon?",
        "options": ["A. Neil Armstrong", "B. Buzz Aldrin", "C. Michael Collins", "D. Yuri Gagarin"],
        "answer": "A"
    },
    {
        "question": "What is the largest continent by land area?",
        "options": ["A. Africa", "B. Europe", "C. Asia", "D. North America"],
        "answer": "C"
    },
    {
        "question": "Which river flows through the Grand Canyon?",
        "options": ["A. Colorado River", "B. Mississippi River", "C. Amazon River", "D. Nile River"],
        "answer": "A"
    },
    {
        "question": "Who discovered penicillin?",
        "options": ["A. Alexander Fleming", "B. Louis Pasteur", "C. Jonas Salk", "D. Robert Koch"],
        "answer": "A"
    },
    {
        "question": "What is the largest species of bear?",
        "options": ["A. Polar Bear", "B. Grizzly Bear", "C. Kodiak Bear", "D. Brown Bear"],
        "answer": "A"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["A. China", "B. Japan", "C. South Korea", "D. Vietnam"],
        "answer": "B"
    },
    {
        "question": "Who is known as the Father of the Computer?",
        "options": ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"],
        "answer": "A"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon dioxide", "D. Hydrogen"],
        "answer": "C"
    },
    {
        "question": "Who wrote the play 'Hamlet'?",
        "options": ["A. William Shakespeare", "B. Christopher Marlowe", "C. John Milton", "D. Geoffrey Chaucer"],
        "answer": "A"
    },
    {
        "question": "What is the tallest breed of dog?",
        "options": ["A. Great Dane", "B. Irish Wolfhound", "C. Saint Bernard", "D. Mastiff"],
        "answer": "A"
    },
    {
        "question": "In which city is the headquarters of the United Nations located?",
        "options": ["A. Geneva", "B. Paris", "C. New York City", "D. Vienna"],
        "answer": "C"
    },
    {
        "question": "Who painted the ceiling of the Sistine Chapel?",
        "options": ["A. Leonardo da Vinci", "B. Raphael", "C. Michelangelo", "D. Donatello"],
        "answer": "C"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Diamond", "C. Titanium", "D. Graphite"],
        "answer": "B"
    },
    {
        "question": "Which country is known as the Emerald Isle?",
        "options": ["A. Iceland", "B. Scotland", "C. Ireland", "D. Greenland"],
        "answer": "C"
    },
    {
        "question": "Who discovered the theory of general relativity?",
        "options": ["A. Albert Einstein", "B. Isaac Newton", "C. Niels Bohr", "D. Max Planck"],
        "answer": "A"
    },
    {
        "question": "What is the largest species of shark?",
        "options": ["A. Great White Shark", "B. Whale Shark", "C. Hammerhead Shark", "D. Tiger Shark"],
        "answer": "B"
    },
    {
        "question": "Who wrote the novel 'Pride and Prejudice'?",
        "options": ["A. Jane Austen", "B. Emily Brontë", "C. Charlotte Brontë", "D. Louisa May Alcott"],
        "answer": "A"
    },
    {
        "question": "Which country has won the most FIFA World Cup titles?",
        "options": ["A. Brazil", "B. Germany", "C. Italy", "D. Argentina"],
        "answer": "A"
    },
    {
        "question": "Who painted 'The Persistence of Memory', featuring melting clocks?",
        "options": ["A. Salvador Dalí", "B. Pablo Picasso", "C. Vincent van Gogh", "D. Claude Monet"],
        "answer": "A"
    },
    {
        "question": "What is the chemical symbol for iron?",
        "options": ["A. Ir", "B. Fe", "C. In", "D. Io"],
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

