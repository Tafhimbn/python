#Python data types
# 1. number
# --> Number objects

#    i. Integer
int_num = 5  
print("The type of int_num", type(int_num))  

#    ii. Complex Number
com_num = 1+3j 
print("The type of com_num", type(com_num))  

#    iii. float
float_num = 40.5  
print("The type of float_num", type(float_num)) 



# 2. Sequence
#    --> a collection data type

#    i. String
#       --> a sequence of one or more Unicode characters, enclosed in single, double or triple quotation marks (also called inverted commas). 
str1 = "Python" 
print("The type of str", type(str1))  

#    ii. list
#        --> contains items separated by commas and enclosed within square brackets []
L1 = ["Tafhim", 12, "Bangladesh"] 
L2 = [ 11, 12, 13]  
print("The type of L1", type(L1))  
print("The type of L1", type(L2)) 

#    iii. Tuple
#         --> consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses (...).
#             A tuple is also a sequence, hence each item in the tuple has an index referring to its position in the collection. The index starts from 0.

T1 = ("Python", "Java", "Ruby", "Verilog")  
T2 = (11, 12, 13, 14, 15)  
T3 = "Python", "Java", "Ruby", "Verilog"
print("The type of T1", type(T1))  
print("The type of T2", type(T2)) 
print("The type of T3", type(T3)) 

# 3. Dictionary
#    --> a collection which is ordered*, changeable and do not allow duplicates. Dictionary items are presented in key:value pairs

Employee_dic = {"Name": "Tafhim", "ID": 29, "salary":25000,"Company":"GOOGLE"}    
print("The type of Employee_Dic",type(Employee_dic))  

# 4. Boolean
#    --> one of built-in data types which represents one of the two values either True or False
con = True 
print("The type of Con",type(con))  

# 5. Set
#    -->  a collection, but is not an indexed or ordered collection as string, list or tuple
exam_set = {"A", "B", "C"}
print("The type of Exam_SET",type(exam_set)) 



# Type Casting/Conversion
  # 1) implicit Casting/ conversion  -> Compiler/interpreter automatically converts object of one type into other
a=2
b=3.5
c=a+b
print(c)

a=True
b=3.5
c=a+b
print(c)

   # 2) explicit  Casting/ conversion  -> built-in functions int(), float() and str() to perform the explicit conversions 
 
print("Conversion to integer data type")
a = int(1)
b = int(2.2)
c = int("3") # 3.3 is not possible

print(a)
print(b)
print(c)

print("Conversion to float data type")
a = float(1)
b = float(2.2)
c = float("3.3")

print(a)
print(b)
print(c)


print("Conversion to string data type")
a = str(1)
b = str(2.2)
c = str("3.3")

print(a)
print(b)
print(c)


