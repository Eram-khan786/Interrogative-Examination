print("Welcome to my Interrogative Examination!")

playing= input("Do you wanna Play?  ")

if playing.lower()!="yes":
    quit()
print("Okay! Let's play :)")

score=0


Question=input("Who developed Python Programming Language? ").lower()
if Question==("Guido van Rossum").lower():
    print("Correct! :)")
    score+=1
else:
    print("Not Correct! :( ")



Question=input(" Is Python case sensitive when dealing with identifiers? ").lower()
if Question==("Yes").lower():
    print("Correct! :)")
    score+=1
else:
    print("Not Correct! :( ")

Question=input("What will be the value of the following Python expression?  4 + 3 % 5 ")
if Question==("7"):
    print("Correct! :)")
    score+=1
else:
    print("Not Correct! :( ")


Question=input(". Which keyword is used for function in Python language? ").lower()
if Question==("def").lower():
    print("Correct! :)")
    score+=1
else:
    print("Not Correct! :( ")


Question=input(" Python supports the creation of anonymous functions at runtime, using a construct called ").lower()
if Question==("lambda").lower():
    print("Correct! :)")
    score+=1
else:
    print("Not Correct! :( ")


Question=input("What does pip stand for python? ").lower()
if Question==("Preferred Installer Program").lower():
    print("Correct! :)")
    score+=1
else:
    print("Not Correct! :( ")


Question=input("What will be the output of the following Python expression? round(4.576) ")
if Question=="5":
    print("Correct! :)")
    score+=1
else:
    print("Not Correct! :( ")



Question=input(" What is output of print(math.pow(3, 2))? ")
if Question=="9":
    print("Correct! :)")
    score+=1
else:
    print("Not Correct! :( ")


Question=input(" In which language python is written? ").lower()
if Question==("c").lower():
    print("Correct! :)")
    score+=1
else:
    print("Not Correct! :( ")



Question=input(" List in Python is ................in nature. ").lower()
if Question==("mutable").lower():
    print("Correct! :)")
    score+=1
else:
    print("Not Correct! :( ")

print("You got " + str(score) + "questions correct :)")
print("You got " + str((score/10)*100) + "%.")