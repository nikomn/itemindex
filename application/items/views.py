from application import app, db
from flask import redirect, render_template, request, url_for
from application.items.models import Item
from application.categories.models import Category
# from application.item_category.models import ItemCategory
from application.items.forms import ItemForm, ModifyItemForm, ItemSearchForm
from flask_login import login_required, current_user

#GET
@app.route("/items", methods=["GET"])
@login_required
def items_index():
    return render_template("items/list.html", items = Item.query.filter_by(account_id=current_user.id), categories = Category.query.filter_by(account_id=current_user.id))

@app.route("/items/search/", methods=["GET"])
@login_required
def items_search():
    form = ItemSearchForm()
    form.item_category.choices = [(c.id, c.name) for c in Category.query.order_by('name').filter_by(account_id=current_user.id)]
    return render_template('items/search.html', form=form)

@app.route("/items/search/results", methods=["GET"])
@login_required
def items_show_results():
    return render_template("items/list.html", items = Item.query.filter_by(account_id=current_user.id), categories = Category.query.filter_by(account_id=current_user.id))


@app.route("/items/new/", methods=["GET"])
@login_required
def items_form():
    category_list = Category.query.order_by('name').filter_by(account_id=current_user.id)
    c_list = []
    for c in category_list:
        c_list.append(c)

    if len(c_list) == 0:
        c = Category("Ei kategoriaa")
        c.account_id = current_user.id
        db.session().add(c)
        db.session().commit()

    form = ItemForm()

    form.item_category.choices = [(c.id, c.name) for c in Category.query.order_by('name').filter_by(account_id=current_user.id)]
    return render_template('items/new.html', form=form)


@app.route("/items/modify/<item_id>/", methods=["GET"])
@login_required
def items_modify(item_id):
    item = Item.query.get(item_id)
    category = Category.query.get(item.category_id)

    form = ItemForm()
    form.item_category.choices = [(c.id, c.name) for c in Category.query.order_by('name').filter_by(account_id=current_user.id)]
    form.item_category.data = category.id
    form.expired.data = item.expired


    return render_template("items/modify.html", form = form, item = item)

# POST...

@app.route("/items/<item_id>/", methods=["POST"])
@login_required
def items_set_done(item_id):

    t = Item.query.get(item_id)
    t.expired = True
    db.session().commit()

    return redirect(url_for("items_index"))



@app.route("/items/<item_id>/delete", methods=["POST"])
@login_required
def items_delete(item_id):
    item = Item.query.get(item_id)
    db.session().delete(item)
    db.session().commit()

    return redirect(url_for("items_index"))


@app.route("/items/", methods=["POST"])
@login_required
def items_create():

    form = ItemForm(request.form)
    form.item_category.choices = [(c.id, c.name) for c in Category.query.order_by('name').filter_by(account_id=current_user.id)]


    if not form.validate():
        return render_template("items/new.html", form = form)


    i = Item(form.name.data, form.expired.data)
    category = Category.query.get(form.item_category.data)
    # i.item_category = category.id
    # i.categories.append(category)
    # i.item_category.append(category)
    i.account_id = current_user.id
    i.category_id = category.id

    db.session().add(i)
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/<item_id>/commit_changes/", methods=["POST"])
@login_required
def items_commit_changes(item_id):
    form = ItemForm(request.form)
    # item = request.item
    item = Item.query.get(item_id)
    form.item_category.choices = [(c.id, c.name) for c in Category.query.order_by('name').filter_by(account_id=current_user.id)]

    if not form.validate:
        return render_template("items/modify.html", form = form, item = item)

    item.name = form.name.data
    category = Category.query.get(form.item_category.data)
    # item.item_category = category.id
    item.category_id = category.id
    # item.item_category = form.item_category.data
    item.expired = form.expired.data

    db.session().commit()

    return redirect(url_for("items_index"))
