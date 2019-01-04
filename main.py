#author="0han"
#date="2019.1.4"
from spider import Spider
import requests,time
targetUrl=''
_session=requests.session()
obj=Spider(_session,targetUrl)
obj.login('','')#(account,password) both in string, eg ('12345','password')
for number in range(1,128):
    #the range depends on ur target, check how many pages his blog has at the beginning
    obj.getPostsOnOnePage(number)
    time.sleep(5)#you need this to make your spider looks like a human being
    print("[*] Take a break for 5 seconds ...")