from application import app, db
from flask import redirect, render_template, request, url_for
from application.items.models import Item
from application.items.forms import ItemForm
from flask_login import login_required, current_user

@app.route("/items", methods=["GET"])
@login_required
def items_index():
    # return render_template("items/list.html", items = Item.query.all())
    return render_template("items/list.html", items = Item.query.filter_by(id=current_user.id))

@app.route("/items/new/")
@login_required
def items_form():
    # return render_template("items/new.html")
    return render_template("items/new.html", form = ItemForm())

@app.route("/items/<item_id>/", methods=["POST"])
@login_required
def items_set_done(item_id):

    t = Item.query.get(item_id)
    t.expired = True
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/", methods=["POST"])
@login_required
def items_create():
    # t = Item(request.form.get("name"))

    form = ItemForm(request.form)

    if not form.validate():
        return render_template("items/new.html", form = form)

    i = Item(form.name.data)
    i.expired = form.expired.data
    i.account_id = current_user.id

    db.session().add(i)
    db.session().commit()

    # return "hello world!"
    return redirect(url_for("items_index"))
