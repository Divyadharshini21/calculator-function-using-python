#Program for simple calculator

#fun for adding
def add(x,y):
    return x+y
#fun for subraction
def subract(x,y):
    return x-y
#fun for multiply
def multiply(x,y):
    return x*y
#fun for division
def divide(x,y):
    return x/y

#Getting input from the users

print('Select the operation')
print('1.Addition')
print('2.subraction')
print('3.multiply')
print('4.divide')

while True:
    # taking input

    choice =input('Eneter the choice(1/2/3/4): ')
    #input from user
    if choice in('1','2','3','4'):
        num1=float(input('Enter the number: '))
        num2=float(input('Eneter the number: '))

        if choice=='1':
         print(num1,'+',num2,'=',add(num1,num2))
        elif choice=='2':
         print(num1,'_',num2,'=',subract(num1,num2))
        elif choice=='3':
         print(num1,'X',num2,'=',multiply(num1,num2))
        elif choice=='4':
         print(num1,'/',num2,'=',round(divide(num1,num2,),2))
         break
    else:
     print('Enter a valid input')
# End of the program(done by Divyadharshini N)
