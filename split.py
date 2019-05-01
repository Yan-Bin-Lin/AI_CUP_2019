'''
Created on 2019年4月28日

@author: danny
'''

import csv

with open('C:/Users/danny/Desktop/文本分析深度學習/競賽/powershell/NC_1.csv', newline='') as csvfile:
    rows = list(csv.reader(csvfile, delimiter=','))
    title = rows.pop(0)
    title.append('News_Content')
    l = len(rows) // 1000
    for i in range(l):
        tmp = rows[i * 1000:(i+1) * 1000]
        tmp.insert(0, title)
        with open('D:/文本分析資料/NC_1(' + str(i) + ').csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(tmp)