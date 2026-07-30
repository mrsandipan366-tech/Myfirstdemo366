# 1_______pip and module

# import pyjokes

# j=pyjokes.get_joke()
# print(j)


# a=input("enter a number")
# b=type(a)
# c=int(a)
# print(b,c)



#a="i have never been to this city. but i hope i will visit one day"
# b=a[0:7]
# print(b)

# c=len(a)
# print(c)


# 2______LIST AND TUPLES

# list=[7,10,50,"hello," 6.75]
# print(list)
# print(list.reverse())
# print(list.sort())

#    input 8 fruit name and print their name 
# fruits=[]
# for i in range(1,8):
#     fruit=input(f"enter a name of fruit{i}: ")
#     fruits.append(fruit)
# print("\nthe list of the fruit name is ")
# print(fruits)



#        sum of list with 4 numbers

# list=[2,45,3,12]
# sum=0
# for i in range(0,4):
#    sum=sum+list[i]

# print(sum)



#            count the zero is the list

# list=[1,2,0,0,5,0,4,0]
# count=0
# for i in range(0,len(list)):
#     if (list[i]==0):
#         count=count+1
#     else:
#         pass

# print(count)


# 3_______dictionary and set

# dic={
#     "sandy":100,
#     "rohit":99,
#     "list":[1,5,9],
#     100:60
# }

# print(dic["list"])


#     find given name has 10 alphabet or not


# name=input("enter ur name")
# a=len(name)
# if(a<10):
#     print("yes it contain less then 10")
# elif(a==10):
#     print("no is alphabet is 10")
# else:
#     print("its contain more then 10 ")



#          find the grade of a student 


# mark=input("enter a number")
# marks=int(mark)

# if(marks>90 and marks<100):
#    print("O")
# elif(marks>80 and marks<90):
#    print("E")
# elif(marks>70 and marks<80):
#    print("A")
# else:
#    print("Fail")


# 4______ for and while loops


# list=[1,2,4,5,5,67,6,8]
# for i in range(0, len(list)):
#     print(list[i])

# i=0
# while(i<=10):
#     print(f"this is a no of {i}")
#     i=i+1 

# find sum of the natural n digit no

# a=input("enter first nth no")
# n=int(a)
# sum=0
# for i in range (1,n):
#     sum=sum+i

# print(sum)

# print the pattern
# a=input("enter ur no")
# n=int(a)
# i=0
# while(i<n):
#     j=0
#     while(j<n):
#         print("*")
#         j=j+1
#     print("\n")
#     i=i+1 


# 5_______ function and recursion

#           inches into cms

# a=input("enter inches")
# m=int(a)
# def convert(n):
#     cm=n*2.54
#     return cm
# n=convert(m)
# print(n)

#           recursion of factorial

# a=input("enter no of factor")
# n=int(a)
# def recursion(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*recursion(n-1)
    
# yoyo=recursion(n)
# print(yoyo)



#6___________ file
#read a file

# f=open("first.txt", "r")
# t=f.read()
# print(t)
# f.close()

#write a file

# f=open("first.txt", "w")
# f.write("hello guys")
# f.close()

# with open ("first.txt") as f:
#     f.read()


# 7____________ OOPS

#class and objects

# class employees:
#     company="toys" 
#     salary=100  #class attributes
#     @staticmethod
#     def printh():  #self function
#         print("hello sir")

# harry=employees()
# print(harry.company)
# rahul=employees()
# rahul.printh()
# rahul.salary=200  #instance attributes
# print(rahul.company, rahul.salary)


# class ctrl:
#     food="non veg"
#     time=12.00
#     def __init__(self, time):    #constructor
#         self.time=time
#         print("100*200=500")
   
# sim=ctrl(2.00)
# print(sim.food, sim.time)



# find squre, cube, sqroot

# class calculator:
#     def __init__(self, n):
#        self.n=n

#     def squre(self):
#        print(f"squre is {self.n*self.n}")

# sq = calculator(4)
# sq.squre()  
# same like other 2  



#           inheritance

# class coder:
#     code="python"
#     def run(self):
#         print("enter ur skill in python")

# class programmer:
#     code="java"
#     def run2(self):
#         print("enter ur skill in java")

# class employee(coder, programmer):
#       code="c++"
#       def run3(self):
#           print("its ur time baby")

# a=employee()
# print(a.run())

#                 super() method
# class java:
#     def __init__(self):
#         print(1)
# class python(java):
#     def __init__(self):
#             super().__init__()
#             print(2)
# class c(python):
#      def __init__(self):
#              super().__init__()
#              print(3)

# a=c()

# class demo:
#     def __init__(self,n):
#         self.n=n
#     def sim(self):
#         print(f"two is a {self.n}")
# a=demo(5)
# a.sim()

#         classmethod
# class jio:
#     a=5
#     @classmethod
#     def show(self):
#         print(f"the class is {self.a}")
# e=jio()
# e.a=45
# e.show()

#       operator_overlaoding

# class dommme:
#     def __init__(self,n):
#         self.n=n
#     def __add__(self, num):
#         return self.n+num.n
# a=dommme(1)
# b=dommme(2)
# print(a+b)
 

# class twoDvector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j

# class threeDvector:
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k

# o=twoDvector(1,2)
# m=threeDvector(1,2,3)




# 44444444444444444444444444444444

# class complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i
#     def __add__(self,c2):
#         return complex(self.r+c2.r, self.i+c2.i)
#     def __str__(self):
#         return f"{self.r}+{self.i}i"

# c1=complex(1,2)
# c2=complex(3,4)
# print(c1+c2)



#  enumerate function

# l=[2,3,4,5,6,7,10]
# for index,i in enumerate(l):
#     print(f"{index} {i}")



#########list compihention 











# ADVANCE PROBLEM IN PYTHON


# def https(status):
#     match status:
#         case 200:
#             return "ok"
#         case 300:
#             return "lol"
#         case 600:
#             return "teri keya hoga"
# print(https(300))

##############

# dict={"a":2, "b":6}
# dict2={"f":3, "c":7}
# marged=dict|dict2
# print(marged)













































































































































































































































































    














