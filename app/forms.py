import wtforms


class ContactUsForm(wtforms.Form):

    name = wtforms.StringField("Name", [wtforms.validators.DataRequired()])
    email = wtforms.EmailField("Email", [wtforms.validators.DataRequired()])
    subject = wtforms.EmailField("Email", [wtforms.validators.DataRequired()])
    message = wtforms.TextAreaField("Message", [wtforms.validators.DataRequired()])
