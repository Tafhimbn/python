# Arithmetic Operators
a = 21
b = 10
c = 0

c = a + b    # Addition
print (f"a: {a} b: {b} a+b: {c}")
c = a - b    # Subtraction 
print (f"a: {a} b: {b} a-b: {c}")
c = a * b    # Multiplication 
print (f"a: {a} b: {b} a*b: {c}")
c = a / b    # Division
print (f"a: {a} b: {b} a/b: {c}")
c = a % b   # Modulas
print (f"a: {a} b: {b} a%b: {c}")
a = 2
b = 3
c = a**b  # Root / Exponent
print (f"a: {a} b: {b} a**b: {c}")

a = 10
b = 5
c = a//b # Floor Division
print (f"a: {a} b: {b} a//b: {c}")

# Assignment Operators
a = 21
b = 10
c = 0
print (f"a: {a} b: {b} c : {c}" )
c = a + b
print (f"a: {a}  c = a + b: {c}" )
c += a
print (f"a: {a} c += a: {c}" )
c *= a
print (f"a: {a} c *= a: {c}" )
c /= a 
print (f"a: {a} c /= a : {c}" )
c  = 2
print (f"a: {a} b: {b} c : {c}" )
c %= a
print (f"a: {a} c %= a: {c}" )
c **= a
print (f"a: {a} c **= a: {c}" )
c //= a
print (f"a: {a} c //= a: {c}" )


# Bitwise Operators

a = 20            
b = 10            

print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0
c = a & b;  # ADD      
print ("result of AND is ", c,':',bin(c))
c = a | b;    # OR 
print ("result of OR is ", c,':',bin(c))
c = a ^ b;    # XOR 
print ("result of EXOR is ", c,':',bin(c))
c = ~a;        # COMPLEMENT    
print ("result of COMPLEMENT is ", c,':',bin(c))
c = a << 2;      # LEFT SHIFT 
print ("result of LEFT SHIFT is ", c,':',bin(c))
c = a >> 2;       # RIGHT SHIFT
print ("result of RIGHT SHIFT is ", c,':',bin(c))



# Logical Operators

var = 5

print(var > 3 and var < 10)
print(var > 3 or var < 4)
print(not (var > 3 and var < 10))