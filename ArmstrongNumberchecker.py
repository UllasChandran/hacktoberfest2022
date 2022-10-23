number =  int(input("Enter the Number to be checked:::"))
originalnum = number
result = 0
count = 0
while(number!=0):
    number = number//10
    count+= 1
number = originalnum
while(number!=0):
    rem = number%10
    number = number // 10
    result = result + rem**count

if (originalnum == result) :
    print("Entered Number ",originalnum,"is an ARMSTRONG NUMBER")
else :
    print("Entered Number  ",originalnum,"  is NOT an ARMSTRONG NUMBER")
    

    
