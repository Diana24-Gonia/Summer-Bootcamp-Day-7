'''def diana():
    print("hello")
diana()'''

'''def add():
    return 1 + 1 

def sub():
      print(1 - 1)
    
num = add()
num2 = sub()

print(num)
print(num2)'''

'''def add(x):
    print(x + 1)
i = 142
add(i)'''

'''def triangle(b1, b2, g1):
    print(f"{b1} likes {g1}")
    print(f"{b2} likes {g1}")
triangle(g1="Marjore", b2="Bertox", b1="Don Lowell")'''

'''def names(*args):
    for arg in args:
        print(arg)
names("Bertox", "Don Lowell", "Jerson", "Marjore")'''

'''def names(*args):
    for arg in args:
        print(arg)
names("Bertox", "Don Lowell", "Jerson", "Marjore")'''

def names(**kwargs):  
    for key, value in kwargs.items():
        print(f"{key} ~ {value}")

names(paloma="Airon", Bubbles="daniel")

