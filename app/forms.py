import wtforms


class ContactUsForm(wtforms.Form):

    name = wtforms.StringField("Name", [wtforms.validators.DataRequired()])
    email = wtforms.EmailField("Email", [wtforms.validators.DataRequired()])
    subject = wtforms.StringField("Subject", [wtforms.validators.DataRequired()])
    message = wtforms.TextAreaField("Message", [wtforms.validators.DataRequired()])
