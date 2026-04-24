from flask import Flask,render_template
from datetime import datetime 
app = Flask(__name__)

@app.template_filter("handle_time")
def handle_time(time):
    if isinstance(time,datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp<60:
            return "刚刚"
        elif timestamp>=60 and timestamp<60*60:
            minutes = timestamp/60
            return f"{int(minutes)}分钟前"
        elif timestamp>=60*60 and timestamp<60*60*24:
            hours=timestamp/(60*60)
            return f"{int(hours)}小时前"
        elif timestamp>=60*60*24 and timestamp<60*60*24*30:
            days=timestamp/(60*60*24)
            return f"{int(days)}天前"
        else:
            return time.strftime('%Y/%M/%d %H:%M')
    else:
        return time

@app.route('/')
def index():
    tmp_time = datetime(2026,4,10,10,10,10)
    return render_template('tmp3.html',tmp_time=tmp_time)

if __name__ == '__main__':
    app.run(debug=True)

