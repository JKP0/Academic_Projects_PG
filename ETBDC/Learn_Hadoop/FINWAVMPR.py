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
        freq=list(count_one)
        yield 'a', len(word)*sum(freq)
        yield 'b', sum(freq)
        
    def mapper2(self, ky, Sm):
        yield ky, Sm

    def reducer2(self, ky, size):
        yield 'ky', sum(size)

    def mapper3(self, k, S):
        yield k,S
        
    def reducer3(self, ky, Sz):
        S0=list(Sz)
        yield 'Weighted Average for length of words in file is : ',S0[0]/S0[1]

if __name__ == '__main__':
 	MRJWAV.run()   
