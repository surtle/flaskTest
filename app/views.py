from flask import render_template, flash, redirect
from app import app
from flask_login import LoginManager, UserMixin, login_user, logout_user, \
       current_user
from .forms import LoginForm

#====================================================================
# Loads user
#====================================================================
@lm.user_loader
def load_user(id):
  return User.query.get(int(id))

#====================================================================
# Function returns the html template for the home page
#====================================================================
@app.route('/')
@app.route('/index')
def index():
  # dummy objects TODO delete later
	user = {'nickname': 'Miguel'}	#fake user
	posts = [  # fake array of posts
          { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
          },
          { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
          }
        ]
	return render_template('index.html', 
                         user=user, 
                         posts=posts)

#====================================================================
# Function returns the html template for the login page
#====================================================================
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
      flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
      return redirect('/index')
  return render_template('login.html', 
                         title='Sign In', 
                         form=form,
                         providers=app.config['OPENID_PROVIDERS'])

#====================================================================
# Function returns the html template for the login page
#====================================================================
@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))

#====================================================================
# Function returns the html template for the login page
#====================================================================
@app.route('/authorize/<provider>')
def oauth_authorize(provider):
  if not current_user.is_anonymous:
    return redirect(url_for('index'))
  oauth = OAuthSignIn.get_provider(provider)
  return oauth.authorize()

#====================================================================
# Function returns the html template for the login page
#====================================================================
@app.route('/callback/<provider>')
def oauth_callback(provider):

  if not current_user.is_anonymous:
    return redirect(url_for('index'))

  oauth = OAuthSignIn.get_provider(provider)
  social_id, username, email = oauth.callback() 

  if social_id is None:
    flash('Authentication failed.')
    return redirect(url_for('index'))

  user = User.query.filter_by(social_id=social_id).first()

  if not user:
    user = User(social_id, username, email, 0)
    #db.session.add(user)
    #db.session.commit()

  login_user(user, True)
  return redirect(url_for('index'))

 
