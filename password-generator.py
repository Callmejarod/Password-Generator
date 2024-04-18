import random

list =  [
    '0','1','2','3','4','5','6','7','8','9','!','$','%','&','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
        ]

password_list = []

while len(password_list) <= 16:
    generator = random.choice(list)
    password_list.append(generator)
   
print(password_list)

password = ''.join(password_list)

print(f"\nThis is your password:\n{password[0:4]}-{password[4:8]}-{password[8:12]}-{password[12:16]}\n")


#Figure out how to make randomize upper and lower cases