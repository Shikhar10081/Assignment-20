def pangram(str):
    A="abcdefghijklmnopqrstuvwxyz"
    flag=True
    for e in A:
        if e not in str.lower():
            flag=False
        
    if flag==True:
        print("pangram")
    else:
        print("non")
str="abcdefghijklmnopqrstuv"
pangram(str)
