# jabber = open("C:/Users/HP-INDIA/Downloads/sample.txt","r")
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close()
# with open("C:\\Users\\HP-INDIA\\Downloads\\sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

with open("C:\\Users\\HP-INDIA\\Downloads\\sample.txt", 'r') as jabber:
    lines = jabber.read()
print(lines)
# for line in lines[::-1]:
#     print(line, end='')