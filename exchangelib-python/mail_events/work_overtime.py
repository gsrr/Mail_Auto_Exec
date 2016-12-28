#-*- coding: utf-8 -*- 
import re

def check(line, TEXT_FORMAT):
    if "RD 個人加班預先申請單".decode("utf-8").encode(TEXT_FORMAT) in line:
        return True

def do(body):
    search_obj = re.search(r'http(.*eflow.infortrend.com.*)todo', body)
    print search_obj.group(0).replace("amp;", "")
    
