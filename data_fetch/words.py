#! /usr/bin/env python
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch list of words from URL"""
    data = urlopen(url)
    data_box = []
    for bytes in data:
        bytes_text = bytes.decode('utf8').split()
        for text in bytes_text:
                data_box.append(text)
    data.close()
    return data_box


def print_items(items):
    for item in items:
        print(item)

def main():
    url = input()
    words = fetch_words(url)
    print_items(words)

            
if __name__ == '__main__': # take arg from command line
    main()
#   main(sys.argv[1])
