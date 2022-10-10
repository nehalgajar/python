# 1. Provide a program for the calculator from terminal.
# • Make sure it do not ask questions but when you press enter. it displays the result. 
# • Amount and formula has to be in one line. 
# e.g 456 - 12 
#  564/ 10 
#  456*1234+09-12

class Abc:
	def addition(self,a,b):
		sum = a + b #for addition 
		print('Addition',sum)

	def substraction(self,a,b):
		sub = a - b #for substraction
		print('Substraction',sub)

	def multipication(self,a,b):
		mul = a * b #for multipication
		print('Multipication',mul)

	def divsion(self,a,b):
		div = a / b #for divsion
		print('Divsion',div)

	def multipalcalculations(self,a,b,c,d):
		all = a * b + c - d #for multipalcalculations
		print('Multipal calculations',all)

number = int(input("Enter a number="))
number1 = int(input("Enter a number agian="))
number2 = int(input("Enter a number agian="))
number3 = int(input("Enter a number agian="))

print('------------------------------------------')
print('enter 1 for Addition')
print('enter 2 for Substraction')
print('enter 3 for Multipication')
print('enter 4 for Divsion')
print('enter 5 for Multicalculations')

choice = int(input('Enter your choice :'))
obj =Abc()

if choice == 1:
 	obj.addition(number,number1)
elif choice ==2:
 	obj.substraction(number,number1)
elif choice ==3:
 	 obj.multipication(number,number1)
elif choice ==4:
    obj.divsion(number,number1) 
elif choice ==5:
	obj.multipalcalculations(number,number1,number2,number3) 
else:
	print('Invalid chioce.......try agian')	    