num = int(input("Enter Input : "))
for i in range(num+1):
	print("."*(num-i+1),end="")
	print("#"*(i+1),end="")
	if(i==0):
		print("+"*(num+2),end="")
	else:
		print("+",end="")
		print("#"*num,end="")
		print("+",end="")
	print()
for i in range(2):
	print("#"*(num+2),end="")
	print("+"*(num+2),end="")
	print()
for i in range(num):
	print("#",end="")
	print("+"*num,end="")
	print("#",end="")
	print("+"*(num+1-i),end="")
	print("."*(i+1),end="")
	print()
print("#"*(num+2),end="")
print("+",end="")
print("."*(num+1))


