# -*- coding:utf-8 -*-
from flask.globals import request
from flask.helpers import make_response
from flask.json import jsonify
from flask.app import Flask

# 인공지능 데이터 필요할떄 마다 꺼내서 쓰는
# AI의 결과를 어디서든 사용 가능하게
#        개발자가 만든 일반 프로그램
#        개발자가 만든 스마트폰 앱
#        개발자가 만든 웹페이지
#        분석용 Python 프로그램
#        ...

# 프로젝트, 확보한 데이터 -> 어떻게 보여주나?

# 웹서버 : 웹사이트를 보여주는 서버
# WAS(Web Application Server) : 웹서버 + 프로그램 실행 가능

# Python WAS framework (본인 PC를 WAS로 만들어주는)
#    Django
#    flask (더 가벼운, 더 많이 쓰는)

# pip install flask
###################################################
app = Flask(__name__)

# 서버는.. 요청 -> 응답

# 클라이언트가 req.test라는 주소로 GET방식 요청하면
@app.route("/req.test")
def reqTest():
    return "reqTest_Haha"

@app.route("/html.test")
def htmlTest():
    t = "<html><body>"
    t += "<marquee>Hi</marquee>"
    t += "</body></html>"
    return t

# http://IP주소:포트번호/param.test?x=123&y=234
@app.route("/param.test")
def paramTest():        # 요청 파라매터 (ex. sort=sim&...)
    xx = request.args.get("x")
    yy = request.args.get("y")
    return xx + yy
    
@app.route("/json.test")
def jsonTest():
    xx = request.args.get("x")
    yy = request.args.get("y")
    zz = int(xx) + int(yy)
    # loads() : JSON -> Python컬렉션
    # jsonify() : Python컬렉션 ->JSON
    resBody = make_response(jsonify({"sum":zz}))   # 응답 만들기(제이슨화 시키기)
    return resBody

# 자기 컴
#    IP주소 (192.168.0.189)
#    127.0.0.1 (-> 자기 컴퓨터를 가리키는 IP주소)
#    localhost
#    통신사에 연락 -> qwerty.com

if __name__=="__main__":
    app.run("0.0.0.0",  # 접속 허용 방식 (0.0.0.0->모든 IP 접근가능) : ()안에 방법으로만 접근 가능
            6547,       # 포트번호 지정 (ODB와 WAS 헷깔리지 않게)
            True)       # 이벤트 발생시 콘솔에 내용 출력
    
    
    
    