# -*- coding: utf-8 -*-

''' Used to extract the main contents of html files saved in ./html folder.
    Extracted contents are saved in ./text folder. '''

from urllib import parse
import os, re

path = os.path.abspath('.')

title = re.compile(r'''<title>(.*)</title>''')
contentline = re.compile(r'''(.*)<br />''')

failcnt = 0

def fuck(s):
    l = []
    for c in s:
        if c in r'''!@#$%^&*()+={}|[]\\:";'<>?,./【】：；‘’“”《》？／。，！@＃¥％……&＊（）——＋－＝｜、［］｛｝''':
            pass
        else:
            l.append(c)
    return ''.join(l)

for htmlfile in os.listdir('%s/html/'%path):
    with open('%s/html/%s'%(path,htmlfile),'r',errors='ignore') as f:
        print('Extracting from',parse.unquote_plus(htmlfile))
        flag = True
        lines = f.readlines()

        for line in lines:
            p = re.search('<title> SexInSex! Board </title>', line)
            if p:
                flag = False
                print('Failed to extract from',parse.unquote_plus(htmlfile))
                failcnt += 1
                break

        if flag:
            for line in lines:
                h = title.search(line)
                if h:
                    tt = fuck(h.group(1))
                    break
            print('Filename:', tt)
            for line in lines:
                p = contentline.search(line)
                if p:
                    with open('%s/text/%s.txt'%(path,tt),'a') as t:
                        t.write(p.group(1)+'\n')
            print('OK')

print('Finished. %d files failed to extract.'%(failcnt))
