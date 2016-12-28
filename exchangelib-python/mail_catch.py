#-*- coding: utf-8 -*- 
from exchangelib import DELEGATE, Account, Credentials,EWSTimeZone,EWSDateTime
import sys
from BeautifulSoup import BeautifulSoup
import re
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data
        # instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

creds = Credentials(
        username='ift.local\\%s'%sys.argv[1], 
        password='%s'%sys.argv[2])
account = Account(primary_smtp_address='jerry.cheng@infortrend.com',
        credentials=creds, 
        autodiscover=True, 
        access_type=DELEGATE)

print account
print type(account.drafts)
# Print inbox contents in reverse order
for item in account.drafts.all().order_by('-datetime_received'):
    #print(item.subject, item.body, item.attachments)
    pass

year, month, day = 2016, 11, 10
tz = EWSTimeZone.timezone('UTC')

print tz.localize(EWSDateTime(year, month, day + 10))
print tz.localize(EWSDateTime(year, month, day))

'''
items = account.calendar.filter(
    start__gt=tz.localize(EWSDateTime(year, month, day + 1)),
    )
print len(items)
for item in items:
    print item.subject.encode("utf-8")

items = account.inbox.filter(subject__contains='Debby')
print len(items)
for item in items:
    print item.subject.encode("utf-8")

n = account.inbox.all().count()
print n

all_subjects = account.inbox.all().values_list('subject', flat=True)
for subject in all_subjects:
    print subject

items = account.calendar.filter(start__range=(tz.localize(EWSDateTime(2016, 1, 1)), tz.localize(EWSDateTime(2017, 1, 1))))
for item in items:
    print item.subject.encode("utf-8")

items = account.inbox.filter(subject__contains='Debby')
print len(items)
for item in items:
    print item.subject.encode("utf-8")
    print dir(item)
    print item.datetime_received
'''
import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

items = account.inbox.filter(datetime_received__range=(tz.localize(EWSDateTime(2016, 12, 22)), tz.localize(EWSDateTime(2016, 12, 23))))
print len(items)
for item in items:
    subject = item.subject.encode("utf-8")
    if "RD 個人加班預先申請單" in subject:
        print subject
        body = item.body.encode("utf-8")
        search_obj = re.search(r'http(.*eflow.infortrend.com.*)todo', body)
        print search_obj.group(0).replace("amp;", "")

    elif "RD 加班預估計畫" in subject:
        print subject
    '''
    soup = BeautifulSoup(item.body.encode("utf-8"))
    ps = soup.findAll('p')
    for p in ps:
        print cleanhtml(str(p))
    '''



