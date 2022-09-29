#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?: ")) 
nr_symbols = int(input("How many symbols would you like?: "))
nr_numbers = int(input("How many numbers would you like?: "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
tChar = 0
ez_password = ""
new_password = ""

for count in range(0, nr_letters):
  ez_password += random.choice(letters)
  tChar += 1

for count in range(0, nr_symbols):
  ez_password += random.choice(numbers)
  tChar += 1

for count in range(0, nr_numbers):
  ez_password += random.choice(symbols)
  tChar += 1

print("\n*Ordered password")
print("==================================================")
print(f"Your password is: {ez_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
lst_char = []
lst_password = []

for letter in ez_password:
  lst_char.append(letter)

for char in lst_char:
  while (tChar != 0):
    ranLst_Char = random.choice(lst_char)
    lst_password.append(ranLst_Char)
    lst_char.remove(ranLst_Char)
    tChar -= 1
  
for elem in lst_password:
  new_password += elem
  
print("\n*New Randomised password")
print("==================================================")
print(f"Your new randomized password is : {new_password}")