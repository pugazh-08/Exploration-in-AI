def calculate(u):
    bill=0
    if u==100:
        bill=u*1.50
    elif u<=250:
        bill=100*1.50+(u-100)*2.50
    elif u<=500:
        bill=100*1.50+100*2.50+(u-200)*4.00
    else :
        bill=100*1.500+100*2.50+100*4.00+(u-500)*6.00
    return bill
n=int(input("Enter number of customers:"))
for i in range (1,n+1):
    print(f"\n Coustomer {i}")
    name=input("Enter customer Name: ")
    u=float(input("Enter unit consumed:"))
    bill=calculate(u)
    print("CUSTOMER NAME :",name)
    print("UNITS         :",u)
    print("BILL AMOUNT   :Rs.",round(bill,2))