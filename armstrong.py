# armstrong of a number with function
def arm(digit):
    n = num
    leng = len(str(num))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** leng
        n //= 10

    if total == num:  
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")
        
num = int(input("Enter a number: ")) 
print(arm(num))  

