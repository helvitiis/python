# Program that calculates a user's weekly gross and take-home pay.

print("Pay Check Calculator")
print()

hoursWorked = float(input("Hours Worked: "))
payRate = float(input("Hourly Pay Rate: "))

taxRate = 18 # 18%

grossPay = hoursWorked * payRate
taxAmt = grossPay * (taxRate / 100)
takeHomePay = grossPay - taxAmt

print()
print("Gross Pay: ", grossPay)
print("Tax Rate: ", taxRate, "%")
print("Tax Amount: ", taxAmt)
print("Take Home Pay: ", takeHomePay)
