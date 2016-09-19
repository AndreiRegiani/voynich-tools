#!/usr/bin/env python3
"""
Generates a HTML document where each word from file_input will be anchored
and set a CSS class. Example:

FILE IN:  hello there
FILE OUT: <a href="/words/hello.html" class="word word-hello">hello</a> <a href="/words/there.html" class="word word-there">there</a>
"""

from sys import argv

BASE_URL = '/voynich/words/'
BASE_CSS = 'word word-'

def main(file_input):
        file_output = 'anchored_' + file_input.replace('.txt', '') + '.html'
        fout = open(file_output, 'w')
        with open(file_input, 'r') as fin:
            for line in fin:
                for word in line.split():
                    html = '<a href="{url}{word}.html" class="{css}{word}">{word}</a> \n'.format(url=BASE_URL, word=word, css=BASE_CSS)
                    fout.write(html)
                fout.write('<br>\n')
        fout.close()
        print("File '{}' generated".format(file_output))


if len(argv) == 2:
    main(argv[1])
else:
    print("Usage: file_input")
