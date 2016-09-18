#!/usr/bin/env python3
"""
Works for this transcription extractor tool: 
http://voynich.freie-literatur.de/index.php?show=extractor

This script makes the transcription file more readable for humans
and more friendly to be parsed by modern programming languages like Python

Example:

FILE IN:  fachys.ykal.ar.ataiin.Shol.Shory.cTh!res.y.kor.Sholdy!-
FILE OUT: fachys ykal ar ataiin Shol Shory cThres y kor Sholdy  
"""

from sys import argv


def main(file_input):
        file_output = "clean_" + file_input

        fout = open(file_output, 'w')
        with open(file_input, 'r') as fin:
            for line in fin:
                line = line.replace('!', '')  # null-character
                line = line.replace('.', ' ')  # word separator
                line = line.replace('-', ' ')  # end of line
                line = line.replace('=', '\n\n')  # end of paragraph
                fout.write(line)
        fout.close()
        print("File '{}' generated".format(file_output))


if len(argv) == 2:
    main(argv[1])
else:
    print("Usage: input_file")

