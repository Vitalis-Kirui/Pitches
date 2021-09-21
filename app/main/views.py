from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from wtforms import form
from ..models import Pitch,User,Comments
from .forms import PitchesForm,UpdateProfile,CommentForm
from .. import db,photos

#index view function
@main.route('/')
def index():
    """
    Index view function that returns the index html page. Which is the homepage.
    """
    all_pitches = Pitch.query.order_by('id').all()
    print(all_pitches)

    main_title = 'First Impression Pitches'
    return render_template('index.html', main_title=main_title,all_pitches=all_pitches)

@main.route('/category/interview', methods=['GET'])
def interview():
    """
    Function for displaying interview pitches page.
    """
    pitches = Pitch.get_pitches('interview')

    interview_title = "Interview Pitches"

    return render_template('pitches/interview.html', interview_title = interview_title, interview_pitches = pitches)

@main.route('/category/discussion', methods=['GET'])
def discussion():
    """
    Function for displaying discussion pitches page.
    """
    pitches = Pitch.get_pitches('discussion')

    discussion_title = "This page will display discussion pitches"
    return render_template('pitches/discussion.html', discussion_title = discussion_title, discussion_pitches = pitches)

@main.route('/category/promotion', methods=['GET'])
def promotion():
    """
    Function for displaying promotion pitches page.
    """
    pitches = Pitch.get_pitches('promotion')

    promotion_title = "This page will display promotion pitches"
    return render_template('pitches/promotion.html', promotion_title =promotion_title, promotion_pitches = pitches)

@main.route('/category/friendship', methods=['GET'])
def friendship():
    """
    Function for displaying friendship pitches page.
    """
    pitches = Pitch.get_pitches('friendship')

    friendship_title = "This page will display friendship pitches"
    return render_template('pitches/friendship.html', friendship_title = friendship_title, friendship_pitches = pitches)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchesForm()

    if form.validate_on_submit():
        title = form.pitch_title.data
        category = form.pitch_category.data
        user_pitch = form.pitch_itself.data

        new_pitch = Pitch(pitch_title=title, pitch_category=category, pitch_itself=user_pitch, user=current_user)

        #save pitch
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

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

@main.route('/comment/<int:id>', methods=['POST', 'GET'])
@login_required
def post_comment(id):
    pitche = Pitch.getPitchId(id)
    comments = Comments.get_comments(id)

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.user_comment.data

        new_comment = Comments(comment_itself=comment,user_id=current_user.id,
                               pitches_id=pitche.id)

        new_comment.save_comment()

        return redirect(url_for('main.post_comment', id=pitche.id))
    return render_template('comments.html',
                           commentform=form,
                           comments=comments,
                           pitch=pitche)