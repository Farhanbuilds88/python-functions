def even_odd_checker(number):
    if number%2==0:
        return "even"
    else:
        return "odd"
result=even_odd_checker(int(input("enter a number:")))
print("the number is ",result)
#factorial
n=5
fac=1
for i in range(1,n+1):
    fac*=i

print(fac)

def cal_fac(anynumber):
    factorial = 1
    for j in range(1, anynumber+1):
        factorial *= j
    return factorial

print("The factorial of the number is:", cal_fac(4))
