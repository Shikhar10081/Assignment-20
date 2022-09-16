def palinrrome(s):
    s1=''
    for e in s:
          s1=e+s1
    if s1==s:
          print("True")
    else:
        print("no")
s=str(input("enter string:"))        
palinrrome(s)
