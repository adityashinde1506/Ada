

class Interface(object):

    """
        Interface object for ensuring a common way to access all modules.
    """

    def __init__(self,name):
        self.name=name

    def init(self,*args,**kwargs):
        raise NotImplementedError(f"init method not implemented for {self.name}")

    def run(self,*args,**kwargs):
        raise NotImplementedError(f"run method not implemented for {self.name}")
