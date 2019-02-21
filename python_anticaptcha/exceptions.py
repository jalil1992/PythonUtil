        self.error_code = error_code



        self.error_id = error_id
        self.error_code = error_code

        self.error_description = error_description
        self.cls = cls
        self.error_code = error_code

        self.width = width
        self.error_id = error_id
        self.error_code = error_code



    def __init__(self, error_id, error_code, error_description, *args):
    def __init__(self, error_id, error_code, error_description, *args):

    def __init__(self, width):
        msg = 'Missing name data in {0}. Provide {0}.__init__(name="X") or {0}.serialize(name="X")'.format(str(self.cls))
