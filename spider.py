import requests,os.path,random,json
from bs4 import BeautifulSoup
from data import *

class Spider():
    def __init__(self,session,targetUrl):
        self.userUrl=targetUrl
        self.main_url='https://weibo.cn'
        self.loginUrl='https://passport.weibo.cn/sso/login'
        self.imgFolder='img'
        self.session=session
        self.create_path()
        
    def create_path(self):
        """
            This method will create a path for image with a folder 
            with the name, self.imgFolder
            It will print out info on Terminate if the path is 
            already exist
        """
        if(os.path.exists(self.imgFolder)):  
            print("[!] The path %s is already existed"%self.imgFolder) 
        else:
            os.mkdir(self.imgFolder)
            print("[+] Image folder %s created"%self.imgFolder)   

    def login(self,username,password):
        """
            Login to the account and save/load cookie 
        """
        self.session.get(self.main_url,verify=True)
        self.save_cookies()
        postData={'username':username,
                    'password':password,
                    'savestate':1,
                    'r':'https://weibo.cn',
                    'ec':0,
                    'pagerefer':'https://weibo.cn/pub/',
                    'entry':'mweibo'
                    }
        r=self.session.post(self.loginUrl,headers=loginHeader,data=postData,verify=True)
        if r.ok==True:
                print("[*] Login Success")
                self.save_cookies()
                print("[*] Cookie saved")
        else:
            print("[x] Login fails")
            #This script is written by 0han, email:0han@pm.me
    def run(self, pageUrl):
            dataDic=self.arriveSinglePage(pageUrl)#dataDic will receive a package contains time, text, imgAddr
            self.writeText("==== "+dataDic['time'][:-4]+" ====\n")
            self.writeText(dataDic['text'])
            if dataDic['imgUrl']!=None:
                self.writeText('\n[Image \' %s.jpg \' Saved]'%dataDic['time'].split(' ')[0])
                self.writeText('[Original Image addr: %s'%dataDic['oriImg'])
                picName=dataDic['time'].split(' ')[0]
                if(os.path.exists('img/'+picName+'.jpg')):
                    picName+=str(random.random())
                self.saveImg(dataDic['imgUrl'],picName)
            else:
                self.writeText('[No Image/没有图像]')
            self.writeText("字数: "+str(len(dataDic['text'])))
            self.writeText("==== END ====\n\n")
            print("[+] "+dataDic['time'][:-4]+" done")
    def getPostsOnOnePage(self,pageNumber):
        currPage=self.userUrl+str(pageNumber)
        try:
            response=self.session.get(currPage,headers=header_data,verify=True)
            soup = BeautifulSoup(response.text,'html.parser')
            #res=soup.select('.ctt')
            res=soup.select(".c .ctt a")
            for i in res:
                #if i['href'][1:8]=='comment':
                if i.get_text()=='全文':
                    singlePageUrl=self.main_url+i.attrs['href']
                    self.run(singlePageUrl)
                else:
                    continue
        except:
            print("[!] Something goes wrong during the procedure, please check ur internet connection")

    def arriveSinglePage(self,url):
        """
            This method will return an dic, the first element is the time of the post
            and the second is the text,
            the third element is the address of the image if it has one
        """
        response=self.session.get(url,headers=header_data,verify=True)
        soup = BeautifulSoup(response.text,'html.parser')
        textRes=soup.select(".c .ctt")
        text=textRes[0].get_text()[1:]#text of the post
        timeRes=soup.select(".c .ct")
        timetag=timeRes[0].get_text()#time of the post

        limgAddr=soup.select(".c div a")
        imgAddr=soup.select(".c .ib")
        for j in limgAddr:
            if j.get_text()=="原图":
                oriImg='http://wx4.sinaimg.cn/large/'+j.attrs['href'].split('u=')[1].split('&rl')[0]+'.jpg'
        if imgAddr!=[]:
            imgUrl=imgAddr[0]['src']#image address
        else:
            imgUrl=None#no image attached
        resDic={
            'time':timetag,
            'text':text,
            'imgUrl':imgUrl,
            'oriImg':oriImg
        }
        return resDic
    def writeText(self,text):
        with open("text.txt", 'a', encoding='utf-8') as f:
            f.write(text+'\n')
    def saveImg(self,imgURL,picName):
        pic_r=requests.get(imgURL,headers=header_data,verify=True)
        name=picName+'.jpg'
        with open('img/'+name,"wb") as file:
            file.write(pic_r.content)

    def save_cookies(self):
        with open('./'+"cookiefile",'w')as f:
            json.dump(self.session.cookies.get_dict(),f)#_session.cookies.save()
    def read_cookies(self):
        #_session.cookies.load()
        #_session.headers.update(header_data)
        with open('./'+'cookiefile')as f:
            cookie=json.load(f)
            self.session.cookies.update(cookie)
            return cookie

