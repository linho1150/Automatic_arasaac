import os
import time
import json
import urllib.request
import sys
import re

direction = 0
subDirection = 0
   
            
def downloadImg(id): #이미지 다운로드 받기
    url = "https://api.arasaac.org/api/pictograms/"+str(id)+"?backgroundColor=%23ffffff&hair=brown&url=true&download=false"
    nameUrl = "https://api.arasaac.org/api/pictograms/"+str(id)+"/languages/en?backgroundColor=%23ffffff&hair=brown&url=true&download=false"

    req = urllib.request.Request(url)
    response = json.loads(urllib.request.urlopen(req,timeout=5).read())
    url=response["image"]
    nameReq = urllib.request.Request(nameUrl)
    nameResponse = json.loads(urllib.request.urlopen(nameReq,timeout=5).read())
    name=nameResponse["keywordsByLocale"]['en'][0]['keyword']
    Ename=name
    if direction=="1":
        name=translate(name)
        if name==0:
            print("당일 API 무료 지원이 완료되었습니다. 다른 항목을 이용하세요")
            sys.exit()
        print(str(id)+'_'+str(name['message']['result']['translatedText']))
        nameTxt=str(id)+'_'+re.sub('[\/:*?"<>|]','',str(name['message']['result']['translatedText']))+".png"
    elif direction=="2":
        nameTxt=str(id)+'_'+re.sub('[\/:*?"<>|]','',str(Ename)+".png")
    elif direction=="3":
        nameTxt=str(id)+".png"
    else:
        print("알수없는오류")
    start = time.time()
    urllib.request.urlretrieve(url,nameTxt)
    print(id,"완료 소요시간: ",time.time() - start)



def checkRecentfile(): #로컬에서 가장 최신 고유번호 가져오기
    try:
        path_dir = os.getcwd()
        file_list = os.listdir()
        file_list.pop()
        filenum=int(max(file_list).split('_')[0].replace('.png',''))
        return filenum
    except:
        print("Error : *.py 파일 외에는 문자로 시작하는 파일 혹은 폴더가 있으면 불가합니다.\n다운받은 이미지 외 파일 혹은 폴더를 정리해주세요.")
        sys.exit()

def translate(txt): #네이버 파파고 api 번역기
    try:
        client_id = "t3rKqVrY7s09i66hhUiM"
        client_secret = "1rQ6pa6Vud"
        encText = urllib.parse.quote(txt)
        data = "source=en&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            return json.loads(response_body.decode('utf-8'))
        else:
            return 0
    except:
        return 0

def arasaacRecentImgId(): #가장 최신 이미지 파일 id 가져오기
    count=5
    url = 'https://api.arasaac.org/api/pictograms/ko/new/'+str(count)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    jsonData = json.loads(data)
    recent=jsonData[0]['_id']
    return recent

##메인 프로그램 시작----------------------

while True:
    print("원하시는 기능을 입력해주세요")
    print("1. 고유번호_한글번역.png")
    print("2. 고유번호_영문.png")
    print("3. 고유번호.png")
    print("* 1번항목은 무료 제한이 있습니다\n")
    direction = input("번호를 입력하세요 : ")
    if direction == '1':
        print("1. 마지막으로 다운받은 항목부터 최신 항목까지")
        print("2. 특정 고유번호부터 최신 항목까지")
        print("3. 고유번호 입력하여 한개 다운로드")
        subDirection=input("보조 번호를 입력하세요 : ")
        if subDirection=='1' or subDirection=='2' or subDirection=='3':
            break
        else:
            print("번호를 다시 입력하세요")
    elif direction == '2':
        print("1. 마지막으로 다운받은 항목부터 최신 항목까지")
        print("2. 특정 고유번호부터 최신 항목까지")
        print("3. 고유번호 입력하여 한개 다운로드")
        subDirection=input("보조 번호를 입력하세요 : ")
        if subDirection=='1' or subDirection=='2' or subDirection=='3':
            break
        else:
            print("번호를 다시 입력하세요")
    elif direction == '3':
        print("1. 마지막으로 다운받은 항목부터 최신 항목까지")
        print("2. 고유번호 입력하여 최신 항목까지")
        print("3. 고유번호 입력하여 한개 다운로드")
        subDirection=input("보조 번호를 입력하세요 : ")
        if subDirection=='1' or subDirection=='2' or subDirection=='3':
            break
        else:
            print("번호를 다시 입력하세요")
            
filenum=checkRecentfile()
recent=arasaacRecentImgId()
if subDirection=='1':
    ImgId=filenum-1
elif subDirection=='2':
    try:
        ImgId=int(input("시작할 이미지의 고유번호를 입력하세요 : "))
    except:
        print("숫자를 입력하세요")
        sys.exit()
elif subDirection=='3':
    try:
        ImgId=int(input("이미지의 고유번호를 입력하세요 : "))
    except:
        print("숫자를 입력하세요")
        sys.exit()
    try:
        downloadImg(ImgId)
        sys.exit()
    except Exception as e:
        print(ImgId,"가없음")
        sys.exit()
        pass
else :
    ImgId=filenum-1
    
for imgId in range(ImgId,recent):
    try:
        downloadImg(imgId)
    except Exception as e:
        print(imgId,"가없음")
        pass
