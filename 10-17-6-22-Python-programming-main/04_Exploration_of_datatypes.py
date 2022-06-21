'''The below example for int (integer) data type'''
# n=5;m=0;p=-4
# print(n,type(n)) 
# print(m,type(m)) 
# print(p,type(p)) 

'''The below example for float (decimal) data type'''
# n=3.6;m=0.9;p=-7.2
# print(n,type(n)) 
# print(m,type(m)) 
# print(p,type(p)) 

'''converting int to float'''
# b=10
# print(b)
# print(b,type(b))
# print(int(b))
# print(float(b))
# c=float(b)
# print(c,type(c))

'''converting float to int'''
# g=4.5
# print(g)
# print(int(g))
# print(float(g))

# k=0.2+0.1
# print('%f'%k) 
# print('%.1f'%k) 
# print('%.2f'%k) 
# print('%.3f'%k) 

'''When not/forgot to keep . (point) then spaces will be printed'''
# k=0.3+0.4
# print('%1f'%k) 
# print('%2f'%k) 
# print('%14f'%k) 
# print('%14f'%k) 
# print('%24f'%k) 
# print('%34f'%k) 
# print('%44f'%k) 


# b="python"
# c='hello'
# d='''Hello Python'''
# e="""hi hey"""
# print(b,type(b))
# print(c,type(c))
# print(b,type(d))
# print(e,type(e))
# a="hello" "world"
# print(a,type(a))

'''To keep a space between them following are the ways'''
# a="hello "   "world"  
# print(a,type(a))    

# b="hello"   " world"
# print(b,type(b))

# c="hello" ' ' "world"
# print(c,type(c))


# name="python"
# print("My Name is"+name)
# print("My Name is "+name)
# print("My Name is",name)
# print("My Name is" " "+name)
# print("My Name is"+" "+name)
# print("My Name is" ' ' +name)
# print("My Name is"+' '    +name)
# print("My Name is",name,sep=" ")

# h=" python"
# print("My Name is"+h)
# print("My Name is",h)


# place=7
# print("%d"%place)
# print("%i"%place)
# print(place)
# print("%f"%place)



'''Date: August 12-08-2021'''
"""Note:We can convert number (integer/float)
to str (string) but we cannot convert str
to integer or float until the string contains
the number in it."""

# a=5
# print(a,type(a))
# b=str(a)
# print(b,type(b))
# print("The Value entered is"+a)
# print("The Value entered is"+b)


# a=7.4
# print(a,type(a))
# b=str(a)
# print(b,type(b))
# c=int(a)
# print(c,type(c))


# a='5'
# print(a,type(a))
# b=int(a)
# c=float(a)
# print(b,type(b))
# print(c,type(c))

# n="python"
# v=int(n) 
# x=float(n) 
# print(v) 
# print(x) 


'''None data type'''
# b=None
# print(b,type(b))

# boolean ( bool) data type
'''Note: boolean means either True or False'''
# x=True
# print(x,type(x))
# y=False
# print(y,type(y))
# print(3<6)
# print(3>6)

# m="hello"
# print(m[5])
# print("%c"%m[0]) 
# print("%c"%m[1])
# print("%c"%m[2])
# print("%c"%m[3])
# print("%c"%m[4])
# print("%c"%m[-1]) 
# print("%c"%m[-2])
# print("%c"%m[-3])
# print("%c"%m[-4])
# print("%c"%m[-5])
# print("%c"%m[5]) # IndexError: string index out of range

# w="12899"
# print(int(w[0])+ int(w[-1]))

'''List Data Type
List is represented by square brackets [ ]
list is mutable, modifications can be made.
list can contain several datatypes in it.
we can represent an empty list'''


# a=[]
# print(a,type(a))

# p=["Ameerpet",55]
# print(p,type(p))
# print(p[0],type(p[0]))
# print(p[1],type(p[1]))

# b=[2,7.9,"hi",None,True]
# print(b[0],type(b[0]))
# print(b[1],type(b[1]))
# print(b[2],type(b[2]))
# print(b[3],type(b[3]))
# print(b[4],type(b[4]))
# print(b[5],type(b[5])) # IndexError: list index out of range


'''Note: modifications cannot be made inside the string data type'''
# s="hello"
# s[0]='H'
# print(s) # TypeError: 'str' object does not support item assignment

'''Note: List will allow the modifications'''
# r=[4,3.1,"python"]
# r[0]=89.23
# r[-1]='Python'
# print(r)


'''Date: 13-08-2021 (Friday) '''

'''Tuple Data Type
Tuple is represented by ( ,) then only
it is called as tuple. A comma , should
be kept/assigned to the variable/ in the print.

Tuple can also contain several data types in it.
Tuple is immutable, modifications cannot be made.
'''

# y=("a")
# print(y,type(y)) # ('a',) <class 'tuple'>

# h=(3,6.8,'by',None)
# print(type(h))
# print(h[-1])
# h[0]=5



'''when trying to print the code which is
already printed , will get None'''
# c=print('hi') # hi
# d=print(c) # None
# print(c,type(c)) # None <class 'NoneType'>


# x=(1)
# print(x,type(x))

# x=(1,)
# print(x,type(x))

# pr=('apple','reliance','asus','dell','samsung')
# pr[1]="Motorolla"
# print(pr)

# n="Hello" ,  "World"
# print(n,type(n)) 
# print(n[0])

"""  Date: 14-08-2021     """
# a=complex(2+6j)
# print(a,type(a)) # (2+6j) <class 'complex'>

# a=complex(4j)
# print(a,type(a)) # 4j <class 'complex'>

# a=complex(-2j)
# print(a,type(a)) # (-0-2j) <class 'complex'>

# a=complex(0j)
# print(a,type(a)) # 0j <class 'complex'>

# a=complex(-0j)
# print(a,type(a)) # (-0-0j) <class 'complex'>

# a=complex(1+(-3j)) 
# print(a,type(a))  # (1-3j) <class 'complex'>


# v=2j
# print(v,type(v)) # 2j <class 'complex'>


# v=-2j
# print(v,type(v))  # (-0-2j) <class 'complex'>


# v=0+2j
# print(v,type(v))   # 2j <class 'complex'>


# v=-1+2j
# print(v,type(v))   # (-1+2j) <class 'complex'>

# g=-0+(-0j)
# v=0+(-0j)
# b=0-0j
# n=0-(-0j)
# m=0-(+0j)
# x=0+0j
# print(g,type(g))  # 0j <class 'complex'>
# print(v,type(v))  # 0j <class 'complex'>
# print(b,type(b))  # 0j <class 'complex'>
# print(n,type(n))  # 0j <class 'complex'>
# print(m,type(m))  # 0j <class 'complex'>
# print(x,type(x))  # 0j <class 'complex'>


# a=75_345
# print(a,type(a)) # 75345 <class 'int'>

"""set data type
set is represented by { } with element inside it
but we cannot represented an empty set.
if we keep an empty set { } it will treated
as dictionary (dict) 
set can contain several data types in it but
we cannot have a list and one more set inside it.
set cannot have one more set inside it.
set is immutable , modifications cannot be made.
set is unordered.
"""

# e={}
# print(e,type(e)) # {} <class 'dict'>

# v={1,2,3}
# print(v,type(v)) # {1, 2, 3} <class 'set'> 

# v={1,2.6,"Hello",("hi",2)}
# print(v,type(v)) # <class 'set'>

# n={10,20,30}
# print(n[1]) # TypeError: 'set' object is not subscriptable

# d={1,3,5}
# print(d,type(d)) # <class 'set'>
# k=frozenset(d)
# print(k)
# print(k,type(k)) # frozenset({1,3, 5}) <class 'frozenset'>
# print(k[0])

"""       Date: 16-08-2021   """
''' Dictionary:  It is a data type in python.
It is represented by { : } , dict (dictionary) it is 
a combination of key-value pair.
The value can be accessed with the help of a key.
dict can have several data types in it , it can also
have one more dict inside it.
'''

# book={
# 1: "Python Programming",
# 2: 'Core Python Programming',
# 3: 'Advance Python Programming'
# }
# print(book[2])
# print(book[10]) # KeyError


h={1:"", 2: "Python", 3: 7, 4: 6.2,
5: [1,4], 6: (4,3), 7: {1,2},
8: {3: "world"}}
# print(h[1],type(h[1]))
# print(h[2],type(h[2]))
# print(h[3],type(h[3]))
# print(h[4],type(h[4]))
# print(h[5],type(h[5]))
# print(h[6],type(h[6]))
# print(h[7],type(h[7]))
# print(h[8],type(h[8]))
# print(h,type(h))
# print(h.keys())
# print(h.values())
# print(h.items())

# t=range(6)
# print(t,type(t)) # (0,6) <class 'range'>
# for i in t:
    # print(i)  #  ones
    # print(i*i) # squares
    # print(i*i*i) # cubes


# n=int(input())
# for i in range(5,n): print(i)

# x=b"hello world"
# print(x,type(x))

# z=B"hello"
# print(z,type(z))
# d=bytearray(b"hello")
# print(d,type(d))


# print('\u0001')
# print('\u0002')
# print('\u0003')
# print('\u0004')
# print('\u0005')
# print('\u0006')
# print('\u0007')
# print('\u0008')
# print('\u0009')

# print('\U0001f601')
# print('\U0001f602')
# print('\U0001f603')
# print('\U0001f604')