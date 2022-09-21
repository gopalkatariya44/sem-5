from base import app
from flask import render_template, request, redirect
from base.com.vo.category_vo import CategoryVO
from base.com.dao.category_dao import CategoryDAO


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/admin/load_category')
def admin_load_category():
    return render_template('base/category/insert_category.html')


@app.route('/admin/insert_category', methods=['POST'])
def admin_insert_category():
    name = request.form.get('categoryName')
    description = request.form.get('categoryDescription')

    category_vo = CategoryVO()
    category_dao = CategoryDAO()

    category_vo.category_name = name
    category_vo.category_description = description

    category_dao.insert_category(category_vo)
    return redirect('/admin/view_category')


@app.route('/admin/view_category')
def admin_view_category():
    dao = CategoryDAO()
    view_list = dao.view_category()
    return render_template("base/category/view_category.html", list=view_list)


@app.route('/admin/delete_category/')
def admin_delete_category():
    category_id = request.args.get('id')
    category_vo = CategoryVO()
    category_dao = CategoryDAO()
    category_vo.category_id = category_id
    category_dao.delete_category(category_vo)
    return redirect('/admin/view_category')


@app.route('/admin/edit_category/')
def admin_edit_category():
    category_id = request.args.get('id')

    category_vo = CategoryVO()
    category_dao = CategoryDAO()

    category_vo.category_id = category_id
    edit_list = category_dao.edit_category(category_vo)
    return render_template('base/category/update_category.html', list=edit_list)


@app.route('/admin/update_category/', methods=['POST'])
def admin_update_category():
    category_id = request.form.get('id')
    name = request.form.get('categoryName')
    description = request.form.get('categoryDescription')

    category_vo = CategoryVO()
    category_dao = CategoryDAO()

    category_vo.category_id = category_id
    category_vo.category_name = name
    category_vo.category_description = description

    category_dao.update_category(category_vo)
    return redirect('/admin/view_category')
