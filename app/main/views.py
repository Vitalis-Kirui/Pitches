from flask import render_template
from . import main
from ..models import Pitch
from .forms import PitchesForm

# Pitch = pitch.Pitch

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

@main.route('/pitches/pitch/new', methods = ['GET','POST'])
def new_pitch():
    form = PitchesForm()

    if form.validate_on_submit():
        pitch_title = form.title.data
        pitch_category = form.category.data
        pitch_itself = form.pitch.data

        new_pitch = Pitch(pitch_title,pitch_category,pitch_itself)
        new_pitch.save_pitch()

    return render_template('new_pitch.html', pitch_form = form)