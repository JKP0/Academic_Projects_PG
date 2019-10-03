from mrjob.step import MRStep
from mrjob.job import MRJob

class MRJLRCH(MRJob):
    def steps(self):
            return [
                MRStep(mapper=self.mapper1, reducer=self.reducer1),
                MRStep(mapper=self.mapper2),# reducer=self.reducer2),
                #MRStep(mapper=self.mapper3, reducer=self.reducer3),
            ]
    def mapper1(self, key, line):
        words = line.split(' ')
        for word in words:
            yield word, 1

    def reducer1(self, word, cnt):
        yield word, sum(cnt)

    def mapper2(self, word, sm):
        s=sm
        wd=word
        cha= list(wd)
        lc=0
        for c in cha:
            if (c == 'a' or c == 'e'):
                lc +=1
        yield  lc, (wd,s)

    def reducer2(self, lc, val):
        yield lc, val


    
if __name__ == '__main__':
 	MRJLRCH.run()   
