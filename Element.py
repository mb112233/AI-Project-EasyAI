class ElementClass:

    def __init__(self,type):
        self.type=type

    def get_type(self):
        return self.type

    def __str__(self):
        return self.type

    def __repr__(self):
        return self.__str__()

    def destroy(self):
        if (self.type=='*'):
            self.type='X'
            return 'hit'
        else:
            return 'miss'
