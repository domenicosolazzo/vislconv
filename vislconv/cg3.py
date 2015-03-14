import re


def transform_whitespace(compword):
    """Avoid whitespace-separated compound words.
Returns compword with whitespace substituted with underscores."""
    return re.sub('\s+', '_', compword)


# FIXME Will probably barf on larg files, make use of generators
# TODO use newline_eos and marker_eos to enable users to choose none,
#      one or both ways to discover sentence-end markers
#      (these arguments are currently not in use)
def read(cg3_file, newline_eos=True, marker_eos=True):
    """Read a file containing CG3-formatted data.

Returns: a list of sentences of the following structure:
- Each sentence is itself a list containing information about each word.
- Each word is again a list of the form:
  [TOKEN, LEMMA, TAG0, TAG1, ...]
    """
    rx_token = re.compile("^\"<(.+?)>\"$")
    rx_attributes = re.compile("^\s+\"(.+?)\"\s+(.+)$")

    # For files that use an empty line to mark sentence-end
    rx_eos = re.compile("^\s*$")

    # For files that use the "<<<" token to mark sentence-end
    marker_eos = "<<<"
    was_eos = False  # Set to true whenever "<<<" is found

    curr_token = None
    curr_word = []
    curr_sentence = []
    result = []

    for line in cg3_file:

        # Empty line or sentence-end marker marks sentence-end, raise
        # eos flag
        if rx_eos.match(line) or marker_eos in line:
            was_eos = True

        if rx_token.match(line):
            curr_token = transform_whitespace(
                rx_token.match(line).group(1)
            )

        if rx_attributes.match(line):
            curr_lemma = transform_whitespace(
                rx_attributes.match(line).group(1)
            )
            curr_attrs = rx_attributes.match(line).group(2).split()
            curr_word = [curr_lemma] + curr_attrs

            if curr_token and curr_word:
                curr_sentence += [[curr_token] + curr_word]
                curr_token = None
                curr_word = []

        # If a sentence-end marker was encountered in the previuos
        # iteration, process the sentence
        if was_eos:
            result += [curr_sentence]
            curr_sentence = []
            curr_token = None
            curr_word = []
            was_eos = False

    # Final cleanup (in case of missing blank line or attributes at the end)
    if curr_token and curr_word:
        curr_sentence += [[curr_token] + curr_word]
        curr_token = None
        curr_word = []

    if curr_sentence:
        result += [curr_sentence]

    return result

###############################################################################
# WORD-LEVEL
###############################################################################


def token(word):
    """Return the token for the word."""
    return word[0]


def attribute_list(word):
    """Return a list of attributes from the word."""
    return word[1:]


def lemma(word):
    """Return the lemma for the word."""
    return attribute_list(word)[0]


def tag_list(word):
    """Return the tag list for the word."""
    return attribute_list(word)[1:]


def coarse_tag(word):
    """Return the coarse-grained tag for the word."""
    return tag_list(word)[0]


def fine_tag_list(word):
    """Return the fine-grained tags for the word."""
    return tag_list(word)[1:]


###############################################################################
# SENTENCE-LEVEL
###############################################################################

def tokens(sentence):
    """Return a list of tokens from the sentence."""
    return [token(w) for w in sentence]


def attribute_lists(sentence):
    """Return a list of attributes (as a list) from the sentence."""
    return [attribute_list(word) for word in sentence]


def lemmas(sentence):
    """Return a list of lemmas from the sentence."""
    return [lemma(word) for word in sentence]


def tag_lists(sentence):
    """Return a list of tags (as a list) from the sentence."""
    return [tag_list(word) for word in sentence]


def coarse_tags(sentence):
    """Return a list of coarse-grained tags from the sentence."""
    return [coarse_tag(word) for word in sentence]


def fine_tag_lists(sentence):
    """Return a list of fine-grained tags from the sentence."""
    return [fine_tag_list(word) for word in sentence]


###############################################################################
# DOCUMENT-LEVEL
###############################################################################


def tokens_all(document):
    """Return a list of lists of tokens from all sentences."""
    return [tokens(sentence) for sentence in document]


def attribute_lists_all(document):
    """Return a list of lists of attributes from all sentences."""
    return [attribute_lists(sentence) for sentence in document]


def lemmas_all(document):
    """Return a list of lists of lemmas from all sentences."""
    return [lemmas(sentence) for sentence in document]


def tag_lists_all(document):
    """Return a list of lists of tags from all sentences."""
    return [tag_lists(sentence) for sentence in document]


def coarse_tags_all(document):
    """Return a list of lists of coarse-grained tags from all sentences."""
    return [coarse_tags(sentence) for sentence in document]


def fine_tag_lists_all(document):
    """Return a list of lists of fine-grained tags from the sentence."""
    return [fine_tag_lists(sentence) for sentence in document]


def print_tsv(sentence):
    """Print parsed cg3 as tab-separated lines.

Each sentence is separated by an empty line."""
    for sent in sentence:
        for w in sent:
            print "\t".join(w)
        print
