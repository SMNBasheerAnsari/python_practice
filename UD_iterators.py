
#fibonocy within N value(range):
class Fibo:
    def __init__(self,f,s,n):
        self.first=f
        self.second=s
        self.end=n

    def __iter__(self):
        self.i=self.first
        self.j=self.second
        print(self.i,self.j)
        return self

    def __next__(self):
        dummy=self.i+self.j
        if dummy<self.end:
            self.i,self.j=self.j,dummy
            return dummy
        else:
            raise StopIteration

f=Fibo(2,3,150)

for a in f:
    print(a)

#fibonocy for N values of series:
class FiboSeries():
    def __init__(self,fe,se,n):
        self.first=fe
        self.second=se
        self.n=n

    def __iter__(self):
        self.i=1 #count c=1
        return self

    def __next__(self):
        if self.i<=self.n:#count c<=n
            self.i+=1
            dummy=self.first
            self.first=self.second
            self.second=self.first+dummy
            return dummy
        
        raise StopIteration

f=FiboSeries(2,3,10)

for a in f:
    print(a)

