n=int(input("Enter the row size of the pattern  "))
ch=65
for i in range(1,n+1) :
     for j in range(1,i+1) : 
        print(chr(ch),end=" ")
        ch+=1
     print()
