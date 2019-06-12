from app import db

class dbmovie(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    title = db.Column( db.Text )

    def __repr__(self):
        return '<dbmovie {}>'.format(self.title)    
