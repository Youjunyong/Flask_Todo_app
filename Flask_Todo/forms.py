from models import Myuser
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    userid= StringField('userid', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    repassword = PasswordField('repasswrod', validators=[DataRequired()])



class LoginForm(FlaskForm):
    class UserPassword(object):
        def __init__(self, message=None):
            self.message = message

        def __call__(self, form, field):
            userid = form['userid'].data
            password = field.data

            myuser = Myuser.query.filter_by(userid=userid).first()
            if not myuser :
                raise ValueError("잘못된 아이디 입니다.")
            if myuser.password != password:
                raise ValueError("잘못된 비밀번호 입니다.")
            

    userid = StringField('userid', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), UserPassword()])

