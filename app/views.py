import datetime
from app import app,db
from flask import render_template,redirect,url_for,flash,request,abort
from werkzeug.security import generate_password_hash,check_password_hash #used to hash password to unreadable string
from flask_login import login_required,logout_user,login_user,current_user
from app import forms
from .models import User,Pitches

LoginForm=forms.LoginForm
RegisterForm=forms.RegisterForm
# UpdateForm=forms.UpdateForm
PitchForm=forms.PitchForm


@app.route('/')
def index():
    db.create_all()
    pitches=Pitches.query.all()
    return  render_template('homepage.html',pitches=pitches)

@app.route('/about')
def about():
    
    return  render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and check_password_hash(user.password,form.password.data):
            login_user(user,)
            next_page=request.args.get('next')
            flash('Login Successfully','success')
            return redirect(next_page) if next_page else redirect (url_for('index'))
        flash('Invalid email or password','success')
    return render_template('login.html',form = form)

@app.route('/register',methods = ["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,
        username = form.username.data,
         password = generate_password_hash(form.password.data))

        db.session.add(user)
        db.session.commit()
        flash('Account created successfully', 'success')

        return redirect(url_for('login'))

    return render_template('signup.html',form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/pitch',methods = ["GET","POST"])
@login_required
def pitch():
    form =PitchForm()
    if form.validate_on_submit():
        pitch=Pitches(title=form.title.data,
                      pitch=form.pitch.data,
                      user=current_user
                      )
        db.session.add(pitch)
        db.session.commit()
        
        flash('Pitch successfully created','sucess')
        return redirect (url_for('index'))
    return render_template ('pitch.html',form=form)

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')