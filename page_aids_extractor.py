# -*- coding: utf-8 -*-

''' Used to extract attachment ids from html files in ./html folder.
    Extracted ids are saved in ./pickle folder'''


from urllib import parse
import os, re, pickle

from config import path

attachment = re.compile(r'''<a href="attachment\.php\?aid=(\d+)" target="_blank">''')

failcnt = 0
aids_list = []

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
                a = attachment.search(line)
                if a:
                    aids_list.append(a.group(1))
            print('OK')

s_aids_list = list(set(aids_list))
print(s_aids_list)
print('%d attachment ids found'%len(s_aids_list))
print('saving attachment ids to pickle/aids_list.p')
with open('%s/pickle/aids_list.p'%path,'wb') as a:
    pickle.dump(s_aids_list, a)

print('Finished. %d files failed to extract.'%(failcnt))
