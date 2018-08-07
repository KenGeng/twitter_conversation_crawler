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
sudo apt-get install python-pip python-dev python-virtualenv # for Python 2.7
virtualenv --system-site-packages -p python3 targetDirectory # set python3 interpreter for virtualenv
source ~/targetDirectory/bin/activate # bash, sh, ksh, or zsh
3. install firefox and xvfb https://medium.com/@griggheo/running-selenium-webdriver-tests-using-firefox-headless-mode-on-ubuntu-d32500bb6af2
sudo apt-get install firefox xvfb
Xvfb :10 -ac &
export DISPLAY=:10 or：sudo -H vi /etc/environment  add DISPLAY=:10  then source /etc/environment or restart terminal
run `firefox` to test.
4. install dependency: pandas/scrapy etc. In this process, you may suffer from lots of version problem. Use google and stackoverflow and I'm sure you can get over them.
Problem example:
````
OSError: Command /home/ubuntu/fakenews/bin/python3 - setuptools pkg_resources pip wheel failed with error code 1： https://github.com/certbot/certbot/issues/2883 
Solution:export LC_ALL="en_US.UTF-8" export LC_CTYPE="en_US.UTF-8"
````
5. python run.py

6. tip for connecting a server: 
connect：ssh -p 22  Server@xxx.xxx.xxx.xxx 
copy from server：scp -P 22 -r Server@xxx.xxx.xxx.xxx:~/twitter_conversation_crawler/tweetresult ~/result 
copy to server: scp -P 22 -r ~/project_dir  Server@xxx.xxx.xxx.xxx:~/twitter_conversation_crawler/tweetresult 
background running：nohup python run.py > my_output.log & 
check running state: tail -f my_output.log
