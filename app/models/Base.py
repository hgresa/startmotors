from app import db


class BaseMixin(object):
    @classmethod
    def create(cls, **filters):
        obj = cls(**filters)
        db.session.add(obj)
        db.session.commit()

        return obj

    @classmethod
    def get(cls, columns: list = None, **filters):
        if columns is not None:
            columns = [getattr(cls, i) for i in columns]
            obj = cls.query.with_entities(*columns).filter_by(**filters)
        else:
            obj = cls.query.filter_by(**filters)

        return obj

    @classmethod
    def get_instance(cls):
        return cls()

    def update(self, **columns):
        for key, value in columns.items():
            self.__setattr__(key, value)

        db.session.commit()


class Base(BaseMixin):
    pass
