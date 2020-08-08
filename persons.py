class Person:
    persons = {}
    table = 'persons'
    def __init__(self, person_obj, id_=None):
        self.id_ = id_
        self.f_name = person_obj["f_name"]
        self.s_name = person_obj["s_name"]
