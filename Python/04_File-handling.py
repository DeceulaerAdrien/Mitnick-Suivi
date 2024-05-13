import os

filename = "./data/handling/data.txt"
my_file = open(filename, "r")

split = my_file.read().split()

#     print(elem)

my_file.close()

path = os.path.join("./data/handling")
content = ""
txt_file = []

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".txt"):
            txt_file.append(os.path.join(root, file))

for elem in txt_file:
    content += open(elem, "r", encoding="latin1").read()

open(os.path.join("./", "handling_final.txt"), "w").write(content)
