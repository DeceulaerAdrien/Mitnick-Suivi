import re

# 1. Create a regex that finds integers without size limit.
s = "sssgdds8sfsfs"
pattern = r'\d'

print(re.findall(pattern, s))

# 2. Create a regex that finds negative integers without size limit.
s = r'sssgdds-8sfsfs'
pattern = r'-\d'

print(re.findall(pattern, s))

# 3. Create a regex that finds (positive or negative) integers without size limit.
s = r'sssgdds-8s8fsfs'
pattern = r'-?\d'

print(re.findall(pattern, s))

# 4. Capture all the numbers of the following sentence :
text = "21 scouts and 3 tanks fought against 4,003 protestors, so the manager was not 100.00% happy."
pattern = r'\d+(?:,\d+)*(?:\.\d+)?'

print(re.findall(pattern, text))

# 5. Find all words that end with 'ly'.
text = "He had prudently disguised himself but was quickly captured by the police."
pattern = r'\b\w+ly\b'

print(re.findall(pattern, text))

# 6. License plate number
plate = input("Enter your license plate number: ")
pattern = r'^[A-Z]{2}-\d{3}-[A-Z]{2}$'
if re.match(pattern, plate):
    print("good")
else:
    print("Not good")

# 7 . Address IPV4
ip = input("Enter a IP adress :")
pattern = (r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|['
           r'01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]|0)$')
if re.match(pattern, ip):
    print("good")
else:
    print("Not good")

# 8. Valid Mail
mail = input("Enter your email :")
pattern = r"^[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}$"
if re.match(pattern, mail):
    print("good")
else:
    print("Not good")

# 9. Valid Password
password = input("Enter your password :")
pattern = r"^.{6,}$"
if re.match(pattern, password):
    print("good")
else:
    print("Not good")

# 10. Valid Password bis
password = input("Enter your password :")
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w\s]).{6,}$"
if re.match(pattern, password):
    print("good")
else:
    print("Not good")

# 11. Search by groups
list_mail = open("data/regex/mail.txt", "r")
for line in list_mail:
    m = re.search(r"^(?P<who>\w*)[.]?(?P<who2>\w*)@(?P<operator>\w+)[.](?P<zone>\w+$)", line)

    if m is not None:

        print(m.group("who"))
        print(m.group("who2"))
        print(m.group("operator"))
        print(m.group("zone"))

# 12. Another way of doing things.
# firstName = []
# name = []
# ope = []
# zone = []
#
# for line in list_mail:
#     splitMail = line.replace(".", " ").split("@")
#
#     firstName.append(splitMail[0].split()[0])
#     name.append(splitMail[0].split()[-1])
#     ope.append(splitMail[1].split()[0])
#     zone.append(splitMail[1].split()[-1])
#
# print(firstName, name, ope, zone)

list_mail.close()