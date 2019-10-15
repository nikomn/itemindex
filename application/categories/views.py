from application import app, db
from flask import redirect, render_template, request, url_for
from application.categories.models import Category
from application.categories.forms import CategoryForm
from application.items.models import Item
from flask_login import login_required, current_user


# GET
@app.route("/categories", methods=["GET"])
@login_required
def categories_index():
    return render_template("categories/list.html", categories = Category.query.filter_by(account_id=current_user.id))

@app.route("/categories/new/", methods=["GET"])
@login_required
def categories_form():
    return render_template("categories/new.html", form = CategoryForm())

@app.route("/categories/<category_id>/modify/", methods=["GET"])
@login_required
def categories_modify(category_id):
    category = Category.query.get(category_id)
    form = CategoryForm()
    form.name.data = category.name
    return render_template("categories/modify.html", form = form, category = category)

@app.route("/categories/", methods=["POST"])
@login_required
def categories_create():
    form = CategoryForm(request.form)
    c_test = Category.query.filter_by(name=form.name.data, account_id=current_user.id).first()
    if c_test:
        return render_template("categories/new.html", form = form,
                                error = "Kategoria on jo olemassa, valitse jokin toinen nimi kategorialle!")
    else:


        if not form.validate():
            return render_template("categories/new.html", form = form)

        c = Category(form.name.data)
        c.account_id = current_user.id

        db.session().add(c)
        db.session().commit()

        # return "hello world!"
        return redirect(url_for("categories_index"))



@app.route("/categories/<category_id>/delete", methods=["POST"])
@login_required
def categories_delete(category_id):
    items = Item.query.filter_by(item_category=category_id)
    i_tmp = []
    for i in items:
        i_tmp.append(i)
    if len(i_tmp) == 0:
        category = Category.query.get(category_id)
        db.session().delete(category)
        db.session().commit()
        return redirect(url_for("categories_index"))
    else:
        #print("Virhe! Kategoria on käytössä!")
        #print("Esineet, joissa kategoriaa käytetään:")
        #for c in i_tmp:
        #    print(c)
        # return redirect(url_for("categories_index"))
        return render_template("categories/list.html", categories = Category.query.filter_by(account_id=current_user.id), error="Kategoria on käytössä! Poista ensin kategoria esineistä, joissa sitä on käytetty!")

@app.route("/categories/<category_id>/commit_changes/", methods=["POST"])
@login_required
def categories_commit_changes(category_id):

    form = CategoryForm(request.form)
    category = Category.query.get(category_id)
    category.name = form.name.data
    db.session().commit()

    return redirect(url_for("categories_index"))
