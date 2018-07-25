# twitter_conversation_crawler
a python crawler for getting the whole conversation of a tweet by conversation id.



# Tools
python 3.6 and following packages:
1. scrapy 
2. selenium

# Usage
1. Install the dependencies:
``pip install -r requirements.txt``
2. run code

``scrapy crawl twitter_tree -a tweet_id="1021007656511852544" -o result.csv
``
