# base64url

A command-line tool for encoding and decoding using the Base64 URL encoding
scheme.

Requires Python 3. Tested on Python 3.4 and above.

```
$ ./base64url -h
usage: base64url.py [-h] [-b BREAKAT] [-t] [-d] [-i INPUT] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -b BREAKAT, --breakat BREAKAT
                        break encoded string into num character lines
  -t, --trim            trim padding on encoded string
  -d, -D, --decode      decodes input
  -i INPUT, --input INPUT
                        input file (default: stdin)
  -o OUTPUT, --output OUTPUT
                        output file (default: stdout)
```

## Installation

`base64url` doesn't have to be installed; it has no dependencies other than
Python 3.4 or above. Just run it as `path/to/base64url`.

Of course, you can if you wish add it to your PATH.

## Using with Docker

To encode, pipe to:

```
docker run -i --rm simonwhitaker/base64url
```

To decode, pipe to:

```
docker run -i --rm simonwhitaker/base64url -d
```
