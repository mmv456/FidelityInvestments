
########################################################################
#                                CONTENT                               #
#                                                                      #
# Part 1: README                                                       #
#           -read this first                                           #
# Part 2: INSTRUCTIONS                                                 #
#           -setting up your program to run on your computer and set   #
#            up your preferences                                       #
# Part 3: FREQUENTLY ASKED QUESTIONS                                   #
# Part 4: LIBRARIES                                                    #
#           -packages that help make the code cleaner                  #
# Part 5: USER INPUT                                                   #
#           -add/change emails, key words, and news sources            #
#           -any user input should only be made in this section        #
# Part 6: UTILITY FUNCTIONS                                            #
#           -help with the email functions, nothing much to look at    #
# Part 7: EMAIL FUNCTIONS                                              #
#           -collect news articles and set up html table to send email #
# Part 8: main()                                                       #
#           -the function that runs the whole code                     #
#                                                                      #
########################################################################




#--------------------------------------------------------------------------
#---------------------------------PART 1-----------------------------------
#---------------------------------README-----------------------------------


"""
This is a News Feed program, designed to take in your preferences for news
sources and key words to look out for and give you emails containing those
articles.

Created using Python 3.


*** Before you start reading the Instructions, make your you have Python 3
installed on your computer. This python program will only run if you have that.
If you don't, install the latest version at https://www.python.org/downloads/
If you can't install (you don't have space, you don't have permission, etc.),
then ask someone else who has python on their computer to run this file for you.

Created by Mahitha Valluru during her internship here at Fidelity on 8/9/2018.
mahitha.valluru@gmail.com
https://github.com/mmv456
"""


#--------------------------------------------------------------------------
#---------------------------------PART 2-----------------------------------
#------------------------------INSTRUCTIONS--------------------------------

"""
1.  If you received this Python file to create your own news feed, then the
    first thing you want to do is rename this file whatever you like and
    place it in a folder that you will remember it is in.
2.  Also, create a .txt file IN THE SAME FOLDER you saved this Python file
    in and name it whatever you like. It is recommended that you name it
    the same as whatever you named this Python file so that the two files
    will be right next to each other when you open the folder, but it's your
    choice. If you want to know what the purpose of this .txt file is, read
    the FAQs in part 3.
3.  Read the FAQs in Part 3. Just do it, it'll clear up some questions you may
    have before starting the steps below.
4.  Look through Part 5: User Input and understand what the code means.
5.  Once you read the FAQs and understand the code in Part 5 a little bit,
    feel free to change/add key words, news sources, and emails.
6.  Make sure you change the .txt file to whatever you renamed it to.
7.  Look over all of the changes you made one more time, making sure you kept
    the format of the inputs.
8.  Once you think it's ready to run, go back to your folder where you saved
    your Python file and your .txt file.
9.  Create a new .txt file and rename it to whatever you like. However, when
    you rename it, select the .txt part and change it to .bat
    For example, if I created a new .txt file it would look like this:
          New Text Document.txt
    Now, change it so that the "New Text Document" is whatever you like (can
    be the same as the name of this Python file), AND the ".txt" part is
    changed to ".bat", so now it becomes:
          mmv.bat
10. Hit enter, and a window will pop up asking you if you're sure you want to
    change it to a .bat file, just click yes or continue.
11. Now right click the .bat file you just made and click "Edit". It should
    open to a notepad file.
12. Without any spaces, copy this line: python XXXX.py
13. Replace the Xs with the name of your python file.
14. Save the file and close it.
15. Now click on the .bat file in your folder and it will open the command
    prompt (a program with a black background). Let it run and once you get
    email you can close it.
16. Whenever you want to run the program, you can either just click on the
    .bat file or set up Windows Task Scheduler to make the .bat file
    run periodically.
"""


#--------------------------------------------------------------------------
#---------------------------------PART 3-----------------------------------
#-----------------------FREQUENTLY ASKED QUESTIONS-------------------------
"""
Disclaimer: I didn't actually receive any questions and am just assuming
            questions that may be asked. Feel free to contact me with any
            that you have at mahitha.valluru@gmail.com

What do you mean by "relevant" articles?
-> Relevant articles are those with headlines that match certain key words
   provided by the user. See Part 5: User Input below to add or modify the
   current list of key words.

What are the various news sources?
-> The news sources, similar to key words, are given by user input. Some are
   chosen by default, but you are free to add or remove any that you like in 
   Part 5: User Input.
   Keep in mind that you must follow the format that it is in with commas
   separating each news source. Failure to do so will result in the code not
   working.

Can I send to multiple people?
-> Sure, you can either forward the email that you get to anyone you like, or
   add their emails to the sender list in Part 5: User Input with a comma
   and a space separating each email.

Can I change the to and from emails currently in place?
-> Yes.

Can I make modifications to the code?
-> Sure, just make sure you know what changes you're making and just in case,
   make a copy of this code if you want to go back. Also, I made comments
   for almost all of the functions so you have an idea of what they do. If you
   change anything, add/edit these comments so you know what changes you did.

What is the .txt file that I need?
-> The .txt file (just a notepad file) is for holding all of the past relevant
   articles that you've already received in an email. Every time you get an
   email, these articles are added to this file so that you won't get repeats.
   If you have this Python code, you should also create a .txt file IN THE
   SAME PLACE that this Python file is saved in so that you will get this
   functionality, or else you will get repeat articles. Name it whatever you
   like (preferably the same name as this Python file so you see them together
   in the folder).
   When you name the .txt file, you will also have to go to Part 5: User Input
   in this code and locate the variable named "txtfile". It will already have
   some name in it like "____.txt". Go ahead and change that to the .txt file
   that you named it.

There are a lot of instructions...
-> This program is based on a lot of user preferences, so it will take some
   time on your part to look over the User Input part and see what you want
   to add or remove.
   Other than that, there's about 10 steps on your part to get the program
   to run. It should take anywhere from 2-10 minutes to complete the rest of the
   steps after step 5.

I tried setting up Windows Task Scheduler but it's giving me an error.
-> If it's saying something about needing to be an administrator to perform
   this action, then that means you have to be an administrator. You can try
   contacting the appropriate tech people, but I tried and they said they
   can't do it. You can try it again, though, maybe you'll have more luck
   than I did.
   Other than that, you can try downloading other task schedulers online, but
   it's all based on the security level that Fidelity has.
   The other alternative is just to run the .bat program as often as you want
   to get emails. It's not ideal, and you might forget to run it the same time
   every x number of days, but that's the alternative that I could think of.

I have a Mac or am running an iOS device or am using Linux/Ubuntu
-> I am not familiar with those devices, so try searching online for the
   appropriate formats. Most likely, you should be able to create .txt files
   and maybe .bat files.
   I am confident that there is a form of command prompt on all of those, but
   there will be separate Task Scheduler programs. Look online for the
   appropirate names for each or download one from the Internet.

I ran the .bat file and I didn't get an email.
-> Wait a couple minutes, if you haven't received an email after like 3
   minutes that most probably means there haven't been any new emails since
   the last time you ran it.
   Another option is to see if the code is not right. It most likely should
   be, but check twice to see if everything has the same format.
   Ask the person who gave you this code to send it again so you can check
   for any differences.

I think I messed up the steps in the Instructions. Who do I go to for help?
-> You can either go to the person who gave you this code for help setting it
   up or email mahitha.valluru@gmail.com.
"""


#--------------------------------------------------------------------------
#---------------------------------PART 4-----------------------------------
#--------------------------------LIBRARIES---------------------------------

import feedparser
import datetime
from dateutil import parser, tz
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time, os
from urllib.parse import urlparse


#--------------------------------------------------------------------------
#---------------------------------PART 5-----------------------------------
#-------------------------------USER INPUT---------------------------------

me = "mahitha.valluru@fmr.com"
# add as many emails as you like to the sender list, with a comma and space
# between each
you = ["kenneth.campbell@fmr.com"]


# KEY WORDS
# add as many as you like, with commas between each word covered in quotes
key_words = ['ia act', 'no action letter', 'sec', 'fine', 'adr', 'regulation',
             'regulations', 'fee', 'fees', 'managed account', 'managed accounts',
             'investment adviser','investment advisers','investment advisor',
             'investment advisors','execution quality', 'best ex', 'fraud',
             'volatile', 'volatility', 'lower', 'rise']

# NEWS SOURCES
# add as many as you like, with commas between each and in this format:
# 'NEWS SOURCE NAME (whatever name you like)': 'RSS LINK'
headlines = {'SEC': 'https://www.sec.gov/news/pressreleases.rss',
        'Associated Press': 'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a96b4ad082fe88aa0db04305',
        'Google': 'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US',
        'Yahoo': 'http://news.yahoo.com/rss/',
        'WSJ Markets': 'http://www.wsj.com/xml/rss/3_7031.xml',
        'WSJ Business': 'http://www.wsj.com/xml/rss/3_7014.xml',
        'CNBC Finance': 'https://www.cnbc.com/id/10000664/device/rss/rss.html',
        'CNBC Economy': 'https://www.cnbc.com/id/20910258/device/rss/rss.html',
        'CNBC Business': 'https://www.cnbc.com/id/10001147/device/rss/rss.html',
        'CNBC US': 'https://www.cnbc.com/id/15837362/device/rss/rss.html',
        'CNBC World': 'https://www.cnbc.com/id/100727362/device/rss/rss.html',
        'CNBC Politics': 'https://www.cnbc.com/id/10000113/device/rss/rss.html',
        'Reddit News': 'https://www.reddit.com/r/news/.rss',
        'Nasdaq Markets': 'http://articlefeeds.nasdaq.com/nasdaq/categories?category=US+Markets',
        'marketwatch': 'http://feeds.marketwatch.com/marketwatch/marketpulse/',
        'USNews': 'https://www.usnews.com/rss/news',
        'USA Today': 'http://rssfeeds.usatoday.com/usatoday-NewsTopStories',
        'Business Insider': 'http://markets.businessinsider.com/rss/news'
        }


# do not alter this, unless you are renaming the .txt file
txtfile = 'NewsN.txt'


#--------------------------------------------------------------------------
#---------------------------------PART 6-----------------------------------
#-----------------------------UTILITY FUNCTIONS----------------------------


# try not to change anything here, please



# parses the general news source url to get to the information contained
# in the RSS feed
def parseRSS(url):
    
    return feedparser.parse(url)


# given the url of the news source, use the parseRSS function above to
# get the RSS info, then extract the title and link information from
# each article
def extractInfo(url):

    headlines = []

    feed = parseRSS(url)
    for newsitem in feed['items']:
        titlelist = []

            
        titlelist.append(newsitem['title'].encode("utf-8"))
        titlelist.append(newsitem['link'].encode("utf-8"))


        headlines.append(titlelist)

    return headlines



# this gets the individual articles from each RSS feed
def parseURLS(listOfURLS):

    allHeadlines = []
    
    for key,url in listOfURLS.items():
        allHeadlines.extend(extractInfo(url))


    return allHeadlines

# goes through the headlines and sees whether they have one or more keywords
# in them
def keywordIdentifier(listofAllNews):
    keyword_headlines = []
    
    for headline in listofAllNews:
        split = str(headline[0])[2:][:-1].split("\\s+")

        for word in key_words:
            if word in split[0].lower().split():
                keyword_headlines.append(headline)


    return keyword_headlines

# makes sure the link is not already in the .txt file
# if it's in there that means it's already seen and shouldn't be included
def newNewsIdentifier(listofKeywordHeadlines):

    newHeadlines = []

    f = open(txtfile, 'r', encoding = "latin-1")
    urls = f.readlines()
    urls = [url.strip() for url in urls] # remove the \n character
    f.close

    for headline in listofKeywordHeadlines:
        link = headline[1].decode('utf-8')
        if link not in urls:
            newHeadlines.append(headline)

        
    return newHeadlines


# gets the name of the news source to be put in the html table
def getNewsSource(url):
    site = urlparse(url).netloc
    site = site.replace("www.", "")
    site = site[:-4]

    return site
    


#--------------------------------------------------------------------------
#---------------------------------PART 7-----------------------------------
#----------------------------EMAIL FUNCTIONS-------------------------------



# creates the html table and puts all the news articles in the table
# also sets up the email (the "to", "from", "subject")
def send():
    
    FinalHeadlines = newNewsIdentifier(keywordIdentifier(parseURLS(headlines)))

    if len(FinalHeadlines) != 0:
        html = """\
               <html>
               <head><title>SAI Risk and Oversight WSJ RSS Alerts</title></head>
               <body>
               <p><b>Related articles for the day:</b></p>
               <table border=1>
               """

        for headline in FinalHeadlines:
            html = html + "<tr><td>" + str(FinalHeadlines.index(headline) + 1) + "</td>"
            html = html + "<td>" + getNewsSource(headline[1].decode('utf-8')) + "</td>"
            html = html + "<td><a target = '_new' href = " + headline[1].decode('utf-8') + ">" + str(headline[0])[2:-1] + "</a></td></tr>"


        html = html + "</table></body></html>"

    

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Articles for the day"
        msg['From'] = me
        msg['To'] = ", ".join(you)

        part1 = MIMEText("hello", 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        s = smtplib.SMTP('smtp.fmr.com')

        s.sendmail(me, you, msg.as_string())



# Updates the .txt file to contain all of the news sources so there are no
# future repeats
def TxtUpdate():
    f = open(txtfile, 'r', encoding = "latin-1")
    urls = f.readlines()
    urls = [url.strip() for url in urls] # remove the \n character
    f.close

    FinalHeadlines = newNewsIdentifier(keywordIdentifier(parseURLS(headlines)))

        
    for headline in FinalHeadlines:
        link = headline[1].decode('utf-8')
        if link not in urls:
            n = (headline[1].decode('utf-8'))

            with open(txtfile, 'a') as f:
                f.write('{}\n'.format(n))




#--------------------------------------------------------------------------
#---------------------------------PART 8-----------------------------------
#---------------------------------main()-----------------------------------


# this does the actual sending stuff
def main():
    # calls the send email function
    send()
    # calls the function to add to txt file
    TxtUpdate()


# call the main function to do all this work and get the email sent out
main()
