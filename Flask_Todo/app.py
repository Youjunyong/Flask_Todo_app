import os
from forms import RegisterForm, LoginForm
from flask import Flask,request,render_template , redirect, session
from api_v1 import api as api_v1
from models import db, Myuser, Todo

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/api/v1')

@app.route('/',methods=['GET'])
def home():
    userid = session.get('userid') 
    todos = []
    if userid : 

        myuser = Myuser.query.filter_by(userid=userid).first()
        todos = Todo.query.filter_by(myuser_id=myuser.id)
        return render_template('home.html',userid=userid,todos=todos)
    else :
        return redirect('/error1')
    
    
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['userid'] = form.data.get('userid')
        return redirect('/')
        
    return render_template('login.html', form=form)

@app.route('/logout',methods=['GET'])
def logout():
    session.pop('userid',None)
    return redirect('/')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        myuser = Myuser()
        myuser.userid = form.data.get('userid')
        myuser.password = form.data.get('password')

        db.session.add(myuser)
        db.session.commit()
        
        return redirect('/login')

    return render_template('register.html', form=form)
@app.route('/error1')
def error():
    return render_template('error1.html')


basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir,'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jawelfusidufhxkcljvhwiul'

db.init_app(app)
db.app = app
db.create_all()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True    )
