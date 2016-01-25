# -*- coding: utf-8 -*-

from urllib import request, parse, error
from time import sleep
import re, pickle

from config import start_tid, URLS_PREFIX, encoding, path, sleeptime
from utils import generate_thread_url

class thread():

    def __init__(self,tid):
        self.tid = tid
        self.extracted_pids = []
        self.url = generate_thread_url(self.tid, 1)

    # extract all pages in a thread, used to extract contents not in the first page
    def extract_pids(self):
        with open('%s/html/%s'%(path,parse.quote_plus(self.url)), 'r') as f:
            p = re.compile(r'''<div class="pages">.*<a href=".*" class="last">(.*)</a>.*</div>''')
            for line in f.readlines():
                n = p.search(line)
                if n:
                    self.extracted_pids = list(range(1,int(n.group(1))+1))
                    break

class page():

    def __init__(self,tid,pid):
        self.tid = tid
        self.pid = pid
        self.extracted_tids = []
        self.url = generate_thread_url(self.tid,self.pid)

    # extract all refered tids in this page
    def extract_tids(self):
        with open('%s/html/%s'%(path,parse.quote_plus(self.url)), 'r') as f:
            p = re.compile(r'''<a href="thread-(\d*)-\d*-\d*.html"''')
            for line in f.readlines():
                n = p.search(line)
                if n:
                    self.extracted_tids.append(n.group(1))

def main():

    print('Extracting tids from the page')
    start_page = page(start_tid,1)
    start_page.extract_tids()

    print('Extracted tids:')
    print(start_page.extracted_tids)

    print('Saving extracted tids to pickle/tids_from_thread_%s.p'%start_tid)
    with open('%s/pickle/tids_from_thread_%s.p'%(path,start_tid),'wb') as p:
        pickle.dump(start_page.extracted_tids,p)

if __name__ == '__main__':
    main()
