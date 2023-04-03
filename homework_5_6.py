'''Требуется реализовать программу, которая выводит слово, имеющее максимальную длину
(или список слов, если таковых несколько)'''

words = ['oejrfghjondf', 'efrg', 'qergdfbwrtgbr', 'rfb', 'frbrgbrgb']
max_length = 0
max_words = []
for w in words:
    if len(w) > max_length:
        max_length = len(w)
        max_words = [w]
    elif len(w) == max_length:
        max_words.append(w)
print(max_words)