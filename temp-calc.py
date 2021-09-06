# information

print("Temperature Calculator")
print("Use this tool to convert temperature units")
print("You can convert F* to C* to K* and vice versa")
print("==============================================")

# options input
print("""
Select the first unit. This will be the unit you input
the number you are trying to convert.

1. Fahrenheit
2. Celcius
3. Kelvin
""")
unit1 = input("Select first unit: ")

print("""
Now select the unit you want to convert to. 

1. Fahrenheit
2. Celcius
3. Kelvin
""")
unit2 = input("Select second unit: ")

# operation output
print("Now put the temperature of the 1st unit in:")
unitemp = int(input("Temperature: "))

f_to_c = (unitemp - 32) * 5/9
c_to_f = (unitemp * 9/5) + 32
f_to_k = (unitemp - 32) * 5/9 + 273.15
k_to_f = (unitemp - 273.15) * 9/5 + 32
c_to_k = unitemp + 273.15
k_to_c = unitemp - 273.15
if unit1 == "1" and unit2 == "2":
  print(f_to_c)
elif unit1 == "2" and unit2 == "1":
  print(c_to_f)
elif unit1 == "1" and unit2 == "3":
  print(f_to_k)
elif unit1 == "3" and unit2 == "1":
  print(k_to_f)
elif unit1 == "2" and unit2 == "3":
  print(c_to_k)
elif unit1 == "3" and unit2 == "2":
  print(k_to_c)

