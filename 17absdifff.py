n = int(input("enter the value :"))
def abs_diff(n):
    return((abs(1000-n)<=100) or (abs(2000-n)<=100))
print(abs_diff(n))

#output
'''enter the value :1000
True
enter the value :900 
True
enter the value :800
False
enter the value :2000
True
enter the value :2200
False'''
