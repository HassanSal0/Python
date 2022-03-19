#Question 1
item = int(input("How many items did you buy?: "))

if item<10:
   cost = item * 12
   print ("The total cost of your items is",cost)
elif item>=10 and item<100 :
    print ("The total cost of your items is",cost)
   cost = item * 10
   print ("The total cost of your items is",cost)
else:
    cost = item * 7


#Question 2

for c in range(200):
    if c %5 ==2:
        if c %6 ==3:
            if c %7 == 2:
                print('There are', c, 'in the Halloween Jar')

#Question 3
Semail = 0
Premail = 0
email = int(input("Please enter the number of emails you want to evaluate: "))

for e in range(email):
    num = input("Please enter your email: ")
    if num[-20:] == '@student.college.edu' :
        Semail = Semail + 1
    elif num[-17:] == '@prof.college.edu' :
        Premail = Premail + 1
    else:
        print('Invalid email, This shall not be counted')
print('There are', Semail, 'student emails and', Premail, 'professor emails.')


#Question 4
num = input("Please enter the number to derive its derivative in the following pattern (Ax^y): ")
power = num.split('^')
integer = num.split('x')

if integer[0] =='':
    newpower = int(power[1]) - 1
    print(power[1],power[0],'^',newpower,sep='')
else:
    newinteger = int(power[1]) * int(integer[0])
    newpower = int(power[1]) - 1
    print(newinteger,power[0],'^',newpower,sep='')

#Question 5
#Simulating the dice roll
from random import randint
rolls = 10000
roll_list =[]

for dice in range(rolls):
    first_roll = randint(1,6)
    second_roll = randint(1,6)
    total_score = first_roll + second_roll
    roll_list.append(total_score)

#Calculating % of each value
c2 = (roll_list.count(2)/rolls) * 100
c3 = (roll_list.count(3)/rolls) * 100
c4 = (roll_list.count(4)/rolls) * 100
c5 = (roll_list.count(5)/rolls) * 100
c6 = (roll_list.count(6)/rolls) * 100
c7 = (roll_list.count(7)/rolls) * 100
c8 = (roll_list.count(8)/rolls) * 100
c9 = (roll_list.count(9)/rolls) * 100
c10 = (roll_list.count(10)/rolls) * 100
c11 = (roll_list.count(11)/rolls) * 100
c12 = (roll_list.count(12)/rolls) * 100

#Creating the list of % of each value rounded off to 2 decimals
num_chance = [c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]
num_chance = [round(num,2) for num in num_chance]

#Running a sentence loop
initial = 2
x=0
for c in num_chance:
    print('The percentage of getting a',initial,'is:',num_chance[x],'%',sep=' ',end='.')
    print('\n')
    initial = initial + 1
    x = x + 1

#Question 6
#Getting sentence input from user
sen = str(input("Please input your sentence: "))
sen = sen.strip()

#Counting the words
sp_count = sen.count(' ')
sp_count = sp_count + 1

#Printing the result
print('There are',sp_count,'words in the sentence:',sen)

#Question 7
#Getting sentence input from user
word = str(input('Please input a word: '))
word = word.strip().lower()
vowel = ['a','e','i','o','u']

initialvowel = 0

for letters in word:
    if letters in vowel :
        initialvowel += 1

print('There are',initialvowel, 'vowel(s) in this word')

#Question 8
s = str(input('Please input a sentence: '))
s = s.strip().replace('.', '').replace(',','').lower()
print(s)

## QUESTION: 9
#The Question asks for splitting of a word with only 1 a. This code can execute that, however, what if the word had multiple A's? The code is valid for such a situation too.
#Initial input and variable setup
s = str(input('Enter a word: '))
s = s.strip().lower()
b=0
#if statement to check if one word is input or multiple words are input
if s.count(' ')>0:
    print('Please enter one word only')
else:
    if s.count('a') == 1:
        word = s.split('a')
        lastword = word[-1]
        print(str(word[0]) + 'a')
        print(lastword)
    elif s.count('a') == 0:
        print('This word has no As')
#The code stops if there are no As
    else:
        word = s.split('a')
        for a in word:
            while b<3:
                print(str(word[b]) + 'a' )
                b = b + 1
        lastword = word[-1]
        print(lastword)

#The code can be modified to check on existence of any character and not just 'a'


s = str(input('Please input a word: '))
q = str(input('Please input a character: '))

s= s.strip()
q = q.strip()
c = s.count(q)

#(a)
if s.count(q)>0 :
    print('This word contains the chosen character')
elif s.count(q) == 0:
    print('This word contains no letters of the chosen character')

#(b)
num = s.split(q)
count = len(num) - 1
if count>=1:
    print('There are', count, 'letter(s) of the chosen character')

#(c)
