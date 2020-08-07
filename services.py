class Service:
    services = {}
    table = 'services'
    def __init__(self, service_obj, id_=None):
        self.id_ = id_
        self.name = service_obj["name"]
        self.url = service_obj["url"]
        self.description = service_obj["description"]
