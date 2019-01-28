d={}
x=int(input('ENTER NUMBER OF STUDENTS'))
for i in range (x):
	print('ENTER INFO OF',i+1)
	n=input('enter name')
	g=int(input('gr.no'))
	b=input('enter branch')
	d[g]=(n,b)
print(d)
