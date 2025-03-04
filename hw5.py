#Homework 5

#1. pwd
#2. ls
#3. cd brianna_repo, git pull origin main
#4. mv homework.py homework
#5. cat homework.py
#6. nano homework.py
#7. git add homework.py, git commit -m "adding homework.py", git push origin main
#8. do git pull origin main first, then the 3 commands in question 7
#9. cd ~/Recents

#2.1 
var = 'words'

def checkDataType(input):
    return type(input)

print(checkDataType(var))
print(checkDataType(3.14))
print(checkDataType(26))

#2.2 

def evenOrOdd(num):
    if num % 2 == 0:
        return "even"
    else: 
        return "odd"

print(evenOrOdd(10))
print(evenOrOdd(9))

#3
numbers = [1, 2, 3, 4, 5]

def sumWithLoop(list):
    sum = 0
    for i in range(len(list)): 
        sum+= list[i]
    return sum

print(sumWithLoop(numbers))

#4.1

def duplicateList(list):
    newList = []
    for i in range(len(list)):
        newList.append(list[i])
        newList.append(list[i])
    
    return newList

print(duplicateList(['a', 'b', 'c']))

#4.2 - Missing a semicolon, should be:
def square(num):
    return num*num

print(square(3)) #returns 9




