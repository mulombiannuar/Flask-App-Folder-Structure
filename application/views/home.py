from flask import Blueprint, render_template
from application.forms.post_form import PostForm

# create home blueprint
home = Blueprint('home', __name__)

# define the home route
@home.route('/', methods=['GET'])
def home_page():
    form = PostForm()
    return render_template('home/home.html', form=form)


