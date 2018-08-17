# usage: scrapy crawl twitter_tree -a tweet_id="1021007656511852544" -o result.csv
# this version is collect simplified information


import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import WebDriverException

class TwitterTree(scrapy.Spider):
    def __init__(self,
                 tweet_id=None):
        self.start_urls = ["https://twitter.com/statuses/%s" % tweet_id]
        # remember to set the path of 'geckodriver'


    # https://twitter.com/realDonaldTrump/status/1021007656511852544
    name = 'twitter_tree'

    def parse(self, response):
        try:

            self.driver = webdriver.Firefox(
                    # executable_path='/usr/local/bin/geckodriver')
                    executable_path='/Users/apple/fakenews/twitter_conversation_crawler/ff_geckodriver_mac/geckodriver')
            # executable_path = '/usr/local/bin/geckodriver'
            self.driver.get(response.url)


            page = self.driver.find_element_by_tag_name('body')

            # you can modify following number to make selenium get more tweets from the page
            for i in range(50):
                page.send_keys(Keys.PAGE_DOWN)
                # simulate human operation
                time.sleep(0.4)

            # time.sleep(2)

            # for conversation in response.css(CONVERSATION_SELECTOR).extract_first()
            count = 0
            hxs = Selector(text=self.driver.page_source)
            # get the info of original tweet user
            owner_content = hxs.css('div.permalink-inner.permalink-tweet-container').css('.TweetTextSize ::text').extract()
            owner_name = hxs.css('.permalink-header').css('.username').css('b ::text').extract_first()
            owner_link = 'https://twitter.com' + hxs.css('.permalink-inner').css('div ::attr(data-permalink-path)').extract_first()
            owner_time= hxs.css('.permalink-header').css('.time').css('span ::attr(data-time)').extract_first()
            yield {
                'content': owner_content,
                'username': owner_name,
                'replyto': '',
                # response.css('span[property="city"]::text')
                'permalink': owner_link,
                'time': owner_time
            }
            # traversal tweet conversations
            for conversation in hxs.css('.ThreadedConversation') :
                for tweets in conversation.css('.ThreadedConversation-tweet'):
                    count += 1
                    yield {
                        'content': tweets.css('.content').css('.js-tweet-text-container').css('.TweetTextSize ::text').extract(),
                        'username': tweets.css('.content').css('.stream-item-header').css('.username').css('b ::text').extract_first(),
                        'replyto': tweets.css('.content').css('.ReplyingToContextBelowAuthor').css('.username').css('b ::text').extract(),
                        # response.css('span[property="city"]::text')
                        'permalink': 'https://twitter.com' + tweets.css('div ::attr(data-permalink-path)').extract_first(),
                        'time': tweets.css('.content').css('.stream-item-header').css('.time').css(
                            'span ::attr(data-time)').extract_first()
                    }

            # traversal lone tweet

            for conv_lone in hxs.css('.ThreadedConversation--loneTweet'):
                count += 1
                yield {
                    'content':  conv_lone.css('.content').css('.js-tweet-text-container').css('.TweetTextSize ::text').extract(),
                    'username': conv_lone.css('.content').css('.username').css('b ::text').extract_first(),
                    'replyto': conv_lone.css('.content').css('.ReplyingToContextBelowAuthor').css('.username').css(
                        'b ::text').extract(),
                    'permalink': 'https://twitter.com' + conv_lone.css('div ::attr(data-permalink-path)').extract_first(),
                    'time': conv_lone.css('.content').css('.stream-item-header').css('.time').css('span ::attr(data-time)').extract_first()
                }

            print("count=" + str(count))
            self.driver.close()
            self.driver.quit()
            # quit browser
        except Exception as e:
            print("error happen:",e)
            # self.driver.close()
            # self.driver.quit()
            print("quit browse success.")
        try:
            self.driver.title
            self.driver.quit()
            print(True)
        except WebDriverException:
            print(False)

        # input("Press Enter to continue...")
        print("Done!")

