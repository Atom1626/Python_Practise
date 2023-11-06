n = str(input("enter string :"))
def new_string(n):
    if len(n)>=2 and n[ :2] == 'Is':
        return n
    else:
        return "Is"+" "+n
print(new_string(n))

#output
'''enter string :Is sai
Is sai
enter string :Sai
Is Sai
enter string :
Is 
enter string :Is
Is'''