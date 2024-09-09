import random 

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = '!@#$%^&*()'
number = '0123456789'

all = lower + upper + symbol + number
lenght = 16
password = "".join(random.sample(all, lenght))
print("New Passsword, please note it down: ", password)