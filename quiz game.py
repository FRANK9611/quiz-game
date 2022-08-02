print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! lets play :)")
score = 0

answer = input("What does employee mean? ")
if answer.lower()  == "worker":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("How many months are there in a year? ")
if answer.lower() == "12":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("How did Tom win Jakcon? ")
if answer.lower() == "by a knife":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does run mean in uzbek language? ")
if answer.lower() == "yugurmoq":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("How many bottles coca cola were sold in first year ? ")
if answer.lower() == "25":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is Japanese currency? ")
if answer.lower() == "Yen":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str ((score / 6) * 100)  + "%.")
