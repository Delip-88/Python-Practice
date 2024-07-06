import math
import random
import quiz_question

questions = quiz_question.questions
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
    
    for i,question in enumerate(player_questions,start=1):
        print(f"{i}. {question['question']}")
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
