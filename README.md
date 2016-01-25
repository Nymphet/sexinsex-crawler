# sexinsex-content-crawler

A simple python crawler for [sexinsex board](http://www.sexinsex.net)

Also works for most Discuz! forums. Just change the start url in config file.

# Usage
   
Filenames are kind of self-explanatory. 

To download the initial page:

    python3 initializer.py
    
To extract all thread ids in the initial page (extracted thread ids are stored in a list and dumped to a pickle file):

    python3 thread_tids_extractor.py

To download all threads whose ids are stored in the list you just extracted from the initial page (all html files are saved to the html folder):

    python3 selenium_html_downloader.py
    
To extract the main contents of all html files in the html folder (saved to the text folder):    
    
    python3 page_content_extractor.py

To extract attachment ids in all html files in the html folder (extracted attachment ids are stored in a list and dumped to a pickle file):

    python3 page_aids_extractor.py
    
To download all attachments whose ids are stored in the list you just extracted from files in the html folder (attachments are saved to your Downloads folder):

    python3 selenium_attachment_downloader.py
    
Note that you must have selenium and chromedriver installed to run programs that start with "selenium". Most pages and attachments are only available after you login, so you may need to fill in your login credentials in config.py to download them.

# Known bugs

There are a lot of empty .crdownload files generated in your download folder if you run selenium_attachment_downloader.py, but all files actually finished downloading and it's safe to remove these empty .crdownload files. You will not miss any  attachment.
