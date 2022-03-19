#Question 1
size = 20
len = 4
print(('*' * size + '\n') * len)


#Question 2
size = 20
len = 4
space = 18
print(('*'*size + '\n') + ('*'+ (" " * space ) + '*' + '\n') + ('*'+ (" " * space ) + '*' + '\n') +('*'*size + '\n') )


#Question 3

print(('*\n') + ("*" * 2 + '\n' ) +('*'*3 + '\n')+('*'*4 + '\n'))

#Question 4

print( (512 - 282)/(47*48+5))

#Question 5
num = eval(input('Enter a number: '))
sqr = num * num
print ('The square of',num,'is',sqr,sep=" ")

#Question 6
n2 = eval(input("Enter a number: "))
print(n2,(n2*2),(n2*3),(n2*4),(n2*5),sep='---')

#Question 7
KG = eval(input("Please enter weight in Kg:"))
PND = KG * 2.2
print(PND)

#Question 8
p1 = eval(input("Please enter the first num:"))
p2 = eval(input("Please enter the second num:"))
p3 = eval(input("Please enter the third num:"))
total = p1 + p2 + p3
average = total/3
print('The total of the three numbers is',total, 'and the average of the three numbers is',average)

#Question 9
bamnt= eval(input("Please enter the bill amount:"))
tip = eval(input("Please enter the tip %:"))
ntip = tip/100
tipamnt = bamnt * ntip
tamnt= bamnt + tipamnt
print("The tip amount is",tipamnt, 'and the total bill is',tamnt)
