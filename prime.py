n=int(input("Enter the no. "))
s=0
for i in range (1,n+1):
    if n%i==0:
        s=s+1
if s==2:
    print("No. is Prime")
else :
    print("No. is Not prime")
