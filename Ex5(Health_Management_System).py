print("This is Health Management System.")
a = int(input("Enter 0 if you want to log data or enter 1 if you want "+
          "to retrieve data.\n"))
b = int(input("Enter 0 if you are Aditya, enter 1 if you are Anant or "+
          "enter 2 if you are Harshit.\n"))
c = int(input("Enter 0 if you want log/retrieve exercise or enter 1 if "+
          "you want to log/retrieve food.\n"))
          

def getdate():
    import datetime
    return datetime.datetime.now()

def func1(b):
    e = input("Enter the type of exercise you have done.\n")
    if b == 0:
        d = open("Aditya_Exercise.txt","a")
        d.write(str([str(getdate())])+ " "+e + "\n" )
        print("Your data has been recorded.")
        d.close()
    elif b == 1:
        d = open("Anant_Exercise.txt","a")
        d.write(str([str(getdate())])+ " "+e + "\n" )
        print("Your data has been recorded.")
        d.close()
    elif b == 2:
        d = open("Harshit_Exercise.txt","a")
        d.write(str([str(getdate())])+ " "+e + "\n" )
        print("Your data has been recorded.")
        d.close() 

def func2(b):
    f = input("Enter the type of food you have eaten.\n")
    if b == 0:
        g = open("Aditya_Food.txt","a")
        g.write(str([str(getdate())])+ " "+f + "\n" )
        print("Your data has been recorded.")
        g.close()
    elif b == 1:
        g = open("Anant_Food.txt","a")
        g.write(str([str(getdate())])+ " "+f + "\n" )
        print("Your data has been recorded.")
    elif b == 2:
        g = open("Harshit_Food.txt","a")
        g.write(str([str(getdate())])+ " "+f + "\n" )
        print("Your data has been recorded.")
        g.close()

def func3(b,c):
    if b == 0 and c == 0:
        h = open("Aditya_Exercise.txt")
        i = h.read()
        print(i)
    elif b == 1 and c == 0:
        h = open("Anant_Exercise.txt")
        i = h.read()
        print(i)
    elif b == 2 and c == 0:
        h = open("Harshit_Exercise.txt")
        i = h.read()
        print(i)
    elif b == 0 and c == 1:
        h = open("Aditya_Food.txt")
        i = h.read()
        print(i)
    elif b == 1 and c == 1:
        h = open("Anant_Food.txt")
        i = h.read()
        print(i)
    elif b == 2 and c == 1:
        h = open("Harshit_Food.txt")
        i = h.read()
        print(i) 
if a == 0 and c == 0:
    func1(b)

elif a == 0 and c == 1:
    func2(b)

elif a == 1:
    func3(b,c)

else:
    print("You better write the correct option the next time you "+
          "run the program.")
          


