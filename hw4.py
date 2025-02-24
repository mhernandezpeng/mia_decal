#Homework 4

#2 Practice slicing and striding

#2.1 Making a list variable
numbersList = []

i = 1
while i < 21:
    numbersList.append(i)
    i+=1

print(numbersList[0::])

#2.2 


def squareList(nums):
    for i in range(len(nums)):
        nums[i] = pow(nums[i], 2)
    return nums

print(squareList(numbersList))

#2.3

def first_fifteen_elements(nums):
    return nums[:15]

print(first_fifteen_elements(numbersList))

#2.4 

def every_fifth_element(nums):
    return nums[::5]

print(every_fifth_element(numbersList))

#2.5 

def fancy_function(nums):
    nums = nums[:len(nums)-3]
    return nums[::-3]

print(fancy_function(numbersList))

#3.1

def create_2d_list():
    matrix = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num+=1
        matrix.append(row)
    return matrix

print(create_2d_list())

#3.2 

matrix = create_2d_list()

def modify_2d_list(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] % 3 == 0:
                list[i][j] = "?"
    
    return list

print(modify_2d_list(matrix))

#3.3

modified_matrix = modify_2d_list(matrix)

def sum_non_question_elements(list2):
    sum = 0
    for i in range(len(list2)):
        for j in range(len(list2[i])):
            if list2[i][j] != "?":
                sum += list2[i][j]
    
    return sum

print(sum_non_question_elements(modified_matrix))