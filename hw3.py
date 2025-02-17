#Python DeCal Homework #3
#1. Oski stole your power

def computePower(x,y):
    count = 1
    while(count<y):
        x+=x
        count+=1
    return str(x)

print(computePower(2,3))

#2. What should I wear?
readings = [15,14,17,20,23,28,20]

def temperatureRange(temps):
    minValue = min(temps)
    maxValue = max(temps)
    range = (minValue,maxValue)
    return range

print(temperatureRange(readings))

#3. Check if it's the weekend
day = 6 # Saturday

def isWeekend(today):
    if today == 6:
        return True
    if today == 7:
        return True
    else:
        return False
    
print(isWeekend(day))

#4 Fuel efficiency calculator
distance = 70 #miles
fuel = 21.5 # gallons
def fuel_efficiency(miles, gallons):
    return round(miles/gallons, 2)

print(fuel_efficiency(distance, fuel))

#5 Secret Code
n = 12345

def decodeNumbers(num):
    last_digit = num%10
    remaining_part = int((num - last_digit)/10)
    
    print(last_digit, end="")
    print(remaining_part)

decodeNumbers(n)

#6 Min & Max but with loops
#6.1 For loops
nums = [2024, 98, 131, 2, 3, 72]
def find_min_with_for_loops(numList):
    smallestNum = numList[0]
    for num in numList:
        if num < smallestNum:
            smallestNum = num

    return smallestNum

print(find_min_with_for_loops(nums))

def find_max_with_for_loops(numList):
    largestNum = numList[0]
    for num in numList:
        if num > largestNum:
            largestNum = num
        
    return largestNum

print(find_max_with_for_loops(nums))

#6.2 While Loops

def find_min_with_while_loops(numList):
    i = 0
    smallestNum = numList[0]
    while i < len(numList) - 1:
        if numList[i] < smallestNum:
            smallestNum = numList[i]
        i+=1
    return smallestNum

print(find_min_with_while_loops(nums))

def find_max_with_while_loops(numList):
    i = 0
    largestNum = numList[0]
    while i < len(numList) - 1:
        if numList[i] > largestNum:
            largestNum = numList[i]
        i+=1
    return largestNum

print(find_max_with_while_loops(nums))

#7 Counting vowels
text = "UC Berkeley, founded in 1868!"

def vowel_and_consonant_count(string):
    vowel_count = 0
    consonant_count = 0
    for i in range(len(string)):
        if string[i].isalpha() == True:
            if string[i].lower() in 'aeiou':
                vowel_count+=1
            else:
                consonant_count+=1
    
    return(vowel_count, consonant_count)

print(vowel_and_consonant_count(text))

#8 Calculate digital root
number = 2468

def digital_root(integer):

    str_int = str(integer)

    return int(str_int[0]) + int(str_int[1]) + int(str_int[2]) + int(str_int[3])

print(digital_root(number))