class parent:
    def __init__(self ):
        print("conparent")

    def fun(self):
        self.no=69
        print(self.no)

class child(parent):
    def __init__(self):
        super().__init__()
    def fun(self):
        self.no=77
        super().fun()
ob= child()
ob.fun()

