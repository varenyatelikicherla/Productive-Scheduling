def randomize_response(msg_one, msg_two, msg_three, msg_four):
    import random
    rand= random.randint(1,4)
    if rand==1:
        print(msg_one)
    elif rand==2:
        print(msg_two)
    elif rand==3:
        print(msg_three)
    elif rand==4:
        print(msg_four)
def error():
    randomize_response("Sorry I did not catch that. Can you try typing your response in a different way?", "Error! Please try again.", "What was that? I don't understand..", "Oops! I am unable to process what you just said. Type it once more.")
print("Welcome to Productive Scheduling!")
#first_time=input("Is this your first time here?")
while True:
    first_time=input("Is this your first time here?")
    if first_time.lower()=="yes":
        print("Welcome! Make sure to press enter to understand how to use this tool!")
        print("This is where you can schedule events, courses, hobbies, or whatever you want without worrying about scheduling conflicts! Keep pressing enter to get through the instructions!")
        input()
        print("But don't worry, if there are any conflicts, I'll be sure to let you know :) ")
        input()
        break
    elif first_time.lower()=="no":
        print("Nice to see you again!")
        break
    else:
        error()
        continue
while True:
    


