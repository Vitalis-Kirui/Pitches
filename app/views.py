from flask import render_template
from app import app

#index view function
@app.route('/')
def index():
    """
    Index view function that returns the index html page. Which is the homepage.
    """
    main_title = 'First Impression Pitches'
    return render_template('index.html', main_title=main_title)

@app.route('/category/interview')
def interview():
    """
    Function for displaying interview pitches page.
    """
    interview_title = "This page will display interview pitches"
    return render_template('pitches/interview.html', interview_title = interview_title)

@app.route('/category/discussion')
def discussion():
    """
    Function for displaying discussion pitches page.
    """
    discussion_title = "This page will display discussion pitches"
    return render_template('pitches/discussion.html', discussion_title = discussion_title)

@app.route('/category/promotion')
def promotion():
    """
    Function for displaying promotion pitches page.
    """
    promotion_title = "This page will display promotion pitches"
    return render_template('pitches/promotion.html', promotion_title =promotion_title)

@app.route('/category/friendship')
def friendship():
    """
    Function for displaying friendship pitches page.
    """
    friendship_title = "This page will display friendship pitches"
    return render_template('pitches/friendship.html', friendship_title = friendship_title)