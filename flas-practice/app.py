#2021.2.10
from flask import Flask,escape,url_for

#__name__属性为当是本文件时为__main__，当调用时为该文件文件名
app=Flask(__name__)

@app.route("/hello")
def hello():
    return "hello world"

#多个装饰器装饰可以绑定多个url
@app.route("/photo")
@app.route("/pic")
def pic():
    #浏览器会自动解析返回值中的html代码
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

#在url中定义变量部分
@app.route("/user/<name>")
def user_page(name):
    #用户输入的数据会包含恶意代码，所以不能直接作为响应返回，需要使用 Flask 提供的 escape() 函数对
    # name 变量进行转义处理，比如把 < 转换成 &lt;。这样在返回响应时浏览器就不会把它们当做代码执行。
    return 'User:%s'%escape(name)

@app.route("/test")
def test_url_for():
    #获取函数名对应的url
    print(url_for('hello'))
    print(url_for('user_page',name="syy"))
    print(url_for('user_page',name="yyf"))
    print(url_for('test_url_for'))
    #该页面的返回值
    return 'Test_page'
# 2.11
from flask import render_template
name = 'SYY'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
@app.route("/")
def index():
    return render_template('index.html',name=name,movies=movies)

if __name__=="__main__":
    app.run(debug=True)