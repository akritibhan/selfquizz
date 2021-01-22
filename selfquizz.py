print("----------HEY ! WELCOME TO THIS GAME.... YOU HAVE TO ANSWER BASIC QUESTIONS ABOUT ME ")
print('''Let's see 
how well 
do you know me! ....ready \?''') 
oo = input("Write yes to start \n ")
print("\n")

print("OKAY! LETS START")
score=0
choice="y"

print("What is my fav colour? \n")

print('''Your options are :
1. Red
2. Black
3. Purple
''')
print("\n")
choice = input("Enter ur choice :\n")
if choice=='1':
    print("Kuddos! you  are correct")
    score += 10
    print(f"Your score till now  is: {score}")
else:
    print("------- You are wrong------")
    score+= 0
    print(f"Your score till now  is: {score}")
    print("\n")

print("What is my fav fast food ? \n")
print("\n")
print('''Your options are:
1. Chilli Potato
2. Momos
3. Spring Rolls''')
print("\n")
choice2 = input("Enter ur choice :")
if choice2=='2':
    print("You are correct!")
    score+=10
    print(f"Your score till now  is: {score}")
else:
    print("------ You are wrong-----")
    score+=0

    print(f"Your score for this round is : {score}")

print("What would I choose ? \n")
print('''Your options are:
1. Coffee
2. Tea
3. Juice''')
choice3 = input("Enter ur choice :")
if choice3=='2':
    print(" You are correct! hurray!!!!!!!!!")
    score+=10
    print(f"Your score till now is: {score}")
else:
    print("OOPS! You are wrong ")
    score+=0
    print(f"Your score till now is {score}")
    print("\n")
print("Which programming language do I learn right now ? \n")
print('''Your options are:
1. c++
2. java
3. c
4. python''')
print("\n")
choice4=input("Enter ur choice : ")
if choice4=='4':
    print(" You are correct!!!YAYY!!!")
    score+=10
else:
    print("-----You are wrong-----")
    score+=0
    print(f"Your score till now is: {score}")
    print("\n")
print("Where am I from ? \n")
print('''

''')
print('''Your options are :
1. j and k 
2. Uttar pradesh 
3. Delhi''')
choice5 = input ("Enter ur choice")
if choice5 =='1':
    print("You are correct!!!!!!")
    score+=10
    print(f"Your score till now is: {score}")
else:
    print("------You are  wrong -----")
    score+=0
    print(f"Your till now is : {score}")
print('''

''')

print("What is my birth date ? \n")
print('''

''')
print('''Your options are:
1. 22 dec
2. 18 dec
3. 13 dec''')
choice6 = input("Enter ur choice: ")
if choice6== '2':
    print("You are  correct!!!!!!!!!!!!!!!")
    score+= 10
    print(f"Your score till now  is: {score}")
else:
    print("------ You are wrong------")
    score+=0
    print(f"Your score till now is: {score} ")
if score>=50 :
    print(f"CONGRATSS!!!! YOU KNOW ME WELL .. YOUR FINAL SCORE IS: {score}")
     
else :
    print(f"OOPS !!! BETTER LUCK NEXT TIME --- YOUR FINAL SCORE I: {score}")


print("THANKS FOR PLAYING--------")
