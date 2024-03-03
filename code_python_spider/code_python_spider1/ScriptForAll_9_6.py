# -*- coding: utf-8 -*-
import requests
import re
import time
import pymysql
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import json
from datetime import datetime
import traceback

mysqldb = pymysql.connect(host="localhost", port=3306, password="123.abc", user="root", database="dwd",charset="utf8mb4")
# 创建mysql游标
cursor = mysqldb.cursor()
# 配置edgeDriver
driver = webdriver.Edge()
# 初始化头文件
headers = {
    "Cookie": "NewProvinceId=4; NCid=62; NewProvinceName=%E7%A6%8F%E5%BB%BA; NCName=%E6%BC%B3%E5%B7%9E; 17uCNRefId=RefId=14211945&SEFrom=bing&SEKeyWords=; TicketSEInfo=RefId=14211945&SEFrom=bing&SEKeyWords=; CNSEInfo=RefId=14211945&tcbdkeyid=&SEFrom=bing&SEKeyWords=&RefUrl=https%3A%2F%2Fwww.bing.com%2F; qdid=35297|1|14211945|dd62ba; Hm_lvt_64941895c0a12a3bdeb5b07863a52466=1694053116; Hm_lpvt_64941895c0a12a3bdeb5b07863a52466=1694053116; __tctmu=144323752.0.0; __tctmz=144323752.1694053118170.1.1.utmccn=(referral)|utmcsr=bing.com|utmcct=|utmcmd=referral; longKey=1694053118776960; __tctrack=0; ASP.NET_SessionId=xnwnwr0nmxmnayams0g2nzgs; Hm_lvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1694053123; wwwscenery=4e2eaaef16e5b9246b38c49c8c6872cb; _dx_captcha_cid=99910880; _dx_uzZo5y=963ece66ac5dd12d11f9fa90e7aa5879e5c6f837bf6f299d29413e14db23e0a31c117d9f; _dx_FMrPY6=64f9334dLBOFUhMe6ymVahBlWEi3WbeJlJ4M6HV1; _dx_app_bc4b3ca6ae27747981b43e9f4a6aa769=64f9334dLBOFUhMe6ymVahBlWEi3WbeJlJ4M6HV1; __tccgd=144323752.0; __tctmd=144323752.737325; __tctma=144323752.1694053118776960.1694053118170.1694156566988.1694163906775.5; route=e83eaebd8f07fc1b8cfab528aeb2900e; __tctmc=144323752.41634340; __tctmb=144323752.107140256390249.1694164095388.1694164102278.5; Hm_lpvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1694164863",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "https://www.ly.com/scenery/scenerysearchlist_0_0__0__0_0_0_0_0.html"
}


# 获取评论页数
def getCommentPageNumber(spotCodeList):
    # 类型应该为dict{(景区url,景区code):set(所需要的页面索引)}
    urlDict = dict()
    for spotCode in spotCodeList:
        # 初始化post请求的parame
        data = {
            "action": "GetDianPingList",
            "sid": spotCode,
            "page": 1,
            "pageSize": 10,
            "labId": 1,
            "sort": 0,
            "iid": 0.5454575378386792,
        }
        # 先获取评论的第一页,查看他总共有几页
        commentUrl = "https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid={spotid}&page={page}&pageSize=10&labId=1&sort=0".format(
            spotid=spotCode, page=1)
        page = requests.post(commentUrl, data=data).text
        # 从爬取到的页面获取有多少页,如果没找到,则为1
        try:
            pageNumber = re.compile('"totalPage":(.*?),"totalCount"').findall(page)[0]
        except:
            pageNumber = 1
        # 将得到的结果页数放入随机方法中生成需要爬取的页面,将获取到的结果和url存放进urlDict当中
        urlDict[("https://www.ly.com/" + spotCodeList.get(spotCode), spotCode)] = getPageIndexList(
            pageNumber=int(pageNumber), percent=0.2)
    # 将最终结果的字典返回
    return urlDict


# 拼接url并进入页面获取信息
def getSpotCode(sliceUrl):
    # 初始化变量
    spotId = list()
    for urlEnding in sliceUrl:
        secondUrl = "https://www.ly.com/" + urlEnding
        # 获取景区id
        spotId.append(
            re.compile("https://www.ly.com//scenery/BookSceneryTicket_(?P<id>.*?).html", re.S).findall(secondUrl)[0])
    return spotId


# 跳转页面
def transferPage(page, pageNumber):
    # 判断页面是否只有一页
    # 若为1,则直接获取该页面所有url
    # 若不为1,则跳转,并获取页面url
    if pageNumber == 1:
        splitUrl = etree.HTML(str(driver.page_source)).xpath(
            "//div[@class='scenery_content']//a[@class='sce_name goFinal']//@href")
        return splitUrl
    else:
        driver.find_element(By.XPATH, "//*[@id='pageNum_title']/div/input[1]").send_keys(page)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//*[@id='pageNum_title']/div/input[2]").click()
        splitUrl = etree.HTML(str(driver.page_source)).xpath(
            "//div[@class='scenery_content']//a[@class='sce_name goFinal']//@href")
        return splitUrl


# 传入页面列表和百分比,例如该条件下有1000页景区,百分比为3成,则会随机获取330页数据,而不是全部获取
def getPageIndexList(pageNumber, percent):
    pageIndexList = set()
    # 如果页数过小,则直接取全部
    if pageNumber <= 3:
        while pageNumber > pageIndexList.__len__():
            pageIndexList.add(random.randint(1, pageNumber))
    else:
        page = int(pageNumber * percent)
        while page > pageIndexList.__len__():
            pageIndexList.add(random.randint(1, pageNumber))
    return pageIndexList


# 获取景区景点地区和星级
def getInformation(zoneIndex, gradeIndex):
    driver.get("https://www.ly.com/scenery/scenerysearchlist_0_0__0__0_0_0_0_0.html")
    # 点击展开地区
    driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[3]/div/i').click()
    time.sleep(0.5)
    # 依次点击地区
    zone = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[3]/div/div/div[2]/div[1]/a[{zoneIndex}]'.format(
        zoneIndex=zoneIndex)).text
    driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[3]/div/div/div[2]/div[1]/a[{zoneIndex}]'.format(
        zoneIndex=zoneIndex)).click()
    time.sleep(0.5)
    # 获取景区,点等级,建议从1开始
    grade = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[5]/div/span[3]/a[{gradeIndex}]'.format(
        gradeIndex=gradeIndex)).text
    driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[5]/div/span[3]/a[{gradeIndex}]'.format(
        gradeIndex=gradeIndex)).click()
    time.sleep(0.5)
    # 获取该条件下拥有多少页,如果没有则返回1
    try:
        page = re.findall(r'\D*(\d+)\D*', driver.find_element(By.XPATH, '//*[@id="pageNum_title"]/span').text)[0]
    except:
        page = 1
    # 将上述信息返回,交由随机数进行判定需要爬取哪些页面
    return (zone, grade, page)


# 下载图片并保存
def getImageFunction(imgUrl, spotName):
    image = requests.get(imgUrl).content
    with open(f"D:\imgTest\defineImg\{spotName}.jpg", 'wb') as f:
        f.write(image)


# 获取景区景点信息
# 返回单个景点的景点信息
def getSpotInformation(url, headers):
    informationDict = dict()
    informationPage = requests.get(url=url, headers=headers).text
    try:
        # 获取页面信息并返回
        informationDict.update({
            "spotName": etree.HTML(informationPage).xpath('//*[@id="content"]/div[3]/div[2]/h3/text()')[0].replace('\n',
                                                                                                                   "").replace(
                " ", "").replace("\'", ""),
            "grade": etree.HTML(informationPage).xpath('//*[@id="content"]/div[3]/div[2]/h3/span/text()')[0].replace(
                '\n', "").replace(" ", "").replace("\'", ""),
            "tag": etree.HTML(informationPage).xpath('//*[@id="content"]/div[3]/div[2]/div[2]/p/text()')[0].replace(
                '\n', "").replace(" ", "").replace("\'", ""),
            "address": etree.HTML(informationPage).xpath('//*[@id="content"]/div[3]/div[2]/p[1]/span/text()')[
                0].replace('\n', "").replace(" ", "").replace("\'", ""),
            "openTime": etree.HTML(informationPage).xpath('//*[@id="content"]/div[3]/div[2]/p[2]/span/text()')[
                0].replace('\n', "").replace(" ", "").replace("\'", ""),
            "ticket": etree.HTML(informationPage).xpath('//*[@id="content"]/div[3]/div[2]/div[6]/div/span/b/text()')[
                0].replace('\n', "").replace(" ", "").replace("\'", ""),
            "introduce":
                etree.HTML(informationPage).xpath('//*[@id="scenery_intro_con"]/div[2]/div/div[1]/div/p/text()')[
                    0].replace('\n', "").replace(" ", "").replace("\'", "")
        })
        try:
            imgUrl = "https:" + etree.HTML(informationPage).xpath(
                '//*[@id="scenery_intro_con"]/div[2]/div/div[1]/div/div/img/@orisrc')[0]
            # 将文件名和图片url传过去
            getImageFunction(imgUrl=imgUrl, spotName=informationDict["spotName"])
        # 如果没有图片信息则跳过
        except:
            pass
    except:
        return 1
    return informationDict


# 获取评论信息
# 将评论完整url,景区编号,页数放入其中
def getCommentInformation(urlCodeAndPage, zoneAndGrade):
    for url, code in urlCodeAndPage:
        # 获取景区景点信息
        spotInformation = getSpotInformation(url, headers=headers)
        if spotInformation != 1:
            # 遍历获取页面
            for commentPage in urlCodeAndPage[(url, code)]:
                data = {
                    "action": "GetDianPingList",
                    "sid": code,
                    "page": commentPage,
                    "pageSize": 10,
                    "labId": 1,
                    "sort": 0,
                    "iid": 0.5454575378386792,
                }
                commentUrl = "https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid={spotid}&page={page}&pageSize=10&labId=1&sort=0".format(
                    spotid=code, page=commentPage)
                # 获取到一个有关评论的字典
                commentPage = json.loads(requests.post(commentUrl, data).text)["dpList"]

                # 遇到异常数据,无法写入直接跳过
                try:
                    # 开启一个mysql事务
                    mysqldb.begin()

                    # 返回存储游标,在每个页面数据处理完毕以后提交游标
                    for dic in commentPage:
                        # 剔除无用字段,节约空间 TODO -------------------------------如果想将评论中的更多字段添加入当中,则可以在此处选择----------------------------------------
                        input_key = (
                        "commentType", "dpGuid", "dpId", "DPItemId", 'DPItemName', 'memberHeaderImgUrl', 'dpImgUrl')
                        # 将景点和评论字段合二为一
                        totalInformation = {key: value for key, value in dic.items() if not input_key.__contains__(key)}
                        totalInformation.update(spotInformation)
                        totalInformation.update(zoneAndGrade)
                        # 将数据传入数据库中,并返回一个数据库游标,存储入上一级变量当中 TODO--------------------------------需要添加新字段在此处添加名称和数据,数据来源均来自totalInformation
                        manipulateDatabase(table="new_data", columnsList=(
                            "commentContent",
                            "commentTime",
                            "user_name",
                            "comment_type",
                            "spot",
                            "spot_grade",
                            "tag",
                            "spot_location",
                            "open_time",
                            "city",
                            "introduce",
                            "comment_address"
                        ), dataList=(
                            totalInformation['dpContent'].replace("\'", ""),
                            totalInformation['dpDate'].replace("\'", ""),
                            totalInformation['dpUserName'].replace("\'", ""),
                            totalInformation['lineAccess'].replace("\'", ""),
                            totalInformation['spotName'].replace("\'", ""),
                            totalInformation['grade'].replace("\'", ""),
                            totalInformation['tag'].replace("\'", ""),
                            totalInformation['address'].replace("\'", ""),
                            totalInformation['openTime'].replace("\'", ""),
                            totalInformation['zone'].replace("\'", ""),
                            totalInformation['introduce'].replace("\'", ""),
                            totalInformation['DPLocation'].replace("\'", "")
                        ))

                    # 处理结束,将最后获取到的那个游标提交
                    mysqldb.commit()
                # 报错以后回滚事务
                except:
                    mysqldb.rollback()

        else:
            pass


# 爬取前,先读取文件并组合,查看当前爬的页面是否已经爬过了
def checkCondition(zone, grade):
    # 获取文件信息
    with open(".\information.txt", mode="r", encoding="utf-8") as f:
        information = f.read().split(",")
        f.close()
    # 拼接文件信息,存在返回false,不存在返回true
    if list(information).__contains__(zone + "|" + grade):
        return False
    else:
        return True


# 将已经读取过的数据持久化入文件当中
def allreadyRead(zone, grade):
    with open(".\information.txt", mode="a", newline="", encoding="utf-8") as information:
        information.write(zone + "|" + grade + ",")
        information.close()


# 将数据写入数据库
def manipulateDatabase(table, columnsList, dataList):
    cursor.execute("""
    insert into {table}({columns}) values({data})
    """.format(
        table=table,
        columns=",".join(list(columnsList)),
        data="\'" + "\',\'".join(list(dataList)) + '\''
    ))


# 创建表结构 TODO----------添加新字段时,要将旧表删除,并在这里写入新字段名称,要与上面相对应的名称
def createTable():
    mysqldb.begin()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS new_data(
    `commentContent` VARCHAR(2000) NOT NULL COMMENT '评论内容',
    `commentTime` VARCHAR(20) COMMENT '评论时间',
    `user_name` VARCHAR(20) COMMENT '用户名',
    `comment_type` VARCHAR(1000) NOT NULL  COMMENT '用户评价',
    `spot` VARCHAR(40) NOT NULL COMMENT '景区(点)名称',
    `spot_grade` VARCHAR(10) COMMENT '景区(点)等级',
    `tag` VARCHAR(100) COMMENT '景区(点)标签',
    `spot_location` VARCHAR(60) COMMENT '景区(点)详细地址',
    `open_time` VARCHAR(50) COMMENT '景区(点)开放时间',
    `city` VARCHAR(20) COMMENT '景区(点)所在城市',
    `introduce` VARCHAR(5000) COMMENT '景区(点)介绍',
    `comment_address` VARCHAR(20) COMMENT '用户评论地址'
    )
    """)
    mysqldb.commit()


# 报错跳出,并将报错信息保存下来
def errorBreak(message):
    with open(".\log.txt", mode="a", newline="", encoding="utf-8") as error:
        error.write(str(datetime.now()) + ":  " + message + "\n")
        error.close()


# 将两个list顺序拼接成dict
def zipToDict(lis1, lis2):
    dic = dict()
    for len in range(list(lis1).__len__()):
        dic.update({lis1[len]: lis2[len]})
    return dic


# 入口方法
if __name__ == '__main__':
    # 定义初始化
    # 地区起始位置最小为0
    zoneNumber = 0
    # 景区景点等级列表
    gradeList = (1, 2, 3, 4)
    # 初始化建表
    createTable()
    # 循环获取,直到报错后跳出
    while True:
        try:
            zoneNumber += 1
            for grades in gradeList:
                # 获取条件,包括地区zone,等级grade,页数
                zone, grade, pageNumber = getInformation(zoneIndex=zoneNumber, gradeIndex=grades)
                # 判断该条件下是否已经存在读取结束的情况
                if checkCondition(zone, grade):
                    # 将获取到的page页数进行处理,随机取其中的百分之二十读取
                    for page in getPageIndexList(int(pageNumber), 0.1):
                        # transferpage是换页,getSpotCode是返回一个城市编码列表
                        sliceUrl = transferPage(page=page, pageNumber=pageNumber)
                        # 获取城市编码
                        cityCodeList = getSpotCode(sliceUrl=sliceUrl)
                        # getCommentPageNumber将城市编码导入,生成评论url和评论页数类型为dict{(spotUrl,spotCode):set(页面)}
                        # getCommentInformation是获取景区数据和评论数据,并将获取的结果写入数据库
                        getCommentInformation(getCommentPageNumber(zipToDict(cityCodeList, sliceUrl)),
                                              zoneAndGrade={"zone": zone, "grade": grade})
                    # 一轮结束,将结束结果存储入日志当中
                    allreadyRead(zone=zone, grade=grade)
                else:
                    pass
        except Exception as e:
            errorBreak(str(traceback.format_exc()))
