import Lorem_Ipsum_Generator
from Lorem_Ipsum_Generator import lorem_ipsum as li
np = int(input('Enter the number of paragraphs - '))
nl = int(input('Enter the number of lines per para - '))
nw = int(input('Enter the number of words per line - '))
c = input('Do you want to store this random text in a file ? (Y/N) - ')
txt = li(np, nl, nw)
if c == 'y' or c == 'Y':
    lor_text = open("rand_text.txt", "w")
    lor_text.write(txt)
    lor_text.close()
else:
    print(txt)