n=int(input("Enter the row size  "))
for i in range (1,n+1):
     for j in range(n-i+1,1,-1):
           print(" ",end=" ")
     for k in range(1,i+1):
           print("*",end=" ")
     print()
