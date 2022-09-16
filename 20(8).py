def stc():
    x='shikhAr'
    count1=0
    count2=0
    for e in x:
        if e.isupper():
            count1=count1+1
        else:
            count2=count2+1
    print("is upper: ",count1)
    print("is lower:",count2)
stc()       
