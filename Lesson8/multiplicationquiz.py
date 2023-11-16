import random,time
numberOfQuestions = 10
correctAnswers = 0
print("You get 8 seconds to answer a question")
def exit():
    print("Incorrect")
for questionNumber in range(numberOfQuestions):
    tries=0
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    start = time.time()
    a= int(input(f"{num1}*{num2}= "))
    end= time.time()
    time_taken= end-start
    if a==num1*num2 and time_taken<=8:
        print("Correct")
        correctAnswers+=1
        time.sleep(1)
    elif time_taken==9:
        print("Incorrect, out of time limit")

    elif a!=num1*num2 and time_taken<=8:
        for j in range(2):
            print("Incorrect, try to answer again")
            startingtime=time.time()
            a= int(input(f"{num1}*{num2}= "))
            endingtime=time.time()
            time_taken_a= endingtime-startingtime
            tries+=1
            if a==num1*num2 and time_taken_a<=8:
                print("Correct")
                correctAnswers+=1
                time.sleep(1)
                break
            else:
                print("Out of time limit")
                break

        print("Incorrect")

        if tries>3:
            break
    else:
        print("Incorrect")
print("Number of correct answers = ", correctAnswers)