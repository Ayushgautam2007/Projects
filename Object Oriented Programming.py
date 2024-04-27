#!/usr/bin/env python
# coding: utf-8

# In[1]:


class student:
    name = "Karan"
    
s1 = student()
print(s1.name)

s2 = student()
print(s2.name)


# In[2]:


class car:
    color = "blue"
    brand = "mercedes"
    
car1 = car()
print(car.color)
print(car.brand)


# In[3]:


class students:
    
    
    def __init__(self,fullname):
        self.name = fullname
        print("adding new student in database.")
        
s1 = students("Karan")
print(s1.name)

s2 = students("Vijay")
print(s2.name)


# In[4]:


class students:
    
    
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database.")
        
s1 = students("Karan", 88)
print(s1.name, s1.marks)

s2 = students("Vijay", 87)
print(s2.name, s2.marks)


# In[5]:


class Students:
    collage_name = "GLA University"
    def __init__(self, name, marks, roll_no):
        self.name=name
        self.marks = marks
        self.roll_no = roll_no
        print("adding new students details in database")
        
s1 = Students("Karan", 67, 5)
s2 = Students("Vijay", 76, 8)
s3 = Students("Anil", 88, 9)

print(s1.name, s1.marks, s1.roll_no)
print(s2.name, s2.marks, s2.roll_no) 
print(s3.name, s3.marks, s3.roll_no)


# In[6]:


class students:
    collage_name = "GLA University"
    
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome", self.name)
        
    def get_marks (self):
        return self.marks
        
s1 = students("Karan", 87)
s2 = students("Vijay", 89)
print(s1.name)
print(s2.name)
s1.welcome()
s2.welcome()
print(s1.get_marks())
print(s2.get_marks())


# In[7]:


class clg_student:
    
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your avg score is", sum/3)
        
s1= clg_student("Ayush", [99, 98, 97])
s1.get_avg()

s1.name = "Karan"
s1.get_avg()


# ## Decorator : Decorators allow us to wrap another function in order to extand the behaviour of the wrapped function, without parmanently modifying it.

# # methods that don't use the self parameter (work at class level) : staticmethod

# In[8]:


class clg_student:
    
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
        
    @staticmethod
    def hello():
        print("Hello")
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your avg score is", sum/3)
        
s1= clg_student("Ayush", [99, 98, 97])
s1.get_avg()

s1.name = "Karan"
s1.get_avg()

print("Hello")


# In[9]:


# Abstarction :

class car:
    
    def __init__ (self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc  = True
        print("car started")
        
car1 = car()
car1.start()


# In[10]:


# Encapsulation : Warraping data and functions into single unit(object):

class car:
    
    def __init__ (self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc  = True
        print("car started")
        
car1 = car()
car1.start()


# In[12]:


class Account:
    
    def __init__ (self, bal, acc):
        self.balance = bal
        self.account_no = acc
              
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())
    
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())
        
    def get_balance(self):
        return self.balance
    
acc1= Account (10000, 23456)
acc1.debit = 1000
acc1.credit = 500


# In[22]:


# del keyword : used for delete object propertes or object itself.

class stud:
    def __init__ (self, name):
        self.name = name
        
s1 = stud("Somya")
print(s1.name)
# del s1
# print(s1)  : NameError: name 's1' is not defined showing this error


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




