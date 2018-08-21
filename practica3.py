#------------------------------------------------------------------------------------------------------- 
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615

value = 5
result = value + int(str(value)+str(value)) + int(str(value)+str(value)+str(value))
print(result) 