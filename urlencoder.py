#!/usr/bin/env python3

import urllib.parse

input_file_path = 'input.txt'
output_file_path = 'output.txt'

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        encoded_line = urllib.parse.quote(line.strip())
        output_file.write(encoded_line + '\n')
