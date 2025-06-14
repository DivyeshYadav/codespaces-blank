class libraty:
    def __init__(self,list,name):
        self.blist = list
        self.name = name
        self.lendDict = {}
    def Displayb(self):
        print("There are following books in our library: ",{self.name})
        for book in self.blist:
            print(book)
    def lendbook(self,book,user):





