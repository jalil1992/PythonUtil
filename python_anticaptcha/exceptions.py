



        self.error_id = error_id


        self.error_description = error_description
        self.cls = cls


        self.width = width
        self.error_id = error_id
        self.error_code = error_code



        msg = 'Missing name data in {0}. Provide {0}.__init__(name="X") or {0}.serialize(name="X")'.format(str(self.cls))
    def __init__(self, error_id, error_code, error_description, *args):
    def __init__(self, error_id, error_code, error_description, *args):
    def __init__(self, width):
        msg = 'Missing name data in {0}. Provide {0}.__init__(name="X") or {0}.serialize(name="X")'.format(str(self.cls))