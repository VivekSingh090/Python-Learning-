num =  int(input("Enter your Number:"))
if num <= 1 :
 print(f"{num}The given number is not Prime number")
else:
 for i in range (2,num):
     if num % 2 == 0 :
         print(f"{num} is not a Prime Number:")
         break
 else:
        print(f"{num} is a Prime Number:")
    
