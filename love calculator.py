# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name1.lower()
name2=name2.lower()
T=(name1+name2).count("t")
R=(name1+name2).count("r")
U=(name1+name2).count("u")
E=(name1+name2).count("e")
TRUE=T+R+U+E
L=(name1+name2).count("l")
O=(name1+name2).count("o")
V=(name1+name2).count("v")
E=(name1+name2).count("e")
LOVE=L+O+V+E
love_score=str(TRUE)+str(LOVE)
love_score=int(love_score)
if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score>=40 and love_score<=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
