import base64


class Creation:
    def __init__(self, id, name, image:bytes, description, amound, created_at):
        self.id = id
        self.name = name
        self.image = image
        self.description = description
        self.amound = amound
        self.created_at = created_at


