from application import app, db
from flask import redirect, render_template, request, url_for
from application.categories.models import Category
from application.categories.forms import CategoryForm
from flask_login import login_required, current_user

@app.route("/categories", methods=["GET"])
@login_required
def categories_index():
    # return render_template("items/list.html", items = Item.query.all())
    return render_template("categories/list.html", categories = Category.query.filter_by(account_id=current_user.id))

@app.route("/categories/new/")
@login_required
def categories_form():
    # return render_template("items/new.html")
    return render_template("categories/new.html", form = CategoryForm())

@app.route("/categories/", methods=["POST"])
@login_required
def categories_create():
    # t = Item(request.form.get("name"))

    form = CategoryForm(request.form)

    if not form.validate():
        return render_template("categories/new.html", form = form)

    c = Category(form.name.data)
    # c.item_category
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()

    # return "hello world!"
    return redirect(url_for("categories_index"))

@app.route("/categories/<category_id>/modify", methods=["POST"])
@login_required
def categories_modify(category_id):
    # return render_template("items/list.html", items = Item.query.all())
    # , form = ItemForm()
    category = Category.query.get(category_id)
    # Item.query.
    # form = ModifyItemForm()
    form = CategoryForm()
    # form.name.value = item.name
    # form.expired.value = item.expired
    # form = ModifyItemForm()
    if not form.validate():
        # return render_template("items/modify.html", form = form, item = Item.query.get(item_id))
        return render_template("categories/modify.html", form = form, category = category)
    # return render_template("items/modify.html", form = form, item = Item.query.get(item_id))

    # i = Item(form.name.data)
    category.name = form.name.data
    # item.account_id = current_user.id

    # db.session().add(i)
    db.session().commit()

    # return "hello world!"
    return redirect(url_for("categories_index"))

@app.route("/categories/<category_id>/delete", methods=["POST"])
# @login_required
def categories_delete(category_id):
    category = Category.query.get(category_id)
    db.session().delete(category)
    db.session().commit()

    # return "hello world!"
    return redirect(url_for("categories_index"))
