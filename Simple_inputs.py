#run_time_input

''' a=int(input("Enter a value : "))
b=int(input("Enter b value : "))
print(a+b) '''

'''a=float(input("Enter a value : "))
b=float(input("Enter b value : "))
print(a+b) '''

'''a=str(input("Enter a String : "))
b=str(input("Enter b String : "))
print(a+b)''' 

'''a=(input("Enter a String : "))
b=(input("Enter b String : "))
print(a+" "+b)''' 

'''fname=input("fname : ")
lname=input("lname : ")
print((fname+" "+lname).title())'''

'''city=input("Enter a city :")
print("city is",city) '''

'''a=complex(input("Data1 : "))
b=complex(input("Data2 : "))
print(a+b) '''

'''a=bool(input("Data1 : "))
b=bool(input("Data2 : "))
print(a+b) '''

'''a=bool(input("Data1 : "))
b=bool(input("Data2 : "))
c=bool(input("Data3 :"))
print(a+b+c) '''

'''a=int(input("a value: "))
b=int(input("b value: "))
option=int(input("choss the option 1.Add 2.Sub 3.Mul"))
print(a+b)
print(a-b)
print(a*b)'''

'''a=int(input("a value: "))
b=int(input("b value: "))
option=int(input("choss the option \n \t\t1.Add \n \t\t2.Sub \n \t\t3.Mul :"))
print(a+b)
print(a-b)
print(a*b)'''

'''a=int(input())
b=int(input())
print(a+b)'''

'''a=input()
print(a)'''



#Task1

#input --> a=["codegnan","python","course"]
#output --> ["CODEGNAN","PYTHON","COURSE"]

'''a0=input("Enter String")
a1=input("Enter String")
a2=input("Enter String")

a=[a0.upper(),a1.upper(),a2.upper()]
print(a)'''

'''a=["codegnan","python","course"]

b=str(a)
c=b.upper()
print(c)

print(type(c)) '''

#Task2

#input --> ints or strings for Bio Data
#output --> linely bio data

'''name=input("Enter name: ")
idno=int(input("Enter Idno: "))
mob =int(input("Enter Mobno: ")) 
email=input("Enter Email: ")
city=input("Enter city: ")
address=input("Enter address: ")

print("\t \t BIO DATA")
print("\t\t ID-No: ",idno)
print("\t\t Mob-No: ",mob)
print("\t\tEmail: ",email)
print("\t\tCity: ",city)
print("\t\tAddress: ",address) '''


#Task3

#input --> a=[10,20,30,40,50,60]
#output -->[10,20,30,40,50,60,"python"]

a=[10,20,30,40,50,60]
b,c=a,a
a.append("python")
print(a)
b.extend("python")
print(b)
c.extend(["python"])
print(c)
