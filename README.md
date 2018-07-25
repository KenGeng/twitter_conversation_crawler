# twitter_conversation_crawler
a python crawler for getting the whole conversation of a tweet by conversation id.



# Tools
Firefox python 3.6 and following packages:
1. scrapy 
2. selenium


# Usage
1. Install latest firefox browser
2. Download geckodriver executive file from https://github.com/mozilla/geckodriver/releases
3. Install the dependencies:
``pip install -r requirements.txt``
4. Set geckodriver path in twitter_tree.py like this: self.driver = webdriver.Firefox(executable_path='/Users/apple/Downloads/geckodriver')
5. run code

``scrapy crawl twitter_tree -a tweet_id="1021007656511852544" -o result.csv
``
