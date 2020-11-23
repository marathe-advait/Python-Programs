# Lorem Ipsum Generator
import random


def lorem_ipsum(number_of_paras, number_of_lines_per_para, number_of_words_per_line):
    paras = []
    for k in range(number_of_paras):
        lines = []
        for i in range(number_of_lines_per_para):
            words = []
            for j in range(number_of_words_per_line):
                word = ""
                word_length = random.randint(3, 11)
                for k in range(word_length):
                    word = word + chr(random.randint(97, 122))
                words.append(word)
            line = " ".join(words)
            lines.append(line)
        para = "\n".join(lines)
        paras.append(para)
    text = "\n\n".join(paras)
    return text
