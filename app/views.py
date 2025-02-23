from app import app
from flask import render_template, request, redirect, url_for, flash
from datetime import datetime
import json

# JSON data as a dictionary
user_data = {
    "name": "Mary Jane",
    "username": "@mjane",
    "location": "Kingston, Jamaica",
    "joined": "2018-01-01",
    "posts": "7",
    "following": "100",
    "followers": "250"
}

# Accessing values
name = user_data["name"]
username = user_data["username"]
location = user_data["location"]
joinedraw = user_data["joined"]
posts = user_data["posts"]
following = user_data["following"]
followers = user_data["followers"]

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name=name)

"""returns the date formatted as Month, Year (e.g. Feb, 2021)"""
def format_date_joined(date_string):
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")  # Convert string to datetime object
    return "Joined " + date_obj.strftime("%b, %Y")  # Format as "Month, Year"


joined = format_date_joined(joinedraw)

@app.route('/profile/')
def profile():
    """Render the website's profile page."""
    return render_template('profile.html', name=name, username=username, location=location,\
     joined=joined, posts=posts, following=following, followers=followers)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
