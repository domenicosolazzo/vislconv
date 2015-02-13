
def read(conll_file, input_enc='utf-8'):
    curr_sentence = []
    result = []

    for line in conll_file:
        lstr = line.strip()
        if lstr:
            curr_sentence.append(lstr.split())
        else:
            result.append(curr_sentence)
            curr_sentence = []

    if curr_sentence:
        result.append(curr_sentence)
    return result


def tab(word, pos):
    print "%d[%d]" % (len(word), pos)

    if pos >= len(word):
        return '_'
    if not word[pos].strip():
        return '_'
    return word[pos]

###############################################################################
# WORD-LEVEL
###############################################################################


def id(word):
    return tab(word, 0)


def form(word):
    return tab(word, 1)


def lemma(word):
    return tab(word, 2)


def cpostag(word):
    return tab(word, 3)


def postag(word):
    return tab(word, 4)


def feature_list(word):
    return tab(word, 5).split('|')


def head(word):
    return tab(word, 6)


def deprel(word):
    return tab(word, 7)


def phead(word):
    return tab(word, 8)


def pdeprel(word):
    return tab(word, 9)

###############################################################################
# SENTENCE-LEVEL
###############################################################################


def ids(sentence):
    return [id(word) for word in sentence]


def forms(sentence):
    return [form(word) for word in sentence]


def lemmas(sentence):
    return [lemma(word) for word in sentence]


def cpostags(sentence):
    return [cpostag(word) for word in sentence]


def postags(sentence):
    return [postag(word) for word in sentence]


def feature_lists(sentence):
    return [feature_list(word) for word in sentence]


def heads(sentence):
    return [head(word) for word in sentence]


def deprels(sentence):
    return [deprel(word) for word in sentence]


def pheads(sentence):
    return [phead(word) for word in sentence]


def pdeprels(sentence):
    return [pdeprel(word) for word in sentence]

###############################################################################
# DOCUMENT-LEVEL
###############################################################################


def ids_all(document):
    return [ids(sentence) for sentence in document]


def forms_all(document):
    return [forms(sentence) for sentence in document]


def lemmas_all(document):
    return [lemmas(sentence) for sentence in document]


def cpostags_all(document):
    return [cpostags(sentence) for sentence in document]


def postags_all(document):
    return [postags(sentence) for sentence in document]


def feature_lists_all(document):
    return [feature_lists(sentence) for sentence in document]


def heads_all(document):
    return [heads(sentence) for sentence in document]


def deprels_all(document):
    return [deprels(sentence) for sentence in document]


def pheads_all(document):
    return [pheads(sentence) for sentence in document]


def pdeprels_all(document):
    return [pdeprels(sentence) for sentence in document]
