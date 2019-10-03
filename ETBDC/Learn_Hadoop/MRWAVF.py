from mrjob.step import MRStep
from mrjob.job import MRJob
from statistics import mean

class MRJWAV(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper1, reducer=self.reducer1),
            MRStep(mapper=self.mapper2, reducer=self.reducer2),
            MRStep(mapper=self.mapper3, reducer=self.reducer3),
        ]
    def mapper1(self, key, line):
        words = line.split(' ')
        for word in words:
            yield word, 1
            
    def reducer1(self, word, count_one):
        f=list(count_one)
        yield 'a', len(word)*sum(f)
        yield 'b', sum(f)
        
    def mapper2(self, ky, Sm):
        #f=list(line)
        #yield key*sum(f), sum(f)
        #yield 1, Sm
        #ul=list()
        #ll=0
        #if (ky == 'a'):
            #ul+=Sm
        #if (ky == 'b'):
            #ll+=Sm
        #yield ky, sum(Sm)
        yield ky, Sm
         
            
    def reducer2(self, ky, size):
        #l = list(label)
        #l1=list(size)
        #yield 'average', sum(l)/sum(l1)
        #ul=0
        #ll=0
        #if (ky == 'a'):
            #ul=sum(size)
        #if (ky == 'b'):
            #ll=sum(size)
        #if (ll!=0):
            #yield ul,ul/ll    
        yield 'ky', sum(size)
        #yield 'average', mean(l)
        #yield 'min', min(l)
        #yield 'max', max(l)
    def mapper3(self, k, S):
        yield k,S
    def reducer3(self, ky, Sz):
        S0=list(Sz)
        yield 'WAV',S0[0]/S0[1]        
        
if __name__ == '__main__':
 	MRJWAV.run()       
        

