import random as rd

def generate_integer(min, max):
    """function to generate a random integer"""
    return rd.randint(min, max)
    
def generate_operator():
    """function to generate a random arithmetic operation"""
    return rd.choice(['+', '-', '*'])


def calculation(n1, n2, o):
    """ function to calculate the solution for generated numbers and operation """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    score = 0         # initial score
    total_quest = 3    # total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_quest):
        # generate integers and operations
        n1 = generate_integer(1, 10) 
        n2 = generate_integer(1, 5)
        o = generate_operation()   

        PROBLEM, ANSWER = calculation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        # check user input with try-ecxept statement
        while True:
            try:
                userinput = input("Your answer: ")
                useranswer = int(userinput)
                break  # if input is valid, loop breaks
            except ValueError:
                print("The input was not valid. Only integers.") # else the error message occurs
        # check the user answer
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_quest}")

if __name__ == "__main__":
    math_quiz()
