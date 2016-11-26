# -*- coding: utf-8 -*-

from flask import request
from flask import url_for
from flask import session
from flask import redirect
from flask import flash
from flask import render_template
from . import blueprint
from core.database import db
from core.models import Book
from dateutil import parser


@blueprint.route('/', methods=['GET'])
def book_store_index():
    if 'login_user' in session.keys():
        return redirect(url_for("bookstore.book_store_list_books"))
    else:
        return redirect(url_for("bookstore.book_store_login"))


@blueprint.route('/login', methods=['GET', 'POST'])
def book_store_login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            session['login_user'] = 'admin'
        else:
            flash("Username or password not correct.")

        return redirect(url_for("bookstore.book_store_index"))

    else:
        return render_template('login.html')


@blueprint.route('/logout')
def book_store_logout():
    if 'login_user' in session.keys():
        session['login_user'] = None
        session.pop('login_user')

    return redirect(url_for('bookstore.book_store_login'))


@blueprint.route("/list_books", methods=['GET'])
def book_store_list_books():
    books = Book.query.all()
    return render_template('list_book.html', books=books)


@blueprint.route("/add_book", methods=['GET', 'POST'])
def book_store_add_book():
    if request.method == 'POST':
        print request.form['created_at']
        fileds = {
            "name_en": request.form['name_en'],
            "name_ch": request.form['name_ch'],
            "created_at": parser.parse(request.form['created_at'])
        }
        book = Book(**fileds)
        db.session.add(book)
        db.session.commit()
        flash("Add a new book")
        return redirect(url_for('bookstore.book_store_list_books'))
    else:
        return render_template('add_book.html')
