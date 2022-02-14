#!/usr/bin/python

import sys
import pprint
import json


if len(sys.argv) > 1:
    w = sys.argv[1].upper()
else:
    w = '?????'

if len(sys.argv) > 3:
    x=list(sys.argv[3] or '')
else:
    x=None

if len(sys.argv) > 2:
    z=(sys.argv[2] or '').split(',')
else:
    z=['?????']


def find_prob(word):
    sum = 0

    for i in range(32):
         bin_str = format(i,'05b')
         prod1 = 1
         prod2 = 0
         for index, k in enumerate(list(bin_str)):
            j = word[index]
            for i in range(5):
                prod1 = prod1 * (1 - s1[i].get(j,0))
        
            for i in range(5):
                #prod2 = prod2 + (s1[i].get(j,0)*prod1/(1-s1[i].get(j,0)))
                prod2 = prod2 + s1[i].get(j,0)

            sum  = sum + fin.get(j,0)*prod2#*int(k)
    sum = float("%.6f" %sum)
    return sum

try:
    json_file = open("dataset","r")
except:
    json_file = None

if json_file is None:

    f = open("wordlist", "r")
    l = f.read().strip('\n')
    arr = l.split(" ")
    f1 = open("solution", "r")
    l1 = f1.read().strip('\n')
    arr1 = l1.split(" ")
    fin = {}
    count = len(arr1)
    for i in arr1:
        t = {}
        ws = []
        ws[:0] = i.strip('\n')
        for j in ws:
            if j=='\n':
                continue
            if t.get(j) is None:
                t[j] = 1
                fin[j] = fin.get(j,0) + 1

    s1=[{},{},{},{},{}]
    for i in arr1:
        t = {}
        ws = []
        ws[:0] = i.strip('\n')
        for index, j in enumerate(ws):
            if j=='\n':
                continue
            s1[index][j] = s1[index].get(j,0)+1


    for index, i in enumerate(s1):
        for j in s1[index].items():
            s1[index][j[0]] = float("%.5f" %((1*s1[index].get(j[0],0))/(count)))

    for i,j in fin.items():
        fin[i] = float("%.5f" %((1*fin.get(i,0))/(count)))

    #pprint.pprint(fin)
    #pprint.pprint(s1)

    words={}
    unique={}
    for i in arr:
        t={}
        ws = []
        ws[:0] = i
        sum = 0
        is_unique = True
        for index, j in enumerate(ws):
            if j=='\n':
                continue
            if t.get(j) is None:
                t[j] = 1;
            else:
                is_unique = False
        sum = find_prob(i)
        words[i] = sum
        if is_unique == True:
            unique[i] = sum

    final_data = {"words":words,"unique":unique}
    with open("dataset" , "w") as outfile:
        json.dump(final_data,outfile)


else:
    final_data = json.loads(json_file.read())
    words = final_data['words']
    unique = final_data['unique']




def find_string (words):
    newlist = {}
    for i in words.items():
        wd = i[0]
        match = True
        for j in range(5):
            if x is not None and wd[j] in x:
                match = False
            if w[j] == '?':
                continue
            if w[j] != wd[j]:
                match = False
        for j in z:
            for k in range(5):
                if j[k] == wd[k]:
                    match = False
            for l in list(j):
                if l=='?':
                    continue
                if not l in wd:
                    match = False
        if match == True:
            newlist[wd]  = i[1]

    newlist = dict(sorted(newlist.items(), key=lambda item: item[1], reverse=True))
    print('--'*80)
    print('Top match: ', list(newlist.items())[:15])
    print('Bot match: ', list(newlist.items())[-15:])
    print('--'*80)

print('')
print('Matches::')
find_string(words)
print('')
print('Unique Matches::')
find_string(unique)
