#!/usr/bin/env python
# coding: utf-8

# In[2]:


PI = 3.141592

def number_input():
    output = input("숫자입력 : ")
    return float(output) ##아웃풋 값을 float값으로 나오게 강제할 수 있음

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

print("get_circumference(10) :",get_circumference(10))
print("get_circle_area(10) : ",get_circle_area(10))


# In[ ]:




