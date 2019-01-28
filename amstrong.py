#write a python program to find user entered number is amstrong number
x=int(input('enter number'))
y=x//100
b=x%100
c=b//10
d=b%10
e=y**3+c**3+d**3
if x==e:		
	print('amstrong number')
else:
	print('not amstrong number')

