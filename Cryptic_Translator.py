"""
Creating a cryptic language translator
Converts a letter to a letter two places after it
For example a -> c, b -> d and so on.
y -> a and z-> b
"""


def translate(phrase):
    phrase = phrase.lower()
    output = ""
    for letter in phrase:
        m = ord(letter)
        if 97 <= m <= 120:
            m = m + 2
        elif 120 < m <= 122:
            m = m - 24
        output = output + chr(m)
    print(phrase + " --> " + output)

