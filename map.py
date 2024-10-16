# reduce
import functools

mylist=[1,2,3,6,8,2,39]

def sum(x,y):
    return x+y

result=functools.reduce(sum,mylist,100)
print(result)


# filter

def even(n):
    return n%2==0

result=filter(even,mylist)
print(list(result))