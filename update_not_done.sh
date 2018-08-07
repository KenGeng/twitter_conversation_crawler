## a shell script for update data situation

##!/usr/bin/env bash
#i=0
#for file in /Users/apple/awsnb/tweetresult/*
#do
#    if test -d $file
#    then
#        len=${#file}
#        name=${file:31:len-31}".csv"
#        echo $name
#        if test -f "/Users/apple/fakenews/twitter_conversation_crawler/CsvResult_not_done_aws/"$name
#        then
#            mv "/Users/apple/fakenews/twitter_conversation_crawler/CsvResult_not_done_aws/"$name "/Users/apple/fakenews/twitter_conversation_crawler/CsvDone/"$name
#        echo $file 移动完成
#        let i+=1;
#        fi
#    fi
#done
#echo "total:"$i


#!/usr/bin/env bash
i=0
for file in /Users/apple/azurenb/tweetresult/*
do
    if test -d $file
    then
        len=${#file}
        name=${file:33:len-33}".csv"
        echo $name
        if test -f "/Users/apple/fakenews/twitter_conversation_crawler/CsvResult_not_done_azure/"$name
        then
            mv "/Users/apple/fakenews/twitter_conversation_crawler/CsvResult_not_done_azure/"$name "/Users/apple/fakenews/twitter_conversation_crawler/CsvDone/"$name
        echo $file 移动完成
        let i+=1;
        fi
    fi
done
echo "total:"$i

##!/usr/bin/env bash
#i=0
#for file in /Users/apple/macnb/tweetresult/*
#do
#    if test -d $file
#    then
#        len=${#file}
#        name=${file:31:len-31}".csv"
#        echo $name
#        if test -f "/Users/apple/fakenews/twitter_conversation_crawler/CsvResult_not_done_mac/"$name
#        then
#            mv "/Users/apple/fakenews/twitter_conversation_crawler/CsvResult_not_done_mac/"$name "/Users/apple/fakenews/twitter_conversation_crawler/CsvDone/"$name
#        echo $file 移动完成
#        let i+=1;
#        fi
#    fi
#done
#echo "total:"$i