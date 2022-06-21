'''    strings   '''
# a="hello"
# print(a,type(a))
'''    isspace    '''
# b=""
# print(b.isspace())
# print(b,type(b))
# c='    '
# print(c.isspace())
# print(c,type(c))
"""   Number System   """
'''  binary number  '''
# c=0b1001
# print(c,type(c))
# c=24
# print(bin(c),type(c))
'''   octal number   '''
# a=23
# print(oct(a),type(a))
# a=0o23
# print(a,type(a))
'''   hexadecimal numbers   '''
# b=0x26
# print(b,type(b))
# b=38
# print(hex(b),type(b))
# k=31
# print(hex(k),type(k))
'''    swapping of two numbers    '''
# a=25;b=67
# a,b=b,a
# print(a)
# print(b)
'''    print types    '''
# print("hello","hi")
# print("hello""hi")
# a,b,c,d,e=1,2,3,4,5,6 #ValueError: too many values to unpack (expected 5)5
# a="Hello"
# b=5
# print("the value of a is",a)
# print("the value of b is",b)
'''    string concatenation    '''
# a=5;b="hello";c=4.2
# print(a,type(a))
# print(b,type(b))
# print(c,type(c))
# # print("the value of a is"+a)  #TypeError: can only concatenate str (not "int") to str
# # print("the value of c is"+c)     #TypeError: can only concatenate str (not "float") to str
# print("the value of c is",c)     #  the value of c is 4.2
# print("the value of b is"+b)    #  the value of b ishello
# print("the value of b is",b)       #  the value of b is hello
# a="python"
# b='3.9.6'
# print(a+b)   #   python3.9.6
# print(a,b)     #  python 3.9.6
'''   sep() method   '''
# a="hello";b="world"
# print(a,b,sep=" ")   #  hello world
# print("hello","world",sep=".")     #  hello.world
# print("hello","world",sep="@")    #   hello@world
'''   end() method   '''
# print("core","python",end=" " "hello")   #  core python hello
# print("core","python",end=" " "hello")
# print("core","python",end=" " "hello")      #  core python hellocore python hellocore python hellocore python-3
# print("core","python",end="-" "3")
'''   combination of end() and sep() methods    '''
# print("hello"       "python",sep=" ",end=".")   #   hellopython.core python adv python
# print("core python",end=" ")
# print("adv python")
# print("hello"    ,   "python",sep="-",end=".")   #   hello-python.core python.adv python
# print("core python",sep="@",end=".")
# print("adv python")
# print("core","python",sep="" "hello")   #   corehellopython
# print("core","python",sep="-" "hello")    #   core-hellopython
# print("core","python",sep="-\n" "hello")    
# print("core","python",sep="-" "hello\n")
# print("core","python",sep="-" "hello")
# print("core","python",end=" " "hello")
# print("core","python",end="-" "3")
'''if we want to print a word "n" times then print("hello"*n)'''
# print("hello "*10," world"*10,sep=" ")