import Cryptic_Translator
from Cryptic_Translator import translate as t
stmt = []
choice = "Y"
print("\n<<<<<< Encryptor >>>>>>")
while choice == "Y" or choice == "y" :
    str_input = input("Enter the phrases to translate - ")
    stmt.append(str_input)
    choice = input("Do you want to continue (Y/N) - ")

print("\n<<<<< Encrypted Output >>>>>")
for i in stmt:
    t(i)
