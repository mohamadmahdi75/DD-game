class object:
    bad=[]
    good=[]
    def __init__(self,name):
        self.name=name

    def __gt__(self,other):
        return self.name in other.bad

    def __repr__(self):
        return self.name


class scissors(object):
    bad=['rock']
    good=['paper']

class paper(object):
    bad=['scissors']
    good=['rock']



scissor=scissors("scissors")
papers=paper("paper")



