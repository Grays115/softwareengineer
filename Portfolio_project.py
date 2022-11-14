print()
print(" --------------------------------------------")
print("| Welcome To The Ultimate NFL Fan Trivia Game|")
print("|--------------------------------------------|")
print("|         Are You A Ultimate Fan?            |")
print("|                                            |")
print("|            Test Your Skills!               |")
print(" --------------------------------------------")
print("\n")

name = input("What is your name? ")
print("\n")
start_message = (f"Goodluck {name}! Ready...Set... Hike!!!")
print(start_message)
print("\n")

# q_1 through q_20 refers to the specific question
# q_1_p_1 thru q_1_p_4 refers to the possible answer


# Question 1

q_1 = ("How many Superbowl rings does Tom Brady have?")
q_1_p_1 = (" A: 3 ")
q_1_p_2 = (" B. 8 ")
q_1_p_3 = (" C. 7 ")
q_1_p_4 = (" D. 8 ")

print(q_1)
print(q_1_p_1)
print(q_1_p_2)
print(q_1_p_3)
print(q_1_p_4)
print()
answer_q_1 = ("Enter Your Answer: ")
print(answer_q_1)
print()

answer_q_1 = input()
count = 0

if (answer_q_1.lower() == "C".lower()):
    print()
    print(f"Correct! Nice Work {name}!")
    count += 1
    print(f"Current Score: {count}/10")
else:
    print()
    print("Wrong Answer!")
    print(f"Current Score: {count}/10")
print()

# Question 2

q_2 = ("Which NFL Franchise joined the NFL most recently?")
q_2_p_1 = (" A: Seattle Seahawks ")
q_2_p_2 = (" B. New York Jets ")
q_2_p_3 = (" C. Tennessee Titans ")
q_2_p_4 = (" D. Houstan Texans ")

print(q_2)
print(q_2_p_1)
print(q_2_p_2)
print(q_2_p_3)
print(q_2_p_4)
print()
answer_q_2 = ("Enter Your Answer: ")
print(answer_q_2)
print()

answer_q_2 = input()

if (answer_q_2.lower() == "D".lower()):
    print()
    print(f"Correct! Nice Work {name}!")
    count += 1
    print(f"Current Score: {count}/10")
else:
    print()
    print("Wrong Answer!")
    print(f"Current Score: {count}/10")
print()

# Question 3

q_3 = ("NFL teams from which two conferences make up the NFL?")
q_3_p_1 = (" A: AFC, NFC")
q_3_p_2 = (" B. OFC, BFC")
q_3_p_3 = (" C. AFC, OFC")
q_3_p_4 = (" D. PFC, NFC")

print(q_3)
print(q_3_p_1)
print(q_3_p_2)
print(q_3_p_3)
print(q_3_p_4)
print()
answer_q_3 = ("Enter Your Answer: ")
print(answer_q_3)
print()

answer_q_3 = input()

if (answer_q_3.lower() == "A".lower()):
    print()
    print(f"Correct! Nice Work {name}!")
    count += 1
    print(f"Current Score: {count}/10")
else:
    print()
    print("Wrong Answer!")
    print(f"Current Score: {count}/10")

print()

# Question 4

q_4 = ("Which NFL team won the first Super Bowl?")
q_4_p_1 = (" A: New York Giants")
q_4_p_2 = (" B. New England Patriots")
q_4_p_3 = (" C. Oakland Raiders")
q_4_p_4 = (" D. Green Bay Packers")

print(q_4)
print(q_4_p_1)
print(q_4_p_2)
print(q_4_p_3)
print(q_4_p_4)
print()
answer_q_4 = ("Enter Your Answer: ")
print(answer_q_4)
print()

answer_q_4 = input()

if (answer_q_4.lower() == "D".lower()):
    print()
    print(f"Correct! Nice Work {name}!")
    count += 1
    print(f"Current Score: {count}/10")
else:
    print()
    print("Wrong Answer!")
    print(f"Current Score: {count}/10")

print()

# Question 5

q_5 = ("Which NFL team has lost at least four Super Bowls?")
q_5_p_1 = (" A: Pittsburg Steelers")
q_5_p_2 = (" B. Jacksonville Jaguars")
q_5_p_3 = (" C. Denver Broncos")
q_5_p_4 = (" D. LA Chargers")

print(q_5)
print(q_5_p_1)
print(q_5_p_2)
print(q_5_p_3)
print(q_5_p_4)
print()
answer_q_5 = ("Enter Your Answer: ")
print(answer_q_5)
print()

answer_q_5 = input()

if (answer_q_5.lower() == "C".lower()):
    print()
    print(f"Correct! Nice Work {name}!")
    count += 1
    print(f"Current Score: {count}/10")
else:
    print()
    print("Wrong Answer!")
    print(f"Current Score: {count}/10")

print()

# Question 6

q_6 = ("What is the mascott for the NFL team located in Minnesota?")
q_6_p_1 = (" A: Bear")
q_6_p_2 = (" B. Viking")
q_6_p_3 = (" C. Ram")
q_6_p_4 = (" D. Buccaneer")

print(q_6)
print(q_6_p_1)
print(q_6_p_2)
print(q_6_p_3)
print(q_6_p_4)
print()
answer_q_6 = ("Enter Your Answer: ")
print(answer_q_6)
print()

answer_q_6 = input()

if (answer_q_6.lower() == "B".lower()):
    print()
    print(f"Correct! Nice Work {name}!")
    count += 1
    print(f"Current Score: {count}/10")
else:
    print()
    print("Wrong Answer!")
    print(f"Current Score: {count}/10")

print()

# Question 7

q_7 = ("What two teams share the sames stadium?")
q_7_p_1 = (" A: Bears, Seahawks")
q_7_p_2 = (" B. Jets, Giants")
q_7_p_3 = (" C. Titans, Cardinals")
q_7_p_4 = (" D. Jaguars, Buccaneers")

print(q_7)
print(q_7_p_1)
print(q_7_p_2)
print(q_7_p_3)
print(q_7_p_4)
print()
answer_q_7 = ("Enter Your Answer: ")
print(answer_q_7)
print()

answer_q_7 = input()

if (answer_q_7.lower() == "B".lower()):
    print()
    print(f"Correct! Nice Work {name}!")
    count += 1
    print(f"Current Score: {count}/10")
else:
    print()
    print("Wrong Answer!")
    print(f"Current Score: {count}/10")

print()

# Question 8

q_8 = ("The 49ers are located in ________?")
q_8_p_1 = (" A: San Francisco, CA")
q_8_p_2 = (" B. Austin, TX")
q_8_p_3 = (" C. Las Vegas, NV")
q_8_p_4 = (" D. Seattle, Wa")

print(q_8)
print(q_8_p_1)
print(q_8_p_2)
print(q_8_p_3)
print(q_8_p_4)
print()
answer_q_8 = ("Enter Your Answer: ")
print(answer_q_8)
print()

answer_q_8 = input()

if (answer_q_8.lower() == "A".lower()):
    print()
    print(f"Correct! Nice Work {name}!")
    count += 1
    print(f"Current Score: {count}/10")
else:
    print()
    print("Wrong Answer!")
    print(f"Current Score: {count}/10")

print()

# Question 9

q_9 = ("What year did the NFL most recently move the goalposts from the goaline to the back of the endzone?")
q_9_p_1 = (" A: 1963")
q_9_p_2 = (" B. 2004")
q_9_p_3 = (" C. 1974")
q_9_p_4 = (" D. 1999")

print(q_9)
print(q_9_p_1)
print(q_9_p_2)
print(q_9_p_3)
print(q_9_p_4)
print()
answer_q_9 = ("Enter Your Answer: ")
print(answer_q_9)
print()

answer_q_9 = input()

if (answer_q_9.lower() == "C".lower()):
    print()
    print(f"Correct! Nice Work {name}!")
    count += 1
    print(f"Current Score: {count}/10")
else:
    print()
    print("Wrong Answer!")
    print(f"Current Score: {count}/10")

print()

# Question 10

q_10 = ("Which team is the only NFL team to complete a perfect season?")
q_10_p_1 = (" A: Miami Dolphins")
q_10_p_2 = (" B. Arizona Cardinals")
q_10_p_3 = (" C. Atlanta Falcons")
q_10_p_4 = (" D. New England Patriots")

print(q_10)
print(q_10_p_1)
print(q_10_p_2)
print(q_10_p_3)
print(q_10_p_4)
print()
answer_q_10 = ("Enter Your Answer: ")
print(answer_q_10)
print()

answer_q_10 = input()

if (answer_q_10.lower() == "A".lower()):
    print()
    print(f"Correct! Nice Work {name}!")
    count += 1
    print("--------------------------------------------------")
    print(f"Final Score: {count}/10")
else:
    print()
    print("Wrong Answer!")
    print("--------------------------------------------------")
    print()
    print(f"Final Score: {count}/10")


if count >= 7:
    print(f"Touchdown!!! Way to bring home the W {name}!")
else:
    count <= 6
    print(f"Sorry you lost {name}! To try again, re-run python code.")

print("Thank you for playing!")


print()
print("Game created by: Spencer Gray")
print("--------------------------------------------------")
