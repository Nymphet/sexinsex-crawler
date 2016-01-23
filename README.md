# sexinsex-content-crawler

A simple python crawler for novels listed on this webpage http://www.sexinsex.net/forum/thread-2507213-1-1.html

Also works for most Discuz! forums. Just change the start url in config file.

# Usage

To crawl public contents only:

    git clone https://github.com/Nymphet/sexinsex-content-crawler.git
    
    cd sexinsex-content-crawler
    
    mkdir html,text
    
    python3 crawler.py
    
    python3 extractor.py
    
Some contents on sexinsex board are only visible after you login, fill in your login credentials in config.py, and then:

    git clone https://github.com/Nymphet/sexinsex-content-crawler.git
    
    cd sexinsex-content-crawler
    
    mkdir html,text
    
    python3 selenium_crawler.py
    
    python3 extractor.py
    
Notice: to use the login function you must have chromedriver and selenium installed and make sure chromedriver is in your path

You can always run check_failure.py before running extractor.py so as to know how much you have successfully crawled from the site. 
