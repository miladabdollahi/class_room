from keyword import kwlist

from db import session


class BaseManager:
    def __init__(self):
        self.model = None

    def contribute_to_class(self, model):
        self.model = model

    def all(self):
        instances = session.query(self.model).all()
        return instances

    def get(self, **kwargs):
        instance = session.query(self.model).filter_by(**kwargs).first()
        return instance

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        session.add(instance)
        session.commit()
        return instance

    def delete(self, **kwargs):
        instance = session.query(self.model).filter_by(**kwargs).first()
        session.delete(instance)
        session.commit()

    def update(self, update_params: dict, **kwargs):
        instance = session.query(self.model).filter_by(**kwargs).first()
        if not instance:
            instance.update(**update_params)
            session.commit()
        return instance

    def get_or_create(self, **kwargs):
        _id = kwargs.get('id', None)
        ins = self.get(id=_id)
        created = False
        if ins is None:
            ins = self.create(**kwargs)
            created = True
        return ins, created


class UserManager(BaseManager):

    def create(self, **kwargs):
        username = kwargs.get('username')
        kwargs['username'] = username.lower()
        super(UserManager, self).create(kwargs)


