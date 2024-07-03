import math
import random

questions = [
    {
        "question": "Which is the oldest national park in Nepal?",
        "options": ["A. Sagarmatha National Park", "B. Rara National Park", "C. Chitwan National Park", "D. Makalu Barun National Park"],
        "answer": "C"
    },
    {
        "question": "In which year was the first successful ascent of Mount Everest, the highest peak in Nepal and the world, achieved?",
        "options": ["A. 1952", "B. 1953", "C. 1954", "D. 1955"],
        "answer": "B"
    },
    {
        "question": "What is the national bird of Nepal?",
        "options": ["A. Himalayan Monal", "B. Peacock", "C. Great Hornbill", "D. Indian Roller"],
        "answer": "A"
    },
    {
        "question": "Which is the longest river that flows entirely within Nepal?",
        "options": ["A. Koshi River", "B. Karnali River", "C. Gandaki River", "D. Bagmati River"],
        "answer": "A"
    },
    {
        "question": "Who composed the current national anthem of Nepal ('Sayaun Thunga Phulka')?",
        "options": ["A. King Tribhuvan", "B. King Mahendra", "C. Amber Gurung", "D. Chakrapani Chalise"],
        "answer": "C"
    },
    {
        "question": "Which ancient city in Nepal is known as the 'City of Devotees'?",
        "options": ["A. Bhaktapur", "B. Patan", "C. Lumbini", "D. Janakpur"],
        "answer": "A"
    },
    {
        "question": "In which district of Nepal is the world's deepest gorge, the Kali Gandaki Gorge, located?",
        "options": ["A. Mustang", "B. Dolpa", "C. Solukhumbu", "D. Manang"],
        "answer": "A"
    },
    {
        "question": "What is the average elevation of the Kathmandu Valley, where the capital city is located?",
        "options": ["A. Around 1,000 meters", "B. Around 1,400 meters", "C. Around 1,800 meters", "D. Around 2,200 meters"],
        "answer": "B"
    },
    {
        "question": "Who was the first Nepali to climb Mount Everest without supplemental oxygen?",
        "options": ["A. Babu Chiri Sherpa", "B. Pasang Lhamu Sherpa", "C. Ang Rita Sherpa", "D. Tenzing Norgay Sherpa"],
        "answer": "A"
    },
    {
        "question": "Which ancient trade route passed through Nepal, connecting India and Tibet?",
        "options": ["A. Silk Road", "B. Spice Route", "C. Salt Route", "D. Tea Horse Road"],
        "answer": "D"
    }
]

random.shuffle(questions)

def pick_random_questions(elements, no_of_question):
    if no_of_question > len(elements):
        raise ValueError("Number of picks exceeds the number of elements in the list")
    choosen_questions = random.sample(elements, no_of_question)
    return choosen_questions

no_of_players = 0
while no_of_players < 1:
    no_of_players = int(input("Enter the number of players: "))

user_names = []
no_of_question_per_person = math.floor(len(questions) / no_of_players)
print(f"Each player will get {no_of_question_per_person} questions.")
for i in range(no_of_players):
    player_name = input(f"Enter name of player {i+1}: ")
    user_names.append(player_name)

remaining_questions = questions[:]

scores = []
for index, player in enumerate(user_names, start=1):
    print(f"{index}. For {player}")
    point = 0
    player_questions = pick_random_questions(remaining_questions, no_of_question_per_person)
    
    # Remove selected questions from the remaining questions
    remaining_questions = [q for q in remaining_questions if q not in player_questions]
    
    for question in player_questions:
        print(f"{question['question']}")
        for option in question['options']:
            print(option)
        user_ans = input("Enter your answer: ").upper()
        if user_ans == question['answer']:
            print("You are correct")
            point += 1
        else:
            print("You are wrong")
        print("\n")
    scores.append(point)
    print("-----------------------------------")

user_scores = list(zip(user_names, scores))
print(user_scores)

highest_score = max(scores)
highest_scorers = [user for user, score in user_scores if score == highest_score]

print(f"The highest score is: {highest_score}")
print("Users with the highest score:", highest_scorers)
