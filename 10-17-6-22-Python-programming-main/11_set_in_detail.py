# a={1,2,3}
# b='hello',1,2,3 # Note: can pass string or tuple with many values
# a.add(b) 
# print(a) # {('hello', 1, 2, 3), 1, 2, 3} or {1, 2, 3, ('hello', 1, 2, 3)}

# b={1,5,7}
# b.clear()
# print(b) # set()

# a={1,2,3}; b={4,3,3,6}; c={10,15,20}; d={1,4,7}
# print(a.intersection(b)) 
# print(a.intersection(c)) 
# print(a.intersection(d)) 
# print(b.intersection(d)) 
# print(c.intersection(a)) 
# print(d.intersection(c)) 
# print(d.intersection(a)) 
# print(d.intersection(b)) 

# a={1,2,3}
# b={4,3,5}
# print(a.union(b))
# print(b.union(a))

# a={1,2,3}
# b={4,3,5}
# c={4,3,7}
# a.update(b) 
# a.update(c) 
# c.update(a) 
# print(c) 

# a={5,10,20,25,30}
# b={10,21,5}
# print(a.difference(b)) 
# print(b.difference(a)) 
# print(a-b)
# print(b-a)

# z={55,56,57,73,45,23}
# z.discard(4)
# print(z)
# z.discard(73)
# print(z)

# v={2,7,4,3}
# v.pop()
# print(v)

A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}
# print('Are A and B disjoint?', A.isdisjoint(B))
# print('Are A and C disjoint?', A.isdisjoint(C))
# print('Are B and C disjoint?', B.isdisjoint(C))

# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}
# C = {1, 2, 4, 5}
# print(A.issubset(B))
# print(B.issubset(A))
# print(A.issubset(C))
# print(C.issubset(B))

# print(dir(set))
# print(len(['add', 'clear', 'copy', 'difference',
#  'difference_update', 'discard', 'intersection', 
#  'intersection_update', 'isdisjoint', 'issubset', 
#  'issuperset', 'pop', 'remove', 'symmetric_difference', 
# 'symmetric_difference_update', 'union', 'update']))


""" 1.difference_update"""

# a={5,12,15,18,20}
# b={15,18,21,25}
# a.difference_update(b)
# b.difference_update(a)
# print(a)
# print(b)

"""2.copy"""

# a={1,2,3,4,5}
# a.copy()
# print(a)

"""3. symmetric_difference_update"""

# a={5,12,15,18,20}
# b={15,18,21,25}
# a.symmetric_difference_update(b)
# print(a)
# b.symmetric_difference_update(a)
# print(b)

"""4.intersection_upadate"""

a={5,12,15,18,20}
b={15,18,21,25}
# a.intersection_update(b)
# print(a)
# b.intersection_update(a)
# print(b)

"""5.intersection"""

# a={8,9,10,12,14}
# b={10,14,15,1}
# print(a.intersection(b))#{10,14}
# print(b.intersection(a))#{10,14}

"""6.remove"""

# a={8,9,10,12,14}
# a.remove(10)
# print(a)

"""" 7.issuperset"""

# a={8,9,10,12,14}
# b={10,14,15,1}
# print(a.issuperset(b))
# a={8,9,10,12,14}
# b={8,9,10}
# print(a.issuperset(b))
# print(b.issuperset(a))