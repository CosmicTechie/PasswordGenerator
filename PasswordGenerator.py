import random
import string

Details=input("Please Enter the Details for Password,such as Site and Username : ")
Length=int(input("Please Enter the password length required: "))

# Get the Characters

lcase=string.ascii_lowercase # All LowerCase Characters
ucase=string.ascii_uppercase # All UpperCase Characters 
digi=string.digits           # All Digits
symbo=string.punctuation     # All Special Characters

# Combining All
all=lcase+ucase+digi+symbo

# Extracting a Random Character from Each
random_lcase=random.choice(lcase)  # Eg: a
random_ucase=random.choice(ucase)  # Eg: Z
random_digi=random.choice(digi)    # Eg: 9
random_symbo=random.choice(symbo)  # Eg: &

# Combining the random charcaters: Eg: aZ9&
# Now, We have a combination of random characters of each type 
chars=random_lcase+random_ucase+random_digi+random_symbo

# Get a string with characters of intended length
for x in range(Length-4):
    chars=chars+random.choice(all)

# Rndomize the string to get the completely random and a strong password
password=''.join(random.sample(chars,len(chars)))
print(password)

f = open("MyFile.txt", "a")# in append mode
f.write(Details+" : "+password+"\n")
f.close()
print("Details saved to MyFile.txt")