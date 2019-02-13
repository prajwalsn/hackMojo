from wtforms import Form, StringField , TextAreaField ,IntegerField, PasswordField, validators

class RegisterForm(Form):
    email = StringField('Email', [validators.Length(min=6 , max = 50)])
    typeid = IntegerField('TypeId')
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passswords do not match')
    ])
    confirm = PasswordField('Confirm Password')