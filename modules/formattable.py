from modules.ftools import *

module = {
    'name': 'Formatting Table',
    'version': '0.1',
    'author': 'Filip9696',
    'description': 'Shows all formatting on load',
    'functions': {}
}

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


def onLoad():
    print_format_table()