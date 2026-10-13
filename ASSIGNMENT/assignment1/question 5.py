P = float (input ("Enter principal: "))
T = float (input ("Enter time: "))
R = float (input ("Enter rate:"))

amount = P * (1 + R / 100) ** T
CI = amount - P

print ("compound interest =", CI)
print ("amount =", amount)