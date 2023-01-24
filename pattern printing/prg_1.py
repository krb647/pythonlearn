#pattern printing:

# * * *
# * * *
# * * *  

row=int(input("enter the number of rows: "))
column=int(input("enter the number of column: "))
for i in range(0,row):
  for j in range(0,column):
    print("*",end=" ")
  print()
print("\n")
