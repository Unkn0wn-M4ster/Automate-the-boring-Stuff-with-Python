import re 
date=re.compile(r'(\d{2})/(\d{2})/(\d{4})')
mo=date.search('08/03/2004')
day=str(mo.group(1))
month=str(mo.group(2))
year=str(mo.group(3))

if 1000<=int(year)<=2999:
    if month in ['04','06','09','11']:
        if int(day)<=31:
            print(mo.group())
        else:
            print('invalid day count')
    elif month in ['01','03','5','07','08','10','12']:
        if int(day)<=30:
            print(mo.group())
        else:
            print('invalid day count')
    elif month=='02':
        if (int(year)%4==0 and int(year)%100!=0) or (int(year)%4==0 and int(year)%100==0 and int(year)%400==0):
            if int(day) ==29:
                print(mo.group())
            else:
                print('invalid day count in leap year')
                
        else:
            if int(day)==28:
                print(mo.group())
            else:
                print('invalid day count') 