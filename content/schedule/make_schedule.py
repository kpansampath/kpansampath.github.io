# author: Kannappan Sampath
# about: generate an html file with calendar
# usage:
#      `python <this file> <schedule.data> <name_of_outfile.html>`
#
# data -> html conventions
#      '_' -> ' '
#

import random
from sys import argv
in_name, out_name = argv[1:3]

with open(in_name) as f:
    lines = list()[1:]

def prettifycell(token):
    color, text = token[0], token[1:].replace('_'. ' ')
    bgcolor, fgcolor, style = {
        }[color]
    return '\n <td bgcolor="%s" style="color:%s,%s" rowspan=\"%d\">%s</td>' % (bgcolor, fgcolor, style, height, text)

def print_line(line):


def print_table(lines):


with open('schedule_table_template.html') as f:
    text = f.read()

with open(out_name, 'w') as f:
    f.write(text.replace('TABLE', print_table(lines)))
