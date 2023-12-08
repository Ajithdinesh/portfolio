# regular expression - search pattern
# search(), findall(), sub(), split()



# import re
# s="the rain in spain"
# exp="in"
# x=re.findall(exp,s)
# print(x)

# import re
# s="the rain in spain"
# exp="in"
# x=re.search(exp,s)
# print(x)

# import re
# s="the rain in spain"
# exp="in"
# x=re.sub(exp,"*",s)
# print(x)

# import re
# s="the rain in spain"
# exp="\s"
# x=re.split(exp,s)
# print(x)

# import re
# s="the rain in spain"
# exp="i"
# x=re.split(exp,s)
# print(x)


# import re
# s="the rain in spain"
# pattern="[abcd]"
# pattern="[a-z]"
# pattern="[a-zA-Z0-9]"
# pattern="^The"
# pattern="^[abcT]"
# pattern="^[abcde]"

# x=re.findall(pattern,s)
# print(x)

# import re
# s="The rain in spain"
# pattern="in$"
# x=re.findall(pattern,s)
# print(x)

# import re
# s="The rain in spain"
# pattern="n*"
# x=re.findall(pattern,s)
# print(x)

# import re
# s="The rain in spain"
# pattern="i+"
# x=re.findall(pattern,s)
# print(x)

# import re
# username=input("enter the string:")
# pattern="^quest..[0-9]"
# x=re.search(pattern,username)
# if x:
#     print("valid username")
# else:
#     print("invalid username")    


import re
phone=input("enter the phone no:")
pattern="^((\+)?91(\-)?(\s)?)?(0)?[0-9][0-9]{9}$"
x=re.search(pattern,phone)
if x:
    print("valid phone no")
else:
    print("invalid phone no") 

