from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import InputRequired
 
class ContactForm(FlaskForm):
	name = TextField("Name",  [InputRequired()])
	email = TextField("Email",  [InputRequired()])
	subject = TextField("Subject",  [InputRequired()])
	message = TextAreaField("Message",  [InputRequired()])
	submit = SubmitField("Submit")