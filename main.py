
class Cat:
    def __init__(self, name='', gender='', age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def set_age(self, age):
        if age > 0 and isinstance(age, int):
            self.age = age

    def set_gender(self, gender):
        if isinstance(gender, str):
            self.gender = gender

    def set_name(self, name):
        if isinstance(name, str):
            self.name = name

    def init_from_dict(self, dict):
        self.name = dict.get("name")
        self.gender = dict.get("gender")
        self.age = dict.get("age")

class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f'{getattr(self, key)}')
        return attrs

    def __repr__(self):
        if len(self.gatherAttrs()) < 3:
            return f'{self.gatherAttrs()[0]}, г.{self.gatherAttrs()[1]}'
        return f'{self.gatherAttrs()[0]}, г.{self.gatherAttrs()[1]}, статус "{self.gatherAttrs()[2]}"'

class GuestsList(AttrDisplay):
    def __init__(self, all_name, city):
        self.all_name = all_name
        self.city = city


class NewGuests(GuestsList):
    def __init__(self, all_name='', city='', status=''):
        super().__init__(all_name, city)
        self.status = status

    def init_from_dict(self, collection):
        self.all_name = collection.get("all_name")
        self.city = collection.get("city")
        self.status = collection.get("status")
