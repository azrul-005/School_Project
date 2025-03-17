'''
import random 
a=random.randint(1,10)
num=int(input("enter a number"))
if (num==a):
    print('your guess is correct')
elif(num<a):
    print('your guess is low')
else:
    print('your guess is high')
'''
import random
a=random.randint(1,15)
steps=0
ll=0
hl=15
def check():
    global steps,ll,hl
    num=int(input(f'enter a number from {ll}-{hl}: '))
    
    if(num==a):
        print('your guess is correct')
        print(f"you guessed correct in {steps} steps")
        quit()
    elif(num<a):
        print('your guess is low')
        steps+=1
        ll=num
        check()
        

    else:
        print('your guess is high')
        steps+=1
        hl=num
        check()

check()