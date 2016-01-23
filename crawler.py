# -*- coding: utf-8 -*-

from urllib import request, parse, error
from time import sleep
import re, os

from config import start_tid, URLS_PREFIX, encoding, path, sleeptime

def generate_url(tid,pid=1):
    return ''.join([URLS_PREFIX, 'thread-', str(tid), '-', str(pid), '-1.html'])

def download(url):
    r = request.Request(url)
    r.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
    with request.urlopen(r) as f:
        with open('%s/html/%s'%(path,parse.quote_plus(url)), 'w') as s:
            s.write(f.read().decode(encoding=encoding,errors='ignore'))

class thread():

    def __init__(self,tid):
        self.tid = tid
        self.extracted_pids = []
        self.url = generate_url(self.tid, 1)

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
        self.url = generate_url(self.tid,self.pid)

    # extract all refered tids in this page
    def extract_tids(self):
        with open('%s/html/%s'%(path,parse.quote_plus(self.url)), 'r') as f:
            p = re.compile(r'''<a href="thread-(\d*)-\d*-\d*.html"''')
            for line in f.readlines():
                n = p.search(line)
                if n:
                    self.extracted_tids.append(n.group(1))

def main():

    print('Downloading the first page...')
    download(generate_url(start_tid,1))

    print('OK. Extracting tids from the page')
    start_page = page(start_tid,1)
    start_page.extract_tids()

    print('Extracted tids:')
    print(start_page.extracted_tids)

    for tid in start_page.extracted_tids:
        try:
            if sleeptime:
                print('sleeping...')
                sleep(sleeptime)
            print('downloading:',tid)
            download(generate_url(tid,1))
        except error.HTTPError:
            print('HTTPError')

if __name__ == '__main__':
    main()
