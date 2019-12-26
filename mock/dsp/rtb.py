# encoding:utf-8
import flask
import random
import string
from flask import jsonify, request

app = flask.Flask(__name__)
imps_mock = [{
    "id": "11424_182i500_52476_0",
    "impid": "20853",
    "crid": "525993",
    "price": 4005,
    "ext": {
        "adm": [
            {
                "url": "https://edt.fp.ps.netease.com/file/5a0273398b7427e5f60e7c31FgCVuiiH.jpg",
                "type": 0
            }
        ],
        "advertiser": {
            "id": 1305,
            "industry": "01",
            "subIndustry": "0103"
        },
        "linkUrl": "https://www.baidu.com",
        "style": 1010013,
        "title": "测试RTB bidding v1"
    },
    "nurl": "https://nex.163.com/q",
    "pvm": [
        "https://i.gridsumdissector.com/v/?gscmd=impress&gid=gad_393_89zduu7t&os=__OS__&if=${"
        "IDFA}&oid=__OPENUDID__&aid=__ANDROIDID__&im=${"
        "IMEI}&oa=__OAID__&m=__MAC__&ip=__IP__&ts=__TS__&did=__DUID__&aaid=__AAID__&uid=__UDID__&odin=__ODIN__&ua"
        "=__UA__&lbs=__LBS__&autorefresh=__AUTOREFRESH__&id=${AUCTION_ID}&bidid=${AUCTION_BID_ID}$impid=${"
        "AUCTION_IMP_ID}&price=${AUCTION_PRICE}&currency=${"
        "AUCTION_CURRENCY}&autorefresh=__AUTOREFRESH__&u=https://stats.dmp.ghac.cn/imp.gif?e"
        "=xzv_FaJamw4ixj70jcmA2x4MI9tj9Okb5IZ4YcQcLpUM3LwS.CHzyL&os=__OS__&imei=__IMEI__&mac=__MAC__&mac1"
        "=__MAC1__&idfa=__IDFA__&aaid=__AAID__&openudid=__OPENUDID__&androidid=__ANDROIDID__&duid=__DUID__&ip"
        "=__IP__&ua=__UA__&ts=__TS__"
    ],
    "clickm": [
        "https://g.cn.miaozhen.com/x/k=2008872&p=6vJR8&dx=0&ni=__IESID__&mo=__OS__&ns=__IP__&m0=__OPENUDID__&m0a"
        "=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__ "
    ]
}, {
    "id": "11424_182i500_52476_1",
    "impid": "20869",
    "crid": "525992",
    "price": 6070,
    "ext": {
        "adm": [
            {
                "url": "https://img30.360buyimg.com/img/jfs/t18451/89/1705564050/20987/b2559d13/5ad5a70eN49411961.jpg",
                "type": 0
            }
        ],
        "advertiser": {
            "id": 1306,
            "industry": "01",
            "subIndustry": "0103"
        },
        "linkUrl": "https://www.baidu.com",
        "style": 1010013,
        "title": "测试RTB bidding v1"
    },
    "pvm": [
        "https://g.cn.miaozhen.com/x/k=2008872&p=6vJR8&dx=0&ni=__IESID___&mo=__OS__&ns=__IP__&m0=__OPENUDID__&m0a"
        "=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__"],
    "clickm": ["https://kaola.com"],
}, {
    "id": "11424_182i500_52476_2",
    "dealid": "024200",
    "impid": "20871",
    "crid": "525990",
    "price": 7105,
    "ext": {},
    "nurl": "https://wwww.source.com/vfr/notice",
    "pvm": ["https://126.com"],
    "clickm": [
        "http://g.cn.miaozhen.com/x/k=2008872&p=6vJR8&dx=0&ni=__IESID__&mo=__OS__&ns=__IP__&m0=__OPENUDID__&m0a"
        "=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__"],
}]

_price_list = range(1200, 10000, 250)

"""
 build impid--imp map
"""


def build_impid_imp_map():
    imp_map = {}
    for bid in imps_mock:
        imp_map[bid['impid']] = bid
    return imp_map


_impid_imp_map = build_impid_imp_map()


@app.route('/reqs', methods=['POST'])
def dsp1():
    print("=============================")
    print(request.json)
    print("-----------------------------")
    resp_bids = []
    resp = {"cur": "CNY", "seatbid": [{
        "bid": resp_bids
    }], "id": "", "bidid": "", 'id': request.json['id']}
    # bidid is random string
    random_str = ''.join(
        [random.choice(string.ascii_letters + string.digits) for n in range(32)])
    resp['bidid'] = random_str
    req_imps = request.json['imp']
    if len(req_imps) > 0:
        i = 0
        for req_imp in req_imps:
            impid = req_imp['id']
            if impid in _impid_imp_map:
                # 找到对应广告位的bid
                bid_mock = _impid_imp_map[impid + ""]
                resp_bids.insert(i, bid_mock)
                bid_mock['price'] = random.choice(_price_list)
            i += 1
    print(resp)
    return jsonify(resp)

# app.run(host='0.0.0.0', port=9900)
