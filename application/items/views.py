from application import app, db
from flask import redirect, render_template, request, url_for
from application.items.models import Item
from application.categories.models import Category
from application.items.forms import ItemForm, ModifyItemForm
from flask_login import login_required, current_user

@app.route("/items", methods=["GET"])
@login_required
def items_index():
    # return render_template("items/list.html", items = Item.query.all())
    return render_template("items/list.html", items = Item.query.filter_by(account_id=current_user.id), categories = Category.query.filter_by(account_id=current_user.id))

@app.route("/items/new/")
@login_required
def items_form():
    # return render_template("items/new.html")
    # return render_template("items/new.html", form = ItemForm())
    category_list = Category.query.order_by('name').filter_by(account_id=current_user.id)
    c_list = []
    for c in category_list:
        c_list.append(c)

    if len(c_list) == 0:
        c = Category("Ei kategoriaa")
        # c.account_id = self.id
        c.account_id = current_user.id
        db.session().add(c)
        db.session().commit()

    form = ItemForm()

    form.item_category.choices = [(c.id, c.name) for c in Category.query.order_by('name').filter_by(account_id=current_user.id)]
    return render_template('items/new.html', form=form)
    # if request.method == "POST" and not form.validate():
    #     return render_template('items/new.html', form=form)
    # # return render_template("items/modify.html", form = form, item = item)
    # elif request.method == "GET":
    #     return render_template('items/new.html', form=form)
    # if not form.validate_on_submit():
    #     return render_template('items/new.html', form=form)
    #elif not form.validate() and request.method == "POST":
        #return render_template('items/new.html', form=form)

@app.route("/items/<item_id>/", methods=["POST"])
@login_required
def items_set_done(item_id):

    t = Item.query.get(item_id)
    t.expired = True
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/<item_id>/modify", methods=["POST"])
@login_required
def items_modify(item_id):
    item = Item.query.get(item_id)
    category = Category.query.get(item.item_category)

    form = ItemForm()
    form.item_category.choices = [(c.id, c.name) for c in Category.query.order_by('name').filter_by(account_id=current_user.id)]
    form.item_category.data = category.id


    if not form.validate_on_submit():
        return render_template("items/modify.html", form = form, item = item)
    # return render_template("items/modify.html", form = form, item = Item.query.get(item_id))

    # i = Item(form.name.data)
    item.name = form.name.data
    item.item_category = form.item_category.data
    item.expired = form.expired.data
    # item.account_id = current_user.id
    # i.item_category = form.item_category.data
    # i.expired = form.expired.data
    # i.account_id = current_user.id

    # db.session().add(i)
    db.session().commit()

    # return "hello world!"
    return redirect(url_for("items_index"))

@app.route("/items/<item_id>/delete", methods=["POST"])
# @login_required
def items_delete(item_id):
    item = Item.query.get(item_id)
    db.session().delete(item)
    db.session().commit()

    # return "hello world!"
    return redirect(url_for("items_index"))


    # return render_template("items/modify.html", form = ModifyItemForm(), item = Item.query.get(item_id))


@app.route("/items/", methods=["POST"])
@login_required
def items_create():

    form = ItemForm(request.form)
    form.item_category.choices = [(c.id, c.name) for c in Category.query.order_by('name').filter_by(account_id=current_user.id)]


    if not form.validate():
        return render_template("items/new.html", form = form)


    i = Item(form.name.data)
    i.item_category = form.item_category.data
    i.expired = form.expired.data
    i.account_id = current_user.id

    db.session().add(i)
    db.session().commit()

    # return "hello world!"
    return redirect(url_for("items_index"))
