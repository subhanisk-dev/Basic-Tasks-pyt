print("===== STUDENT RESULT SYSTEM =====")

name = input("Enter Student Name: ")

python = int(input("Enter Python Marks: "))
js = int(input("Enter js Marks: "))
sql = int(input("Enter SQL Marks: "))
html = int(input("Enter HTML Marks: "))
css = int(input("Enter CSS Marks: "))

total = python + js + sql + html + css
average = total / 5

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A+")
elif average >= 75:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")

if python < 35 or js < 35 or sql < 35 or html < 35 or css < 35:
    print("Status: Failed in one or more subjects")
else:
    print("Status: Passed")