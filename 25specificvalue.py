l = [1,5,8,3]
n= int(input("enter a value :"))
def with_group(l,n):
    for i in l:
        if n==i :
            return True
    return False
print(with_group(l,n))

#output
'''
enter a value :1
True

enter a value :2
False
'''