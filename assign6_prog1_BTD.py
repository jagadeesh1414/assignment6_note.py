binary=int(input("enter binary number"))
i, decimal, dec = 0 ,0 , 0
while(binary!=0):
    dec=binary%10
    decimal=decimal+dec*pow(2,i)
    binary=binary//10
    i=i+1
print(decimal)