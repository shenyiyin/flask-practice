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

    return 'Test_page'
if __name__=="__main__":
    app.run(debug=True)