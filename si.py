p=float(input("Enter Principle amount:"))
r=float(input("Enter Rate of interest:"))
t=float(input("Enter Time period in years:"))
ci=((p*t*r)/100)**t-p
print("Compound Interest is:",ci)