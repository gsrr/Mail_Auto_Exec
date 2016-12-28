#-*- coding: utf-8 -*- 
from exchangelib import DELEGATE, Account, Credentials,EWSTimeZone,EWSDateTime
import datetime
import re
import traceback
import platform

TEXT_FORMAT = "utf-8"

class MailAuto:
    def __init__(self, domain, user, password, mail_server):
        self.domain = domain
        self.user = user
        self.password = password
        self.mail_server = mail_server
        self.tz = EWSTimeZone.timezone('UTC')
        self.account = None
        self.history = []
        
    def get_config(self):
        print "domain:", self.domain
        print "user:", self.user
        print "password:", self.password
        print "mail server:", self.mail_server

    def set_creds_account(self):
        creds = Credentials(
                username='%s\%s'%(self.domain,self.user), 
                password='%s'%self.password)

        account = Account(primary_smtp_address='%s'%self.mail_server,
                credentials=creds, 
                autodiscover=True, 
                access_type=DELEGATE)

        self.account = account
    
    def get_mail(self):
        t = datetime.datetime.now()
        start_time = self.tz.localize(EWSDateTime(t.year, t.month, t.day-1))
        end_time = self.tz.localize(EWSDateTime(t.year, t.month, t.day, t.hour))
        print start_time, end_time
        items = self.account.inbox.filter(datetime_received__range=(start_time, end_time))
        if len(items) == len(self.history):
            return
        
        for i in range(len(self.history), len(items)):
            item = items[i]
            subject = item.subject.encode(TEXT_FORMAT)
            #print subject
            self.history.append(subject)
            if "RD 個人加班預先申請單".decode("utf-8").encode(TEXT_FORMAT) in subject:
                print subject
                body = item.body.encode(TEXT_FORMAT)
                search_obj = re.search(r'http(.*eflow.infortrend.com.*)todo', body)
                print search_obj.group(0).replace("amp;", "")
            

def pre_main(func):
    def wrap_func():
        global TEXT_FORMAT
        if platform.system() == 'Windows':
            TEXT_FORMAT = "big5"
        func()
    return wrap_func
    
@pre_main
def main():
    try:
        domain = raw_input("domain:")
        user = raw_input("username:")
        password = raw_input("password:")
        mail_server = raw_input("mail server:(user@domain.com)")
        print
        ma = MailAuto(domain, user, password, mail_server)
        ma.get_config()
        ma.set_creds_account()
        ma.get_mail()
    except:
        print traceback.format_exc()

if __name__ == "__main__":
    main()
