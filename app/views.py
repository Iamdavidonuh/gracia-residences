from flask import Blueprint, redirect, render_template, request, url_for
from app import forms

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/", methods=["GET", "POST"])
def index():
    print("getting files \n\n\n\n\n")
    form = forms.ContactUsForm(request.form)
    if request.method == "POST" and form.validate():
        print(form, "\n\n\n\n\n")
        return redirect(url_for("home.index"))
    return render_template("index.html", form=form)
