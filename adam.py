#from importlib.metadata import pass_none

f_name = "Adams"
print(f_name)
list1 = ["egg", "water", "salt", "beans"]
print(list)
Array = [1,2,4,6,8,10,12]
print(Array)
#import pandas as pd
#d = {"col1":[1,2,3,4,7], "col2":[4,5,6,9,5], "col3":[7,8,12,1,11]}
#df = pd.DataFrame(data=d)
#print(df)
name = input("name")
print("u are welcome", name)
dict1 = {"s_name":"Shawn",
        "age": 29,
         "city":"Ajman",
         "Religion":"Islam"}
print(dict)
#if "age" >=25:
   # print(" u are a Pro")
salary = (int(input("salary")))
debt = (int(input("debt")))
m_age =(int(input("m_age")))
credit_score = salary - debt

if salary<20000 and debt> 50000:
 print("Reject")
 if m_age< 25:
  print("Reject")
 if credit_score > 7000:
  print("Approve")
else:
 pass
print("Reviewing application")

import numpy as np
python_list = [1,2,3,4,5]
numpy_array = np.array([1,2,3,4,5])
print("list:". python_list)
print("array:", numpy_array)
print("\nlist*2:", python_list*2)
zeros = np.zeros(5)
ones = np.ones((3,3))
range_array = np.arange(0.10,2)
random_array = np.random.randint(1,100,size= 5)
print("\nzeros:", zeros)
print("range:", range_array)
print("random array:", random_array)
