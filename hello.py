# name="mayank"
# for a in name:
#     print(a)
#     if(a=="n"):
#         print("something special")
# colors = ["Red","Green","Blue","Pink"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(color)
#         # if(i=="e"):
#         #     print("something new"
# for k in range(1,20,2):
#     print(k)
# i=int(input("enter the number:"))
# while(i<=38):
#     i=int(input("enter the number:"))
#     print(i)
    
# print("done with the loop")
# for i in range(12):
#     if(i==10):
#         break
#     print("12 X", i+1,"=",12*(i+1))
# 
# def calculategmean(a,b):
#     mean=(a*b)/(a+b)
#     print(mean)
# def isgreater(a,b):
#   if(a>b):
#     print("first number is greater")
#   else:
#     print("second number is greater")
# def islesser(a,b):
#     if(a<b):
#         print("first no is lesser")
#     else:
#         print("second no is lesser")
    
# a=7
# b=6 
# isgreater(a,b)
# islesser(a,b)

# calculategmean(a,b)
# c=9
# d=10
# isgreater(c,d)
# islesser(c,d)
# calculategmean(c,d)

# def average(a,b,c):
#     print("the average is ",(a+b+c)/2)
# def sum(a,b,c):
#     print("the sum of no is",(a+b+c))
# def mult(a,b,c):
#     print("the multiplication of no is",(a*b*c))


# average(3,54,999)
# sum(33,44,999)
# sum(99,00,000)
# average(77,99,999)
# mult(33,77,999)
# l=[33,44,55,66,77,"mayank"]
# x="mayank"
# print(x)
# print(l[:])
# print(type(x))

# l.append(4)

# print(l)

# print(type(l))
# print(l[0],l[3],l[5])
# if "mayank" in l:
#     print("yes")
# else:
#     print("no")
# if "yank" in "mayank":
#     print("yes")
# else:
#     print("no")
# lst=[i*i for i in range(10) if i%3==0]
# print(lst)
# l.append(4)
# l=[9,3,2,4,203,90,22]
# print(l)
# l.append(88)
# print(l)
# l.sort(reverse=True)
# print(l)
# print(l.index(4))
# print(l)
# print(l.count(9))
# print(l)
# l.insert(0,999)
# print(l)
# m=[444,555,666]
# l.extend(m)
# print(l)
# tup=(33,22,5,3,34,88,66)
# print(type(tup))
# print(len(tup))
# if 33 in tup:
#     print("yes")
# else:
#     print("no")
# tup2=[2,3,4]
# print(type(tup2))
# name=("mayank","vanshu","lavi","sanjay")
# temp=list(name)
# temp.append("girija")
# name=tuple(temp) 
# print(name)
# countries=("india","usa","china","spain")
# x=list(countries)
# x.append("russia")

# x.pop(3)
# x[2]="srilanka"
# countries=tuple(x)
# print(countries)
# marks1=(11,22,33,44)
# marks2=(77,88,99,66)
# marks=marks1 + marks2
# print(marks)

# tuple1 =(0,1,2,3,4,5,,3,4,1,4,5)
# res=tuple1.count(3)
# print(res)
# import time
# t=time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
# hour=int(input("enter the time"))
# print(hour)

# if(hour>=0 & hour<12):
#     print("good morning")
# elif(hour>=12 & hour<17):
#         print("good afternoon")
# if(hour>=17 & hour<0):
#     print("good night")

# questions=["what is the capital of india?","delhi","up","assam","punjab",0],
# ["what is the color of sun?","yellow","black","pink","blue",0],
# ["what is the capital of bihar?","delhi","patna","goa","mumbai",1]
# levels=[1000,2000,50000,10000,20000,50000,100000,500000]
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(300))
# print(factorial(6))
# def fibonacci(n):
#     if(n==0 or n==1):
#         return n

#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(0))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5)) 
# harry={"mayank",4,5,6,7,7,8}
# print(type(harry))

# for value in harry:
#     print(value)
# s1={22,33,4,22,33,44,4}
# s2={9,8,00,7,2,3}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.issubset(s2))
# s1.update(s2)
# print(s1.symmetric_difference(s2))
# print(s1.isdisjoint(s2))
# s1.add(99)
# print(s1)
# s1.clear()
# print(s1)
# dic={ 
#     344:"mayank",
#     366:"vanshu",
#     666:"lavi",
#     555:"hhhh "
   

# }
# print(dic[666])
# info={'name':'mayank','age':20,'eligible':True}
# print(info)
# print(info["name"])
# print(info['eligible'])
# print(info.keys())
# print(info.values())
# for key in info.keys():
#     print(info[key])  
# ep1={122:45,333:99,999:22,777:55}
# ep2={888:33,666:11}
# ep1.popitem()
# del ep1[122]
# print(ep1)
# i=0
# while(i<9):
#     print(i)
#     i=i+1
# else:
#     print("sorry")-

# a=int(input("enter the number"))
# print("multiplication table of {a}")
# try:
#   for i in range(1,11):
#     print(f"{a} X {i}={a*i}")
# except:
#     print("sorry")
# print("end of progarm")

# try:
#     num=int(input('enter the number'))
# except ValueError:
#     print("number is not integer")

# def func1():

#  try:
#     l=[1,2,5,7]
#     i=int(input("enter the index"))
#     print(l[i])
#     return 1
#  except:
#     print("some error occurred")
#     return 0
#  finally:
#     print("I am always executed")
    
# x=func1()
# print(x)

# from logging import raiseExceptions


# a=int(input("enter any value between 5 and 9"))
# if(a==quit):
#     print("true")
# else:
#     raiseExceptions("invalid word")
# a=4444
# b=999
# print('A') if a>b else print("=") if a==b else print('B')

# c=9 if a>b else 0
# print(c)
# result=print(True) if a>b else print(False)


# marks=[22,11,77,99,55,44]
# for index,mark in enumerate(marks):
#     print(index,mark)
#     if(index==3):
#         print("awesome mayank")
# from math import sqrt as s,pi as p
# # from unittest import result

# result= s(16)*p

# print(result)
# import math
# from unittest import result
# print(dir(math))
# from math import log as l
# result=l(10)
# print(result)
# empt={}
# print(empt)
# x=10
# def my_function():
#  global x
#     x=4
#     y=5
    
#     print(y)

# my_function( )
# print(x)
 
# f= open('myfile.txt','w')
# # # print(f)
# text = f.read()
# print(text)
# f.close()
# f=open('myfile.txt','w')
# f.write('hello world')
# f.close()

# f=open('myfile.txt','r')
# i=0
# while True:
#     i= i+1
#     line=f.readline()
#     if not line:
#         break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
# print("marks of student i in maths is:{m1}")
#     print("marks of student i in sci is:{m2}")
#     print("marks of student i in sst is:{m3}")
#     print(line)
# with open("myfile.txt",'w') as f:
#     f.write('hello world')
#     f.truncate(4)


# with open("myfile.txt",'r') as f:
#     print(f.read())


# double = lambda x:x*5
# cube = lambda x:x*x*x
# avg= lambda x:(x+x+x)/3
# print(double(5))
# print(cube(5)) 
# print(avg(15))


# def cube(x):
#      return x*x*x

# print(cube(3))

# l=[1,2,3,4,5,6,7,89,9]
# mayank=list(map(lambda x:x*x*x,l))
# print(mayank)
# def filter_function(a):
#     return a>5
# manku= list(filter(filter_function,l))
# print(manku)

# class person:
#     name="mayank"
#     age= 22
    
# a=person()
# a.name="vanshika"
# a.age = 99
# print(a.name)
# print(a.age)

# class person:
#     def __init__(self,name,occ):
#         print("hello mayank")
#         self.name=name
#         self.occ=occ
# def info(self):
#     print(f"{self.name} is a {self.occ}")

# a=person('mayank','singer')
# a.info()

# print("decorate")

# class RailwayForm():
#     FormType = "RailwayForm"
#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"Train is {self.train}")

# mayanksApplication = RailwayForm()
# mayanksApplication.name = 'Mayank'
# mayanksApplication.train = 'rajdhani express'
# mayanksApplication.printData( ) 

# class Employee:
#     company = "Google"

# mayank = Employee()
# vanshu = Employee()
# print(mayank.company)
# print(vanshu.company)
# Employee.company = 'facebook'
# print(mayank.company) 
# print(vanshu.company)



 
 


   











