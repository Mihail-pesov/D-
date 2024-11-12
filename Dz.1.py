#1


# x = input("Enter a number: ")
# a = [x]*10
# for i in range(10):
#     print(a[i], end =", ")
 

#2

 
# from random import randint
 
# a = [randint(1, 100) for x in range(10)]
 
# for i in range(10):
#     print(a[i], end = ", ")


#3
 

# x = input("Enter a number: ")
# z = int(x)
# a = [i for i in range(z,z+10)]
# for i in range(10):
#     print(a[i], end = ", ")


#4


# b = [10,9,8,7,6,5,4,3,2,1]

# for i in range(10):
#     print(b[i], end = ", ")


#5


# a = int(input("Enter the first number: "))
# b=0
# c = [0]
# for i in range(1, 11):
#   c.append(a**i)

# print(c) 

#6

a = [0]
for i in range(10):
    a.append(2**i)
    b = a[::-1]
print(b)