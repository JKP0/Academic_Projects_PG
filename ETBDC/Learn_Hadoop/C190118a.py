#from mrjob.step import MRStep
from mrjob.job import MRJob
#from statistics import mean

class MRJLRV(MRJob):

    #def steps(self):
        #return [
            #MRStep(mapper=self.mapper1, #reducer=self.reducer1),
            #MRStep(mapper=self.mapper2, reducer=self.reducer2),
            #MRStep(mapper=self.mapper3, reducer=self.reducer3),
        #]
    def mapper(self, key, line):
        words = line.split(' ')
        for word in words:
            if (word == 'rkmveri'):
                yield (line, ': '+word),1
        if('rkmveri' in words):
            yield 'a', 1
        else:
            yield 'b', 1
                
            
            
    def reducer(self, key, word):
        #f=list(count_one)
        #yield 'a', len(word)*sum(f)
        #yield 'b', sum(f)
        #yield key, word
        k=key
        
        if (k == 'a'):
            w=list(word)
            yield '#of revelant line is : ', sum(w)
        elif (k == 'b'):
            w=list(word)
            yield '#of irrevelant line is : ', sum(w)
        else:
            yield key
        
if __name__ == '__main__':
 	MRJLRV.run()   
