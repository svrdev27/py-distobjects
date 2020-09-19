import inspect
from distobjects.exceptions import ValidationError
from .fields import AbstractField

class DObjectMeta(type):
    def __new__(mcls, name, bases, attrs):
        newattrs = dict(attrs)
        meta = newattrs.get('Meta')
        if not inspect.isclass(meta):
            raise ValidationError("{} does not have Meta Defined".format(name))

        if not getattr(meta,'backend', False) and not getattr(meta,'_is_abs', False):
            raise ValidationError("{} Meta does not have backend".format(name))
        return super(DObjectMeta, mcls).__new__(mcls, name, bases, newattrs)


class DObject(object, metaclass=DObjectMeta):
    class Meta:
        _is_abs = True
        backend = None
        key_space = None

    def get_backend(self):
        return self.Meta.backend

    def get_object_key(self):
        key_space = getattr(self.Meta, 'key_space', None) or type(self).__name__
        return key_space+":"+str(self.id)

    def clear(self):
        self.get_backend().clear_group(self.get_object_key())

    def __init__(self, id):
        self.id = id

    def __getattribute__(self, attr):
        if attr.startswith('_'):
            return object.__getattribute__(self, attr)
        value = super().__getattribute__(attr)
        field = getattr(self.__class__,attr, None)
        if isinstance(field, AbstractField):
            return field.deserialize(
                self.get_backend().fetch_value(
                    group=self.get_object_key(),
                    key=attr
                    ))
        return value

    def __setattr__(self, name, value):
        field = getattr(self.__class__,name, None)
        if isinstance(field, AbstractField):
            self.get_backend().save_value(
                group=self.get_object_key(),
                key=name,
                value=field.serialize(value)
                )

        else:
            super().__setattr__(name, value)
