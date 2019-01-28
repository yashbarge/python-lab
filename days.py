#WRITE A PYTHON PROGRAM TO CONVERT SECONDS INTO DAYS HOURS MINUTES AND SECONDS?
x=int(input('enter seconds'))
q1=x//86400
r1=x%86400
h=r1//3600
d=h%3600
e=d//60
f=d%60
g=f
print('the given seconds',x,'are converted into',q1,'days',h,'hours',e,'minutes',g,'seconds')









