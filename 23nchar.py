s = str(input("enter string :"))
n= int(input("enter no of copies :"))
def n_copies(s,n):
    if len(s)>=2:
        print((s[0:2])*n)
    else:
        print(s*2)
n_copies(s,n)

#output
'''enter string :sai
enter no of copies :2
sasa 

enter string :hi
enter no of copies :2
hihi
'''
