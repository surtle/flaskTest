from app import db

#====================================================================
# id - unique ID for the user
# nickname - unique username for the user
# email - user's email
# totalVal - the total amount of money recorded
# categories - the separate categories the user has specified
#====================================================================

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  social_id = db.Column(db.String(64), nullable=False, unique=True)
  nickname = db.Column(db.String(64), nullable=False) 
  email = db.Column(db.String(120), nullable=True) 
  totVal = db.Column(db.Float) 
  categories = db.relationship('Category', backref=db.backref('user',
        lazy='joined'), lazy='dynamic')

  def __init__(self, social_id, nickname, email, totVal):
    self.social_id = social_id
    self.nickname = nickname
    self.email = email
    self.totVal = totVal

  def __repr__(self):
    return '<User %r>' % (self.nickname) 

#====================================================================
# id - unique id for Category 
# label - category's label
# value - the amount of money recorded for this category
# userID - id field that links back to user
#====================================================================

class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  label = db.Column(db.String(64))
  value = db.Column(db.Float)
  userID = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __init__(self, label, value, user):
    self.label = label
    self.value = value
    self.userID = user.id

  def __repr__(self):
    return '<Category %r>' % (self.label)


