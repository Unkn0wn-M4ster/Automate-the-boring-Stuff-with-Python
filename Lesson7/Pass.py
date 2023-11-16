import re
passwd = input("Enter a password : ")
try:
    req= re.compile(r'\w{8,}')
    mo= req.search(passwd)
    a=mo.group()
    if len(a)<8:
        print("Password is weak")
    dig = any(chr.isdigit() for chr in a)
    upper= any(chr.isupper() for chr in a)
    lower= any(chr.islower() for chr in a)
    if dig and upper and lower:
        print("Password is strong")
    else:
        print("Password is weak")
except:
    print("Password is invalid")