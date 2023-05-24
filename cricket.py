
class Player:
    def __init__(self,name,age,country,no_maches,no_runs,no_wickets):
        self.pname=name
        self.page=age
        self.pcountry=country
        self.pmaches=no_maches
        self.pruns=no_runs
        self.pwickets=no_wickets

class Team:
    def __init__(self,np):
        self.no_players=np
        self.lpo=[]
        for i in range(self.no_players):
        
            n=input('enter player name:')
            a=input('enter player age:')
            c=input('enter player country:')
            nm=input('enter no of maches played:')
            nr=input('enter no runs:')
            nw=input('enter no of wickets taken:')
            
            obj=Player(n,a,c,nm,nr,nw)
            self.lpo.append(obj)
            print()
        #print(self.lpo)
    def mor(self):
        mxo=self.lpo[0]

        for po in self.lpo:
            if po.pruns>mxo.pruns:
                mxo=po
        return mxo.pname

    def mow(self):
        mxw=self.lpo[0]

        for po in self.lpo:
            if po.pwickets>mxw.pwickets:
                mxw=po
        return mxw.pname

    def minr(self):
        mxo=self.lpo[0]

        for po in self.lpo:
            if po.pruns<mxo.pruns:
                mxo=po
        return mxo.pname

    def minw(self):
        mxw=self.lpo[0]

        for po in self.lpo:
            if po.pwickets<mxw.pwickets:
                mxw=po
        return mxw.pname
np=int(input('enter number of player obj going to create:')) 
India=Team(np)
print('max runs',India.mor())
print('max wickets',India.mow())
print('min runs',India.minr())
print('min wickets',India.minw())
