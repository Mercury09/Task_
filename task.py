
# №1------------------------------------------------------------------------------
# a = input("How many puple: ")
# b = input("How many apple: ")

# a = int(a)
# b = int(b)

# w = b / a
# q = b % a

# print(int(w),int(q))



# №2------------------------------------------------------------------------------

# count = 0
# a = input("How many puples of class 'A': ")
# a = int(a)
# if a % 2 != 0:
# 	count = a/2 + 0.5
# else:
# 	count = a/2
# b = input("How many puples of class 'B': ")
# b = int(b)
# if b % 2 != 0:
# 	count = count + b/2 + 0.5
# else:
# 	count = count + b/2
# c = input("How many puples of class 'C': ")
# c = int(c)
# if c % 2 != 0:
# 	count = count + c/2 + 0.5
# else:
# 	count = count + c/2

# count = int(count)
# print(count)




# №3------------------------------------------------------------------------------

# a = [0, 0, 0]
# count = 1
# for i in range(0,len(a)):
# 	a[i] = input("Write number: ")

# if a[0] == a[1] and a[0] == a[2] and a[0] == a[2]:
# 	count = 3
# elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
# 	count = 2
# else:
# 	count = 0
# print(a)
# print(count)



# №4------------------------------------------------------------------------------

# array = []
# count = 0
# a = input("Could you please specify number of 'N': ")
# a = int(a)

# for i in range(0,a):
# 	t = input(f"Please write a {i+1} number: ")
# 	t = int(t)
# 	array.append(t)
# 	if t == 0:
# 		count += 1

# print(array)
# print(f"Number of 0 in array is {count}")




# №5------------------------------------------------------------------------------

# i = 0 

# while i < 100:
# 	with open("Hello.txt", "a") as f:
# 		f.write("I AM PROGRAMMER!!!\n")
# 		i += 1




# №6------------------------------------------------------------------------------

# text = ""
# with open("Hello.txt", "r") as findMars:
# 	text = findMars.read()
# 	text = text.split()
# 	print(text)
# 	for i in range(0,len(text)):
# 		if text[i] == "ElonMars":
# 			print("Correct " + text[i])		
# 	for i in range(0,len(text)):
# 		if text[i] != "ElonMars": 
# 			if text[i].upper() == "ELONMARS":
# 				print("Clone " + text[i])	
		
