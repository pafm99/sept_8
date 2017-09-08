class Team(object):
    def __init__(self,name,city,color):
        self.name = name
        self.city = city
        self.color = color
        self.players = []
        
    def display(self):
        for player in self.players:
            print "Team Players:", player.p_name, player.j_num
            return self

class Player(object):
    def __init__(self, p_name, j_num):
        self.p_name = p_name
        self.j_num = j_num

sea = Team("seahawks","seattle","blue")
russ = Player("Russ",3)
sea.players.append(russ)
sea.display()