# -*- coding: utf-8 -*-

''' Used to initialize the program.
    You will need to run this program once after you changed the settings in config.py'''

import os

from functions import download_html, generate_thread_url
from config import start_tid

def create_directory(d):
    if not os.path.exists(d):
        os.mkdir(d)

def download_first_page():
    print('Downloading the first page...')
    download_html(generate_thread_url(start_tid,1))

def main():
    create_directory('html')
    create_directory('text')
    create_directory('pickle')
    create_directory('attachment')

    download_first_page()


if __name__ == '__main__':
    main()
