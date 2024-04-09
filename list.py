num = [1,2,3,4,5]
fruit =["Mango","Apple","Banana"]
info = ["Tafhim","EEE",3.92,None]

print(num)
print(fruit)
print(info)


print(num[2])      # print 3rd one 
print(fruit[:2])   # print upto second one 
print(fruit[2:])   # print from second one
print(info[-1])    # print last one


fruit.append("Licci")           # list append method
print(fruit)

fruit.insert(1,"Coconat")       # list insert method
print(fruit)

num1 = [0,1,2,3,4]
num2 = [5,6,7,8,9]
number = num1 + num2            # concatenate method
print(number)

num.extend(num2)                # extend method
print(num)

fruit1 = ["mango","apple"]
fruit2 = ["grapes","orange"]
fruit1.append(fruit2)           # append vs extend
print(fruit1)

fruit.pop()                     # remove last items
print(fruit)
fruit.pop(1)                    # remove 2nd items
print(fruit)

del fruit[2]                    # delete 3rd item
print(fruit)

fruit.remove("Apple")
print(fruit)

if "Mango" in fruit:            # in list condition
    print("Apple is present in list")
else:
   print("Apple is not present in list")



