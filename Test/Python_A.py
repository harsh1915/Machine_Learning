#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Write a program to divide two numbers 14 and 5 and get the result as 2


# In[ ]:


class DivideNum:
    """Divide two number 14 and 5"""
    def init(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def display(self):
        # return "number1 : {}, number2 :{}".format(self.num1/7,self.num2/2)
        print(self.num1/7)
        print(self.num2/2)

d1=DivideNum()
print(d1)
print(d1.display())


# In[ ]:


2. Write a program to print the following pattern


# In[7]:


"""Triangle Program"""
a = (2 * 5) - 2
for i in range(0, 4):
    for j in range(0, a):
        print(end="   ")

    a = a - 1
    for j in range(0, i + 1):
        print("  *", end='   ')
    print(" ")


# In[ ]:


Using Data Set (a), perform following task
    a. Create a function to increase the basic of all person with 10%.


# In[8]:


data = {
101 : {'personal':{'name':'ABC', 'city':'Ahmedabad'},
'salary':{'basic':5000, 'allowance':500, 'deductions': 50}},

102 : {'personal':{'name':'ABC', 'city':'Delhi'},
'salary':{'basic':7000, 'allowance':700, 'deductions': 70}},

103 : {'personal':{'name':'DEF', 'city':'Ahmedabad'},
'salary':{'basic':4000, 'allowance':400, 'deductions': 40}},

104 : {'personal':{'name':'GHI', 'city':'Ahmedabad'},
'salary':{'basic':2000, 'allowance':200, 'deductions': 20}},

105 : {'personal':{'name':'DEF', 'city':'Delhi'},
'salary':{'basic':1000, 'allowance':100, 'deductions': 10}}}


def increase_salary():

    for k,v in data.items():
        v['salary']["basic"]= v['salary']["basic"] + v['salary']["basic"] * 10 / 100



a=increase_salary()
print(a)
print(data)


# In[ ]:


b. Create a function to filter records leaving in Ahmedabad.


# In[9]:


"""Return city Ahmedabad"""

data = {
101 : {'personal':{'name':'ABC', 'city':'Ahmedabad'},
'salary':{'basic':5000, 'allowance':500, 'deductions': 50}},

102 : {'personal':{'name':'ABC', 'city':'Delhi'},
'salary':{'basic':7000, 'allowance':700, 'deductions': 70}},

103 : {'personal':{'name':'DEF', 'city':'Ahmedabad'},
'salary':{'basic':4000, 'allowance':400, 'deductions': 40}},

104 : {'personal':{'name':'GHI', 'city':'Ahmedabad'},
'salary':{'basic':2000, 'allowance':200, 'deductions': 20}},

105 : {'personal':{'name':'DEF', 'city':'Delhi'},
'salary':{'basic':1000, 'allowance':100, 'deductions': 10}}}

def filter():
    for k, v in data.items():
        if v['personal']["city"] == "Ahmedabad":
            print(k, v)



a=filter()
print(a)


# In[ ]:


4. Using Data Set (a), add one new value in salary as key tax with value 10% of
allowance.


# In[10]:


data = {
101 : {'personal':{'name':'ABC', 'city':'Ahmedabad'},
'salary':{'basic':5000, 'allowance':500, 'deductions': 50}},

102 : {'personal':{'name':'ABC', 'city':'Delhi'},
'salary':{'basic':7000, 'allowance':700, 'deductions': 70}},

103 : {'personal':{'name':'DEF', 'city':'Ahmedabad'},
'salary':{'basic':4000, 'allowance':400, 'deductions': 40}},

104 : {'personal':{'name':'GHI', 'city':'Ahmedabad'},
'salary':{'basic':2000, 'allowance':200, 'deductions': 20}},

105 : {'personal':{'name':'DEF', 'city':'Delhi'},
'salary':{'basic':1000, 'allowance':100, 'deductions': 10}}}

def tax_in_salary():

    for k,v in data.items():
        v['salary']["tax"]= v['salary']["allowance"] * 10 / 100

a=tax_in_salary()
print(data)


# In[ ]:


5. Write a program to class name Bill and print the two bills. [Make necessary
assumptions]


# In[ ]:


class Bill:
    def __init__(self,Name,PhoneNo,TotalAmount):
        self.Name=Name
        self.PhoneNo=PhoneNo
        self.TotalAmount=TotalAmount


    def Electricity_bill(self):
        print("Electricity bill Details",self.Name)
        print("Electricity bill Details",self.PhoneNo)
        print("Electricity bill Details",self.TotalAmount)


    def Water_bill(self):
        print("Water bill details",self.Name)
        print("Water bill details",self.PhoneNo)
        print("Water bill details",self.TotalAmount)

electricbill=Bill("Minaxi",9876548595,6500)

print(electricbill.shopping_bill())


waterbill=Bill("Manish",PhoneNo=9976548595,TotalAmount=8900)

print(waterbill.food_bill())


# In[ ]:





# In[ ]:




