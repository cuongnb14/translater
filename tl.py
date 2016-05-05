#! /usr/bin/env python2

"""
    From https://github.com/terryyin/google-translate-python
"""
from translate import Translator
from sys import argv

def main():
    lang = 'vi'
    if len(argv) == 3:
        lang = argv[2]
    
    translator= Translator(to_lang=lang)
    translation = translator.translate(argv[1])
    print translation

if __name__ == "__main__":
    main()
