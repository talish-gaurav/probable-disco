n = int(input("Enter your number here"))
s = n
sum = 0
length = len(str(n))
while n > 0:
    digit=n%10
    sum = sum + digit**length
    n=n//10

if sum == s:
    print("Number is armstrong")

else:

    print("Number is not armstrong")