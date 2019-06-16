from app import db


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(model, page, per_page, order="id", isDesc=False, **kwargs):
        resources = model.query.order_by(getattr(model, order) if isDesc else getattr(
            model, order).desc()).paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            'page': page,
            'per_page': per_page,
            'total_pages': resources.pages,
            'total_items': resources.total
        }
        return data


class dbmovie(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    rate = db.Column(db.Float(4, 2))
    rateNum = db.Column(db.Integer)

    def __repr__(self):
        return '<dbmovie {}>'.format(self.title)

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'rate': float(self.rate),
            'rateNum': self.rateNum
        }

        print(data)

        return data
