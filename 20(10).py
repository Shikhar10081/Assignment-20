def anagram(x,y):
    Sx=sorted(x)
    Sy=sorted(y)
    print('yes it is Anagram') if Sx==Sy else print("no")  
x=str(input("Enter str:: "))
y=str(input("Enter str:: "))
anagram(x,y)
