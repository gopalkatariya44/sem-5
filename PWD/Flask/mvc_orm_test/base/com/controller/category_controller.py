from base import app
from flask import render_template, request, redirect
from base.com.vo.category_vo import CategoryVO
from base.com.dao.category_dao import CategoryDAO


@app.route('/home')
@app.route('/')
def home():
    return render_template('hello.html')


@app.route('/add_category')
def add():
    return render_template('insert.html')


@app.route('/admin/insert_data', methods=['POST'])
def add_category():
    name = request.form.get('categoryName')
    description = request.form.get('categoryDescription')

    vo = CategoryVO()
    dao = CategoryDAO()

    vo.category_name = name
    vo.category_description = description

    dao.insert_category(vo)
    return redirect('/')


@app.route('/admin/view_data')
def view():
    dao = CategoryDAO()
    list = dao.view_category()
    print("--->", list)
    return render_template("view.html", list=list)


@app.route('/admin/delete/')
def delete():
    category_id = request.args.get('id')
    vo = CategoryVO()
    dao = CategoryDAO()
    vo.category_id = category_id
    dao.delete_category(vo)
    return redirect('/admin/view_data')


@app.route('/admin/update_page/')
def update_page():
    category_id = request.args.get('id')
    vo = CategoryVO()
    dao = CategoryDAO()
    vo.category_id = category_id
    list = dao.edit_category(vo)
    # print("-----", list[0]['category_name'])
    return render_template('update.html', list=list)


@app.route('/admin/update/', methods=['POST'])
def update():
    category_id = request.form.get('id')
    name = request.form.get('categoryName')
    description = request.form.get('categoryDescription')

    vo = CategoryVO()
    dao = CategoryDAO()

    vo.category_id = category_id
    vo.category_name = name
    vo.category_description = description

    dao.update_category(vo)
    return redirect('/admin/view_data')
