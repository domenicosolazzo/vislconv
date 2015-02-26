# VislConv #
Conversion of Visl formats to other formats.

NB: This is work-in-concept and very project-specific. Don't use it
for anything important.

Currently, only supported input format is [Visl CG](http://beta.visl.sdu.dk/cg3/chunked/streamformats.html#stream-vislcg)
Currently, only supported output format is [conll](http://ilk.uvt.nl/conll/#dataformat).

Ambigious data sets are currently not supported.


## Usage ##

### Conversion ###

To convert a Visl CG3 file to conll:
```
python convert.py <CG3_FILE>
```

To convert Visl CG3 input from stdin to conll:
```
cat <CG3_FILE> | python convert.py
```

In both cases, the converted input is sent to stdout.


### Extraction ###
See extractcg.py for some examples.
