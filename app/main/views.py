from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch,User
from .forms import PitchesForm,UpdateProfile
from flask_login import login_required
from .. import db,photos

#index view function
@main.route('/')
def index():
    """
    Index view function that returns the index html page. Which is the homepage.
    """
    main_title = 'First Impression Pitches'
    return render_template('index.html', main_title=main_title)

@main.route('/category/interview')
def interview():
    """
    Function for displaying interview pitches page.
    """
    interview_title = "This page will display interview pitches"
    return render_template('pitches/interview.html', interview_title = interview_title)

@main.route('/category/discussion')
def discussion():
    """
    Function for displaying discussion pitches page.
    """
    discussion_title = "This page will display discussion pitches"
    return render_template('pitches/discussion.html', discussion_title = discussion_title)

@main.route('/category/promotion')
def promotion():
    """
    Function for displaying promotion pitches page.
    """
    promotion_title = "This page will display promotion pitches"
    return render_template('pitches/promotion.html', promotion_title =promotion_title)

@main.route('/category/friendship')
def friendship():
    """
    Function for displaying friendship pitches page.
    """
    friendship_title = "This page will display friendship pitches"
    return render_template('pitches/friendship.html', friendship_title = friendship_title)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchesForm()

    if form.validate_on_submit():
        pitch_title = form.title.data
        pitch_category = form.category.data
        pitch_itself = form.pitch.data

        new_pitch = Pitch()

    page_title = "Create new pitch."
    return render_template('new_pitch.html', pitch_form = form,page_title= page_title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))