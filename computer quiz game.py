
# computer quiz game

print("Welcome to my computer quiz game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's play: ")
score = 0

question1 = input("What does OS stand for? ")
if question1.lower() == "operating system":
    print("correct!")
    score += 1
else:
    print("incorrect")

question2 = input("What does Mac stand for? ")
if question2.lower() == "macintosh":
    print("correct!")
    score += 1
else:
    print("incorrect")

question3 = input("What does HDD stand for? ")
if question3.lower() == "hard disk drive":
    print("correct!")
    score += 1
else:
    print("incorrect")

question4 = input("What does RAM stand for? ")
if question4.lower() == "read access memory":
    print("correct!")
    score += 1
else:
    print("incorrect")

question5 = input("What does ROM stand for? ")
if question5.lower() == "read only memory":
    print("correct!")
    score += 1
else:
    print("incorrect")

question6 = input("What does BIOS stand for? ")
if question6.lower() == "basic input output system":
    print("correct!")
    score += 1
else:
    print("incorrect")

question7 = input("What does LAN stand for? ")
if question7.lower() == "local area network":
    print("correct!")
    score += 1
else:
    print("incorrect")

question8 = input("What does IP stand for? ")
if question8.lower() == "internet protocol":
    print("correct!")
    score += 1
else:
    print("incorrect")

question9 = input("What does USB stand for? ")
if question9.lower() == "universal serial bus":
    print("correct!")
    score += 1
else:
    print("incorrect")

question10 = input("What does SSD stand for? ")
if question10.lower() == "solid state drive":
    print("correct!")
    score += 1
else:
    print("incorrect")

print("You got " + str((score / 10) * 100) + "%")
