import datetime
now = datetime.datetime.now()
# Use the 'strftime' method to format the datetime object as a string with the desired format
print(now.strftime(" %d-%m-%Y , %H:%M:%S"))
#output
#06-11-2023 , 16:05:48

# Y , H, M , S are case sensitive
print(now.strftime(" %d %m %y , %h %m %s"))
# error output
'''print(now.strftime(" %d %m %y , %h %m %s"))
   ValueError: Invalid format string'''
