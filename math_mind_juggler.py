import random 
import time

NUMBER_PROBLEMS = 10
MIN_OPERAND = 3
MAX_OPERAND = 10
problems = []


def generate_problem():
    for _ in range(NUMBER_PROBLEMS):
        a = random.randint(MIN_OPERAND,MAX_OPERAND)
        b= random.randint(MIN_OPERAND,MAX_OPERAND)

        operation = ["*", "+", "-" ]
        expression = random.choice(operation)

        question = f"{a}" + expression + f"{b}" 

        problems.append(question)
    


answer = input("Press enter or any key to start the game or q to quit ")
print("-----------------------------------------------------")

if answer == "q":
    quit()
else:
    start_time = time.time()

    while True:      
       generate_problem()
       
       for i in range(NUMBER_PROBLEMS):
            
            if i+1 == NUMBER_PROBLEMS:
                finish_time = time.time()
                print(problems)

                print(f"You took {finish_time -start_time} seconds ")
                quit()
            
            question = problems[i]

            player_answer =int(input(f"what is {question} or press q to quit ")) 
            answer = eval(question)

            if player_answer == answer:
                continue
            else:
                finish_time = time.time()
                print(problems)
                print(f"You took {finish_time -start_time} seconds ")
                quit()

    