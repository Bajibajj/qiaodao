# -*- coding:utf-8 -*-
# @Time       :2022/8/13 11:01
# @SOFTWARE   :爬虫学习

import requests

def qiandao():

    session = requests.session()

    url_cook = 'https://www.ruike1.com/k_misign-sign.html?operation=qiandao&format=global_usernav_extra&formhash=c6f8a78f&inajax=1&ajaxtarget=k_misign_topb'

    headers = {
        # 'referer':' https://www.ruike1.com/home.php?mod=space&do=pm',
        # 'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
        'cookie': 'Hm_lvt_9d4dff14662c55b14fcd14fd34b8dcd8=1650421290,1650440143,1650593469,1650679950; zzhh_2132_saltkey=ptF5Jfl1; zzhh_2132_lastvisit=1660527542; zzhh_2132_ulastactivity=54adnP9uL38shJITAAmPYGl8UhDcwc6fyMZ0gquuRIvYA5KN6PR6; zzhh_2132_connect_is_bind=1; zzhh_2132_nofavfid=1; zzhh_2132_newemail=23994%091946497315%40qq.com%091660531193; zzhh_2132_sid=EO5ApZ; Hm_lvt_73ad58a7cf08cf5833714aed91aa7068=1660355572,1660445351,1660530897,1660535769; zzhh_2132_auth=1187HYNSK3dMtNMMciXLfjmKJwWKBC9uzwGER%2BIaOKlUhqLC%2FHqAUBAxNDArZq4pp%2BaYe9IpyVPmvhc90%2FeZvn6kYg; zzhh_2132_lastcheckfeed=23994%7C1660535772; zzhh_2132_lip=120.208.99.4%2C1660447350; zzhh_2132_seccodecSEO5ApZ=2.f08206f3c72f8f6fa1; zzhh_2132_sendmail=1; zzhh_2132_checkpm=1; Hm_lpvt_73ad58a7cf08cf5833714aed91aa7068=1660536077; zzhh_2132_lastact=1660536077%09misc.php%09patch'
    }

    res = session.get(url = url_cook,headers=headers)


    return res.text.split('CDATA')[-1]
def push(res):
    url = 'https://sctapi.ftqq.com/SCT165450TxflxDTaPnd9KfYpxBDj40ee3.send'
    data = {
        "title": '瑞客签到',
        "desp": res
    }

    requests.post(url, data)

def main():
    res = qiandao()
    push(res)

if __name__ == '__main__':
    main()