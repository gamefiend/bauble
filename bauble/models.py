from app import db

class Grammar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(1000), unique=True)
    #categories = db.relationship('Category') 

    def __init__(self, phrase):
        self.phrase = phrase

    def __repr__(self):
        return '<Phrase: {}>'.format(self.phrase)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    # Relationships 
    # A Grammar has many Categories and each Category has many Elements
    grammar_id = db.Column(db.Integer, db.ForeignKey('grammar.id'))
    grammar = db.relationship('Grammar', backref=db.backref('categories', lazy='dynamic'))
    
    def __init__(self, name, grammar):
        self.name = name
        self.grammar = grammar

    def __repr__(self):
        return '<Category: {} >'.format(self.name)

class Element(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000))
    # Relationships
    # A Grammar has many Categories and each Category has many Elements
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('elements', lazy='dynamic'))

    def __init__(self, description, category):
        self.description = description
        self.category = category        

    def __repr__(self):
        return '<Element: {}>'.format(self.description)

