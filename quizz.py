def ask_question(nb_attempts_left, question_sentence, right_answer): # three arguments
    if nb_attempts_left > 0:
        answer = input(question_sentence)
        answer = answer.lower()
        while answer != right_answer:
            nb_attempts_left -=1
            print("Too bad! that is not the correct answer. You have {} left".format(nb_attempts_left))
            if nb_attempts_left == 0:
                print("Oh no, you lost the quiz...")
                break
            answer = input(question_sentence)
            answer = answer.lower()       
    print('')
    return nb_attempts_left

questions_answers_list = [
    ("How many times France soccer team won the world cup ? ", "2"),
    ("What year was the movie 'Rocky' released ? ", "1976"),
    ("Who is the founder of Tesla ? ", "elon musk")
]

nb_attempts = 3

for question, answer in questions_answers_list :
    nb_attempts = ask_question(nb_attempts, question, answer) # calling the function

if nb_attempts > 0:
    print("Good job! This is the right answer. You finished the Quizz !")