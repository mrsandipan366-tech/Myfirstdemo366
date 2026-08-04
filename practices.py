class good:
    summary="i dont know"
    word=10555

class bad(good):
    summary="its to easy"
    word=9999
    def __init__(self,name , roll):
        self.name=name
        self.roll=roll
        print(name, roll)

a=bad("ha bhai", 200)
print(a.summary)


