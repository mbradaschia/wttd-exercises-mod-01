def mimic_dictx(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    with open(filename, 'r') as myfile:
        data = myfile.read().replace('\n', ' ')

    # apaga caracteres indesejados
    chars = ".,-?"
    for c in chars:
        if c in data:
            data = data.replace(c, '')

    # usa set para ter uma lista sem itens repetidos
    words_set = set(data.split(' '))

    words = {}

    for word in words_set:
        words[word] = data.count(word)

    return words


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    with open(filename, 'r') as myfile:
        data = myfile.read().replace('\n', ' ')

    # apaga caracteres indesejados
    chars = ".,-?\"`*"
    for c in chars:
        if c in data:
            data = data.replace(c, '')

    # usa set para ter uma lista sem itens repetidos
    words_list = data.split(' ')
    words = {}

    for n, word in enumerate(words_list):
        if not words.has_key(word):
            words[word] = []

        lista = words[word]

        if n < len(words_list) - 1:
            lista.append(words_list[n+1])
            words[word] = lista

    return words


if __name__ == '__main__':
    p_word = mimic_dict('alice.txt')

    for word in p_word:
        print ('{} : {}'.format(word, p_word[word]))