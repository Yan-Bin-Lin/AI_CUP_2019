'''
Created on 2019年4月27日

@author: danny
'''
import csv
import threading
import requests
import asyncio
import gc
import time

#init
title = ''
threadlist = list()
asylist = list()

#get html
async def send_req(loop, url):
    res = ''
    try:
        res = await loop.run_in_executor(None,requests.get,url)
    except:
        #url of some apple
        url = 'https://tw.appledaily.com' + url
        try:
            res=  await loop.run_in_executor(None,requests.get,url)
        except:
            print('error:\n' + url)
            return 'error'
    return res.text
    
#Coroutine
async def main(loop, data, num):
    for row in data:
        #await for request I/O
        task = await loop.create_task(send_req(loop, row[1]))
        row.append(task)
        #release memory
        del task
        gc.collect()
    #insert csv title
    data.insert(0, title)
    #write for csv format, use '~' for quote
    with open('D:/文本分析資料/NC_1(' + str(num) + ').csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile,  quoting=csv.QUOTE_ALL, quotechar = '~')
        writer.writerows(data)
        
#thread
def newscontent(data, num):
    #new coroutine
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    #set and run Coroutine
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main(event_loop, data, num))
    

for num in range(10, 100):
    #read csv file
    with open('D:/文本分析資料/NC_1(' + str(num) + ').csv', newline='') as csvfile:
        rows = list(csv.reader(csvfile, delimiter=','))
        #get title
        title = rows.pop(0)
        #multy thread
        threadlist.append(threading.Thread(target = newscontent, args = (rows, num,)))
        threadlist[num - 10].start()
    #sleep to save my memory QQ
    time.sleep(120)