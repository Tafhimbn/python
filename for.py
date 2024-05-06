# for loop
# syntax:
# for iterating_var in sequence:
#   statements(s)

# syntax for range function: range(start, stop, step)
for i in range(10):       # start is 0 by default, step is 1 by default,range generated from 0 to 4
    print(f"count {i}")

num = (37,54,44,80,19,70,21,78,97,45)
sum = 0
for n in num:
   sum+=n
print ("Total =", sum)


for num in range(5, 75, 5):
 print (num, end=' ')


# Python for Loop with Strings
zen = """Lorem Ipsum is simply dummy text of the 
printing and typesetting industry. Lorem Ipsum has 
been the industry's standard dummy text ever since 
the 1500s, when an unknown printer took a galley of 
type and scrambled it to make a type specimen book. """

for char in zen:
   if char not in 'aeiou':
      print (char, end='')


# Python for Loop with Tuples
num = (37,54,44,80,19,70,21,78,97,45)
sum = 0
for n in num:
   sum+=n
print ("Total =", sum)


# Python for Loop with List

num = [54,66,48,33,36]
num_len = range(len(num))
for i in num_len:
   print("index",i, "num:", num[i])

# Python for Loop with Dictionaries

num = {1:"One",5:"Five",6:"Six",8:"Eight",9:"Nine"}
for i in num:
   print("index",i, "num:", num[i])


# for else loop

# syntax: 
# for variable_name in iterable:
#  statements in the loop
# else:
#  Statement in else clause

for count in range(6):
   print (f"Count no. {count}")
else:
   print ("End of for loop")

