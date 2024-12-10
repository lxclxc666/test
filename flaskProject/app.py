from flask import Flask,request,render_template
from datetime import datetime
app = Flask(__name__)

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email

def datetime_format(value, format='%Y-%m-%d %H:%M:%S'):
    return datetime.strftime(value,format)
app.add_template_filter(datetime_format,"dformat")

@app.route('/')
def hello_world():
    user = User(name = "lxc",email = "lxc@jb.com")
    person = {
        "name" :"lxc",
        "email" : "lxc@jb.com"
    }
    mytime=datetime.now()
    return render_template('index.html',user = user,person = person,mytime = mytime)

@app.route("/blog")
def blog():
    return 'Welcome to my blog!'

@app.route("/blog/<int:blog_id>")
def show_blog(blog_id):
    return render_template('blog_detail.html', blog_id=blog_id )

@app.route('/blog/list')
def bolg_lost():
    page = request.args.get('page',1,int)
    return f'Blog List Page {page}'

@app.route('/child')
def extend_child():
    return render_template('child.html')

@app.route('/static')
def static_demo():
    return render_template('static_demo.html')

if __name__ == '__main__':
    app.run( host='0.0.0.0')

