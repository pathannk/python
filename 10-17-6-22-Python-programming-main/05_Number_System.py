# from decimal import Decimal as d
# h=d(0.7+0.2) # will give exact lengthy answer
# h=d(0.7)+d(0.2) # will give exact half answer
# h=d('0.7')+d("0.2") 
# print(h)

# a=0.7 ; b= 0.2
# c=a+b
# print(c)
# print('%.1f'%c)

# c=bin(4)
# print(c,type(c)) # 0b100 <class 'str'>

# h=0b100
# print(h)
# n=0B100
# print(n)
# print(0b101) # 5
# print(h,type(h)) # 4 <class 'int'>
# print(n,type(n)) # 4 <class 'int'>


# k=oct(19)
# print(k,type(k)) # 0o23 <class 'str'>

# e=0o23
# print(e)
# f=0O23
# print(f)
# print(e,type(e)) # 19 <class 'int'>
# print(f,type(f)) # 19 <class 'int'>

# y=hex(37)
# print(y,type(y))  # 0x25 <class 'str'>

# t=0x25
# r=0X25
# print(t,type(t)) # 37 <class 'int'>
# print(r,type(r)) # 37 <class 'int'>


from fractions import Fraction as f
# a=f(1,0)
# a=f(1,1)
# a=f(1,5)
# b=f(2)
# c=f(1,0) # We can't even declare like this
# d=f(0,5)
# print(a,type(a)) # 1 <class 'fractions.Fraction'>
# print(b,type(b)) # 2 <class 'fractions.Fraction'>
# print(c,type(c)) # ZeroDivisionError
# print(d,type(d)) # 0 <class 'fractions.Fraction'>


'''Note: We can use Underscore _ in between the numbers 
for clarity in reading and understanding the number.
Ex: 1_23 is same as 123 one hundred and twenty three'''

# a=1_23
# print(a,type(a)) # 123 <class 'int'>

# b=1_.3
# print(b,type(b))  # 12.3 <class float'>

# c=1._03
# print(c,type(c)) # SyntaxError: invalid syntax

# a=5;b=4.6
# print(a,type(a))
# print(b,type(b))
# print(isinstance,(a,int))
# print(isinstance(a ,int))
# print(isinstance(a,float))
# print(isinstance(a,bool))
# print(isinstance(b,float))
'''Note: syntax  isinstance(variable,datatype) '''

# c=2J
# print(c)
# d=1+3j
# print(d,type(d))
# print(isinstance(d,complex))

# e=0+0j
# print(e)

# f=(1-3j)
# print(f)

# g=(0-3j)
# print(g)

# h=(0+ (-3j))
# print(h)

# a=bin(7)
# print(a,type(a))
# b=0b111
# print(b,type(b))
# c=0B111
# print(c,type(c))

# d=oct(19)
# print(d,type(d))
# e=0o23
# print(e,type(e))
# f=0O23
# print(f,type(f))

# g=hex(24)
# print(g,type(g))
# h=0x18
# print(h,type(h))
# i=0X18
# print(i,type(i))
# j=hex(26)
# print(j,type(j))
# k=0x1B
# print(k,type(k))

from fractions import Fraction as F
# print(F(2.5),type(F))
# print(F('2.5'))
# print(F("2.5"))
# y=F(4.5)
# print(y,type(y))
# print(F(5,0))
# b=5/0
# v=F(5,20)
# print(v)

# g=2+3j
# print(g,type(g))
# print(g.real)
# print(g.imag)
# h=2.3j
# print(h,type(h))
# print(h.real)
# print(h.imag)

# print(4)
# print('4')
# print("4")
# print(+4)
# print(+0.1)
# print(+2+3j)
# print(-2+3j)
# print(0-0j)


# print(1e0)
# print(4e0)
# print(1e1)
# print(1e2)
# print(12e2)
# print(1.4e0)
# print(1.4e1)
# print(1.4e2)
# print(1.4e3)

# print(4*5)
# print(2**3)
# print(2**4)
# print(1.5**2)
# print(4**3)

# import math
# print(math.exp(3)) # e=2.71828 , e*e*e
# a=math.exp(1)
# print(a,type(a))