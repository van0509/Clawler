# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tedu
   Author :       Seven
   date：          2019-02-07
-------------------------------------------------
"""
__author__ = 'Seven'

import requests, re,myDb

from UA import UA

# conn = requests.session()
# url='http://uc.tmooc.cn/login'
# postData={
#     'loginName': '1317643074@qq.com',# ntdvip@tedu.cn  1317643074@qq.com
#     'password': '126e7c706ee9da95c4ed5ce46ca78cde',#  2ae8d57bff1e58408d721fe70bea0585  126e7c706ee9da95c4ed5ce46ca78cde
#     'imgCode:':'',
#     'accountType':1,
# }
# headers={
#     'Host':'uc.tmooc.cn',
#     'Origin':'http://www.tmooc.cn',
#     'Referer':'http://www.tmooc.cn',
#     'User-Agent':UA().userAgent(),
#     'X-Requested-With': 'XMLHttpRequest',
# }
# rep=conn.post(url=url,data=postData,headers=headers).json()

# if rep['id']:
#     rep1 = conn.post('http://tts.tmooc.cn/studentCenter/toMyttsPage').content.decode()
#     print(rep1)
# else:
#     print('登录失败',rep)
z = 0
url = 'http://tts.tmooc.cn/studentCenter/toMyttsPage'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'num_1=2; isCenterCookie=no; eBoxOpenVIP_AID_N_GXZ_V01_S=true; tedu.local.language=zh-CN; uniqueVisitorId=2bfbf581-fa0d-e1fa-fc69-3b44598de95a; Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1549288721,1549541049,1550296602,1550495633; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1550495633; TMOOC-SESSION=E1AD820301ED4CCAA781FBDAE05ED709; sessionid=E1AD820301ED4CCAA781FBDAE05ED709|1317643074%40qq.com; cloudAuthorityCookie=0; versionListCookie=VIP_AID_N_GXZ_V01_S; defaultVersionCookie=VIP_AID_N_GXZ_V01_S; versionAndNamesListCookie=VIP_AID_N_GXZ_V01_SN22NAID%25E5%25B0%25B1%25E4%25B8%259A%25E8%25AF%25BE%25E7%25A8%258BVIP1.0; courseCookie=AID; stuClaIdCookie=546140; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1549589006,1550296624,1550296634,1550495646; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1550495646; JSESSIONID=A4F9A23348CFDA120F9DE04AFA6BAD81',
    'Host': 'tts.tmooc.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

rep = requests.get(url, headers=headers).content.decode()
pattern = '<a target="_blank" href="([\S]*?)">'
conn = re.findall(pattern, rep)
for url1 in conn[1::]:
    rep1 = requests.get(url1, headers=headers).content.decode()
    if rep1:
        pattern1 = "\('([\s\S]*?)','A_VIP_[\s\S]*?title=\"([\s\S]*?)\">"
        resp = re.findall(pattern1, rep1)
        # print(resp)
        for i in resp:
            z += 1
        #     # print(i[0],i[1])
            db = myDb.mySql()
            ID= i[0]
            title = i[1]
            sql = 'INSERT INTO seven.python(title, ID)VALUES(%s,%s);'
            params = (title, ID)
            resoult = db.execute(sql, params)
            if resoult == True:
                print('Insert 成功%d条'%z)
            else:
                print('Insert 失败')
        #     mac = 'https://p.bokecc.com/servlet/getvideofile?vid=%s&siteid=0DD1F081022C163E&divid=cc_video_%s_9332455&width=1400&useragent=Android&version=20140214&hlssupport=1&vc=tts-110870F5F7644B12BF4C009A2B48DBFA&mediatype=1&callback=cc_js_Player.showPlayerView&r=7395025.59645809' % (
        #     i[0], i[0])
        #     tts = requests.get(mac).text
        #     pattern2 = '"backupurl":"([\s\S]*?)","'
        #     down = re.findall(pattern2, tts)
        #     print(down)
            # with open('download1.txt', 'a') as f:
            #     f.writelines(str(z)+'-'+i[1] + ',' + down[0] + '\n')
            # print('当前插入第%d条链接,加油哈！' % z)

            # cc_js_Player.showPlayerView({"uid":"0DD1F081022C163E","divid":"cc_video_1E833DCEFCACE45B9C33DC5901307461_9332455","img":"http://2-img.bokecc.com/comimage/0DD1F081022C163E/2018-07-05/1E833DCEFCACE45B9C33DC5901307461-1.jpg","UPID":"4904241549554480614","vrmode":0,"playtype":0,"authenable":1,"freetime":0,"defaultquality":20,"vid":"1E833DCEFCACE45B9C33DC5901307461","copies":[{"mediatype":1,"backupurl":"http://cd15-c120-1.play.bokecc.com/flvs/0DD1F081022C163E/2018-07-05/1E833DCEFCACE45B9C33DC5901307461-20.m3u8?t=1549561680&key=B1E3FC450A468F1600CC6889067A9F73&tpl=10&tpt=112","desp":"高清","playurl":"http://cd12-c120.play.bokecc.com/flvs/0DD1F081022C163E/2018-07-05/1E833DCEFCACE45B9C33DC5901307461-20.m3u8?t=1549561680&key=B1E3FC450A468F1600CC6889067A9F73&tpl=10&tpt=112","quality":20},{"mediatype":1,"backupurl":"http://cd15-c120-1.play.bokecc.com/flvs/0DD1F081022C163E/2018-07-05/1E833DCEFCACE45B9C33DC5901307461-10.m3u8?t=1549561680&key=5636090A09957C10040DEC9805D1F8E6&tpl=10&tpt=112","desp":"清晰","playurl":"http://cd12-c120.play.bokecc.com/flvs/0DD1F081022C163E/2018-07-05/1E833DCEFCACE45B9C33DC5901307461-10.m3u8?t=1549561680&key=5636090A09957C10040DEC9805D1F8E6&tpl=10&tpt=112","quality":10}],"status":1})
