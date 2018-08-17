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
# Run code on a server
1. get a server from AWS/AZURE/Vultr...
2. install virtualenv:
```python
sudo apt-get install python-pip python-dev python-virtualenv # for Python 2.7
virtualenv --system-site-packages -p python3 targetDirectory # set python3 interpreter for virtualenv
source ~/targetDirectory/bin/activate # bash, sh, ksh, or zsh
```

3. install firefox and xvfb (referenced from https://medium.com/@griggheo/running-selenium-webdriver-tests-using-firefox-headless-mode-on-ubuntu-d32500bb6af2)
```
sudo apt-get install firefox xvfb
Xvfb :10 -ac &
export DISPLAY=:10 # or：sudo -H vi /etc/environment  add DISPLAY=:10  then source /etc/environment or restart terminal
```
run `firefox` to test if it works well.

4. install dependency: pandas/scrapy etc. In this process, you may suffer from lots of version problem. Use google and stackoverflow and I'm sure you can get over them.If not, please start a issue. I will try to help you.
Problem example:
````
OSError: Command /home/ubuntu/fakenews/bin/python3 - setuptools pkg_resources pip wheel failed with error code 1： https://github.com/certbot/certbot/issues/2883 
Solution:export LC_ALL="en_US.UTF-8" export LC_CTYPE="en_US.UTF-8"
````
5. run code:
```python
python run.py
```

6. tip for background running：\
nohup python run.py > my_output.log & \
check running state: tail -f my_output.log

# Other Detail
In fact, when deployed on a server, such spider should work in multi thread to accelerate. However, after I tried many parallel method from stackoverflow, I found that those methods could work well in the first few hours but failed when program ran for a longer time. 
After inspecting the running state of each server, I guess the reason might be that the running scrapy and firefox will use too much CPU, which leads to the server to stop for protection. So, finally I make it a single thread version. If you have better solution, please let me know in the issue. Thanks a lot~ 
