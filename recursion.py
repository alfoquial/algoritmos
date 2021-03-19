def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)


def limpiacadena(cadena):
    nuevacadena = ""
    for caracter in cadena:
        if caracter not in ".,;: ":
            nuevacadena = nuevacadena + caracter
    return nuevacadena


def palindromo(cadena):
    if len(cadena) >= 2 and cadena[0].capitalize() == cadena[-1].capitalize():
        palindromo(cadena[1:-1])
    else:
        return False

    return True

# reverse words in a sentence


def reverse_sentence(sentence):
    words = sentence.split()

    for position, word in enumerate(words):
        words[position] = reverse(word)

    return " ".join(words)


def reverse(word):
    if len(word) == 1:
        return word
    else:
        return word[-1] + reverse(word[0:-1])


def baseconversion(number, base):
    convstr = "0123456789ABCDEF"
    if number < base:
        return convstr[number]
    else:
        return str(baseconversion(number//base, base)) + convstr[number % base]


print(baseconversion(1453, 16))
