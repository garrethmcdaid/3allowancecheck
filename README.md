# 3allowancecheck
Python script that checks your mobile data allowance in 3 Mobile

Why you might need this:

http://www.nightbluefruit.com/blog/2017/07/breaking-up-3s-mobile-broadband-scam/

# Requirements

You will need:

**Python 2.7**

**Selenium**

sudo pip install selenium

**PhantomJS**

http://phantomjs.org/download.html

(Ensure you have correct version for your OS)

# How to monitor

Execute the script via Crond and publish the output to a file on a web server somewhere.

Then, install the following Android app:

https://play.google.com/store/apps/details?id=net.ayukawayen.infotracker&hl=en

This app lets you monitor the content of a URL. If will alert when the content changes.

There are probably similar apps for iPhone.



