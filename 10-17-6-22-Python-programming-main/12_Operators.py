"""    Arithmetic Operators """
# a=float(input("Enter the value of a:"))
# b=float(input("Enter the value of b:"))
# a,b=[int(x) for x in input('Enter the value of a and b: ').split()]
# print(f"The value of {a} + {b} is {a+b}")
# print(f"The value of {a} - {b} is {a-b}")
# print(f"The value of {a} * {b} is {a*b}")
# print(f"The value of {a} / {b} is {a/b}")
# print(f"The value of {a} % {b} is {a%b}")
# print(f"The value of {a} ** {b} is {a**b}")

""" Floor Division """
# c=4//2
# print(c) # 2
# d=4//2.0
# print(d) # 2.0
# e=5//2
# print(e) # 2
# f=5.0//2
# print(f) # 2.0

""" Assignment Operator  """
# a=2
# b=3
# a=a+b
# print(a) # a=2+3  a=5
# a=a+a
# print(a) # a=5+5 a=10


# a=5
# a+=3
# print(a) # a=a+3 a=5+3 a=8
# a-=2
# print(a) # a=a-2  a=8-2  a=6
# a*=4
# print(a) # a=a*4 a=6*4  a=24
# a/=2
# print(a) # a=a/2  a=24/2  a=12.0
# a**=2
# print(a) # a=a**2  a=12.0**2  a=144.0

# p=int(input("Enter the value of p:"))
# print(f"The value of p is {p}")
# p+=2  # p=3  p=3+2 p=5
# print("The value of p after p+=2 is {}".format(p))
# p-=4 # p=p-4 p=5-4 p=1
# print("The value of p after p-=4 is {}".format(p))
# p*=6 # p=p*6 p=1*6 p=6
# print("The value of p after p*=6 is {}".format(p))
# p**=2 # p=p**2  p=6**2  p=36
# print("The value of p after p**=2 is {}".format(p))
# p/=2 # p=p/2  p=36/2  p=18.0
# print("The value of p after p/=2 is {}".format(p))

"""     Relational/Comparision Operators   """
a=int(input("Enter the Value of a:"))
b=int(input("Enter the Value of b:"))
# print(f"The value of {a} < {b} is {a<b}")
# print(f"The value of {a} > {b} is {a>b}")
# print(f"The value of {a} <= {b} is {a<=b}")
# print(f"The value of {a} >= {b} is {a>=b}")
# print(f"The value of {a} == {b} is {a==b}")
# print(f"The value of {a} != {b} is {a!=b}")

# print("The value of %d<%d=%d"%(a,b,a<b))
# print("The value of a=%d , b=%d and a<b=%d"%(a,b,a<b))
# print("The value of a=%d , b=%d and a>b=%d"%(a,b,a>b))
# print("The value of a=%d , b=%d and a<=b=%d"%(a,b,a<=b))
# print("The value of a=%d , b=%d and a>=b=%d"%(a,b,a>=b))
# print("The value of a=%d , b=%d and a==b=%d"%(a,b,a==b))
# print("The value of a=%d , b=%d and a!=b=%d"%(a,b,a!=b))

""" Logical Operator  """
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# print("The value of a<b and b>a is {}".format(a<b and b>a)) # False
# print("The value of a>b and a<b is {}".format(a>b and a<b)) # False
# print("The value of a!=b and a==b is {}".format(a!=b and a==b)) # False
# print("The value of a==b or a>b is {}".format(a==b or a>b)) # True
# print("The value of a!=b or a<b is {}".format(a!=b or a<b)) # True
# print("The opposite of {}=={} is {}".format(a,b,not a==b)) # True
# print("The opposite of {}!={} is {}".format(a,b,not a!=b)) # False

""" Bitwise Operator  """
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# c=int(input("Enter the value of c:"))
# print("The value of {} & {} is {}".format(a,b,a&b))
# print("The value of {} | {} is {}".format(a,b,a|b))
"""Note: The formula for Negation (~) is -(value+1)    """
# print("The value of ~{} is {}".format(a,~a))
# print("The value of ~{} is {}".format(c,~c))


""" Identity Operator   """
# a=[5]; b=5; c=6; d=[5]; e=5; f=c;g=a
# print( a is c) # False 
# print( a is b) # False
# print( a is d) # False
# print( a is f) # False
# print( a is g) # True
# print( b is e) # True
# print( f is g) # False
# print( f is not g) # True
# print( a is not b) # True
# print( b is not e) # False


"""   Membership Operator  """
# name=["Lokenath","Krishna","Harish","Lateesh","Waseem" \
# ,"Sohail","Parvez","Hemalatha","Bhavya","Divya","Priyanka"]
# print("Lateesh" in name) # True
# print("Sohail" in name) # True
# print("Bhavya" in name) # True
# print("Hemalatha" in name) # True
# print("Harish" not in name) # False
# print("Waseem" not in name) # False
# print("Priyanka" not in name) # False
# print("Python" not in name) # True
# name.sort()
# name=['p','n','Y','t','o','H']
# name.sort()
# print(name) # H Y n o p t
# name.sort(reverse=True)
# print(name) #  t p o n Y H
# for i in name:print(i)

