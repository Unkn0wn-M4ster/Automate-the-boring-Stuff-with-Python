def func(*arg):
    for  index,item in enumerate(arg):
        if index<len(arg)-1:
            print(item,end=",")
        else:            
            print('and',item)
func(*['apples', 'bananas', 'tofu', 'cats'])