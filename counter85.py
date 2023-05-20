   #counter 
import collections

#method 1
a=collections.Counter()
print(a)
a.update('abc')
print(a)
a.update({'a':1,'b':2,'c':3})
print(a)

#method 2
c1 = collections.Counter(['a', 'b', 'c', 'a' ,'b', 'b'])
c2 = collections.Counter('alphabet')
print('C1: ', c1)
print('C2: ', c2)
print ('\nCombined counts: ')
print(c1 + c2)
print('\nSubtraction: ')
print(c1 - c2)
print('\nIntersection (taking positive minimums): ')
print(c1 & c2)
print('\nUnion (taking maximums): ')
print(c1 | c2)
  