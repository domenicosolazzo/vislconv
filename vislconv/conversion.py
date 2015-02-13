
import cg3


def underscore(elm):
    return elm if elm.strip() else '_'


def to_conll_word(word):
    return "\t".join(
        [underscore(cg3.token(word)),
         underscore(cg3.lemma(word)),
         underscore(cg3.coarse_tag(word)),
         underscore(cg3.coarse_tag(word)),
         underscore("|".join(cg3.fine_tag_list(word))),
         '_', '_', '_', '_', '_']
    ).encode('utf-8')


def to_conll_words(sentence):
    return "\n".join(
        "\t".join([str(i+1), to_conll_word(word)])
        for i, word in enumerate(sentence)
    )


def to_conll_words_all(document):
    return "\n\n".join(to_conll_words(sentence) for sentence in document)
