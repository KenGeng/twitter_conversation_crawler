import os

import pandas as pd
import time
import numpy as np
import multiprocessing

from subprocess import call



def getConversation(file):
    src_path = './CsvResult_not_done_azure'
    dst_path = './tweetresult'
    id = file[0:len(file) - 4]
    d = pd.read_csv(src_path + '/' + str(id) + '.csv', usecols=['tweetid', 'conversationid'],
                    dtype={'tweetid': object, 'conversationid': object}, keep_default_na=False)
    # print(d)
    flag=0
    for i, row in d.iterrows():
        if row['conversationid'] != "":
            print(row['conversationid'])
            flag=1
            # call(["scrapy", "crawl", "twitter_tree", "-a", "tweet_id="+str( row['conversationid']),"-o", dst_path +'/' + str(id) + '/' + row['conversationid'] + '.csv'])
            os.system('scrapy crawl twitter_tree -a tweet_id="%s" -o %s' % (
            row['conversationid'], dst_path +'/' + str(id) + '/' + row['conversationid'] + '.csv'))
    # para="russian mariia butina oval office"
    # os.system('python ../snopes_tweet/GetOldTweets2/Exporter.py --querysearch "%s" --maxtweets 100  --since "2010-01-01" --output "te4.csv"'% para)

    # os.system('scrapy crawl twitter_tree -a tweet_id="1021007656511852544" -o result.csv')
    # scrapy crawl twitter_tree -a tweet_id="797071274673573888" -o result.csv
    if flag==0:
        os.system('mv "/Users/apple/fakenews/twitter_conversation_crawler/CsvResult_not_done_azure/%s.csv" "/Users/apple/fakenews/twitter_conversation_crawler/CsvDone/%s.csv"'%(str(id) ,str(id) ))
        print(id+"aws")

    print("done.")


# cores = multiprocessing.cpu_count()
# pool = multiprocessing.Pool(processes=cores)
# csv_dir = "./CsvResult2"
# dst_dir = "./tweetresult"
# files = os.listdir(csv_dir)
# length = len(files)
# print(length)
# print(cores)
# pool.map(getConversation, files)  # prints [0, 1, 4, 9, 16]



def run_parallel_selenium_processes(datalist, selenium_func):
    print(len(datalist))
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool()

    # max number of parallel process
    ITERATION_COUNT = 1

    count_per_iteration = len(datalist) / float(ITERATION_COUNT)

    for i in range(0, ITERATION_COUNT):
        list_start = int(count_per_iteration * i)
        list_end = int(count_per_iteration * (i+1))
        print(i)
        # pool.apply_async(selenium_func, )
        pool.map(selenium_func, datalist[list_start:list_end])
    # for file in files:
#     id = file[0:len(file) - 4]
#     getConversation(id, csv_dir, dst_dir)
# print(time.asctime(time.localtime(1532262169)))
    print("GOOOOOOOOOOOOOOOOOOOAL!")


csv_dir = "./CsvResult_not_done_azure"
dst_dir = "./tweetresult"
files = os.listdir(csv_dir)
for file in files:
    getConversation(file)
print(len(files))
print("hello,yecang")
# cores = multiprocessing.cpu_count()
# pool = multiprocessing.Pool(processes=cores-2)
# pool.map(getConversation, files)
# run_parallel_selenium_processes(files,getConversation)