from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


class MyForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    textarea = TextAreaField('Say Something')
    radios = RadioField('Radios', default='option3',
                        choices=[('option1', 'Male'), ('option2', 'Female'), ('option3', 'Other')])
    selects = SelectField('Who will win the Euro?', choices=[('1', 'Russia'), ('2', 'Belgium'), ('3', 'England')])


@app.route('/', methods=['GET', 'POST'])
def form():
    form = MyForm()

    if form.validate_on_submit():
        return render_template('results.html', email=form.email.data, password=form.password.data,
                               textarea=form.textarea.data, radios=form.radios.data, selects=form.selects.data)
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
