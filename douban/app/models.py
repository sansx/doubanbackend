from app import db

class dbmovie(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    title = db.Column( db.Text )
    rate = db.Column( db.Float(4,2) )
    rateNum = db.Column( db.Integer )

    def __repr__(self):
        return '<dbmovie {}>'.format(self.title)    
