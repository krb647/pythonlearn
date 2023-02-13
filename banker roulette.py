import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
last_name=len(names)
person=random.randint(0,last_name-1)
person=names[person]
print(f"{person} is going to buy the meal today!")
