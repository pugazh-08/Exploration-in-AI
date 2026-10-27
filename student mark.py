name=(input("Enter Student name:"))
n=int(input("Enter No of Subject:"))
total=0
for i in range(1,n+1):
    mark=float(input(f"Enter mark for subject{i}:"))
    total+=mark
p=total/n
if p>=90:
    grade='A+'
    performance="outstanding "
elif p>=80:
    grade='A'
    performance="Excellent"
elif p>=70:
    grade='B'
    performance=" Very Good"
elif p>=60:
    grade='c'
    performance="Good"
elif p>=50:
    grade='D'
    performance="Average"
else:
    grade='F'
    performance="Needs improvement"

print("\n ----Academic Performance----")
print("Student Name     :",name)
print("Total marks      :",total)
print("Percentage       :",round(p,2),"%")
print("Grade            :",grade)
print("performance      :",performance)
print("All the Best! Study Well !",)
