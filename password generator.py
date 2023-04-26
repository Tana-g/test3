import secrets as s
import string

"""letters = string.ascii_letters
digits = string.digits
special_char = string.punctuation
alphabets = letters+digits+special_char
pswordlength = 10
pwd = ""
while True:
    pwd = ''
    for i in range(pswordlength):
        pwd += ''.join(s.choice(alphabets))
    if(any(char in special_char for char in pwd) and
    sum (char in digits for char in pwd) >= 2):
        break
print(pwd)"""


alphabets=string.ascii_letters+string.digits+string.punctuation
pwd=''
for i in range(12):
    pwd += ''.join(s.choice(alphabets))
print(pwd)
