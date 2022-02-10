# import classes 
# from flask import render_template,redirect,url_for, flash,request
# from flask_login import login_required,current_user
# from ..models import User
# from app.auth import auth
# from models import User
# from flask_login import login_user,logout_user,login_required
# from .forms import LoginForm,RegisterForm
# from app import db

# @auth.route('/login',methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email = form.email.data).first()
#         if user is not None and user.verify_password(form.password.data):
#             login_user(user,form.remember.data)
#             return redirect(request.args.get('next') or url_for('main.index'))

#         flash('Invalid author or Password')

#     return render_template('login.html',form = form)

# @auth.route('/register',methods = ["GET","POST"])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         user = User(email = form.email.data,
#          author = form.author.data,
#          password = form.password.data)

#         db.session.add(user)
#         db.session.commit()

#         return redirect(url_for('auth.login'))

#     return render_template('auth/signup.html',registration_form = form)

# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for("main.index"))
