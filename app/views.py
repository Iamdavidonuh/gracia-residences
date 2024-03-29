from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_mail import Message
from app import forms, mail

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/", methods=["GET", "POST"])
def index():
    form = forms.ContactUsForm(request.form)
    if request.method == "POST" and form.validate():

        postfix_message = f"Sent by: User details - {form.name.data}, {form.email.data}"

        message_body = f"{form.message.data} \n\n\n{postfix_message}"

        message = Message(
            body=message_body,
            subject=form.subject.data,
            sender=("Gracia Residences", "info@graciaresidences.com"),
            reply_to=(form.name.data, form.email.data),
        )
        message.add_recipient("info@graciaresidences.com")
        mail.send(message)
        flash(
            "We've recevied your message. Someone from our team will contact you soon."
        )
        return redirect(f'{url_for("home.index")}#contact-us')
    return render_template("index.html", form=form)
