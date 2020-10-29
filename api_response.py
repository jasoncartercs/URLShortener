class APIResponse:
    def __init__(self, code, data):
        self.code = code
        self.data = data

    def serialize(self):
        return {"code": self.code,
                "data": self.data}
