# 自定义模板过滤器
from flask import Flask, render_template
app = Flask(__name__)

@app.template_filter('rep')
def rep(value):
    value = value.replace('mama','baba')
    return value

@app.route('/')
def index():
    info = '==========小脑斧喜欢mama！=========='
    return render_template('tmp2.html',info=info)

if __name__ == '__main__':
    app.run(debug=True)
