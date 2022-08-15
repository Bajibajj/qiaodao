import os
import requests
from bs4 import BeautifulSoup

def push(result):
    url = 'https://sctapi.ftqq.com/SCT165450TxflxDTaPnd9KfYpxBDj40ee3.send'
    data = {
        "title": '吾爱签到',
        "desp": result
    }

    requests.post(url, data)


def sign(cookie):
    result = ""
    headers = {
        "Cookie": cookie,
        "ContentType": "text/html;charset=gbk",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    requests.session().put(
        "https://www.52pojie.cn/home.php?mod=task&do=apply&id=2", headers=headers
    )
    fa = requests.session().put(
        "https://www.52pojie.cn/home.php?mod=task&do=draw&id=2", headers=headers
    )
    fb = BeautifulSoup(fa.text, "html.parser")
    fc = fb.find("div", id="messagetext").find("p").text
    if "您需要先登录才能继续本操作" in fc:
        result += "Cookie 失效"
    elif "恭喜" in fc:
        result += "签到成功"
    elif "不是进行中的任务" in fc:
        result += "今日已签到"
    else:
        result += "签到失败"
    return result 

def main():
    # b = os.environ['POJIE']
    cookie = 'htVC_2132_saltkey=jz10128N; htVC_2132_lastvisit=1660511501; Hm_lvt_46d556462595ed05e05f009cdafff31a=1660532565; htVC_2132_seccodecSAt6Jm6m=7346206.6094fcebee7d55bbd7; htVC_2132_seccodecSAt6J=7346205.f804b1231b57c585ee; htVC_2132_ulastactivity=1660532575%7C0; htVC_2132_auth=c6192%2F%2B%2BWBuWRcSj%2FHmzpFLA3YpZYtaUcjWlhUmWWp60Wi3MBZ1OT2tp2rvgOmq0wCPSN6Sorpg4lgwZ%2FWWTTyBdUXoz; htVC_2132_lastcheckfeed=1805136%7C1660532575; htVC_2132_checkfollow=1; htVC_2132_lip=120.208.99.4%2C1660532575; htVC_2132_sid=0; htVC_2132_connect_is_bind=1; htVC_2132_noticonf=1805136D1D3_3_1; htVC_2132_lastact=1660532579%09home.php%09spacecp; htVC_2132_checkpm=1; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1660532583'
    sign_msg = sign(cookie=cookie)
    # print(sign_msg)
    push(sign_msg)

if __name__ == "__main__":
    main()