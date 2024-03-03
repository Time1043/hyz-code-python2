# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 12:28
# @File    ：demo2FuZhou2.py
# @Function:

import requests

resp = requests.post(
    url='https://www.fuzhou.gov.cn/ssp/search/api/search?time=1702527772549',
    data={
        "siteType": "1",
        "mainSiteId": "402849946077df37016077eea95e002f",
        "siteId": "402849946077df37016077eea95e002f",
        "type": "0",
        "page": "1",
        "rows": "10",
        "historyId": "48908a988b85d1ee018c22e8a6e242c0",
        "sourceType": "SSP_ZHSS",
        "isChange": "0",
        "fullKey": "N",
        "wbServiceType": "13",
        "fileType": "",
        "fileNo": "",
        "pubOrg": "",
        "themeType": "",
        "searchTime": "",
        "startDate": "",
        "endDate": "",
        "sortFiled": "RELEVANCE",
        "searchFiled": "",
        "dirUseLevel": "",
        "issueYear": "",
        "issueMonth": "",
        "allKey": "",
        "fullWord": "",
        "oneKey": "",
        "notKey": "",
        "totalIssue": "",
        "chnlName": "",
        "zfgbTitle": "",
        "zfgbContent": "",
        "zfgbPubOrg": "",
        "zwgkPubDate": "",
        "zwgkDoctitle": "",
        "zwgkDoccontent": "",
        "zhPubOrg": "1",
        "keyWord": "编程",
        "pubOrgType": "",
        "zhuTiIdList": "",
        "feaTypeName": "",
        "jiGuanList": "",
        "publishYear": ""
    },
    headers={
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
)
print(resp.text)
