
import vislconv.cg3 as cg3
import codecs
import argparse


datatype_functions = {
    'token': cg3.tokens_all,
    'lemma': cg3.lemmas_all,
    'cpos':  cg3.coarse_tags_all
}


def main(filename, datatype, input_enc):
    cg3data = cg3.read(codecs.open(filename, 'r', input_enc))
    for elm in datatype_functions[datatype](cg3data):
        print " ".join(elm)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Extract data from a Visl CG file.'
    )
    parser.add_argument('file', help='a file in Visl CG format')
    parser.add_argument(
        '--type',
        help='type of data to extract',
        choices=datatype_functions.keys(),
        default='token'
    )
    parser.add_argument(
        '--enc',
        help='encoding of input file',
        default='ISO-8859-1'
    )
    args = parser.parse_args()
    main(args.file, args.type, args.enc)
