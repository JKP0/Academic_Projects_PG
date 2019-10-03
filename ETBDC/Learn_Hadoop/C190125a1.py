from mrjob.step import MRStep
from mrjob.job import MRJob

class MRMRBSK(MRJob):
    def steps(self):
            return [
                MRStep(mapper=self.mapper1, reducer=self.reducer1),
                MRStep(mapper=self.mapper2, reducer=self.reducer2),
            ]

    def mapper1(self, key, line):
        words = line.split(',')
        yield words[0], words[1]
            
    def reducer1(self, key, line):
    	yield 1, (key, len(list(line)))
    	  
    def mapper2(self, key, line):
    	yield key, line   
    		    
    def reducer2(self, key, line):
        ls=list(line)
        #ma=max([y for x, y in ls])
        yield next((x,y) for x, y in ls if(y==max([y for x, y in ls])))
        #yield next((x,y) for x, y in ls if(y==ma))
        #yield ((x, y) for x, y in ls if(y==ma))
        #for x, y in ls:
            #if(y==ma):
                #yield x, y
        
            
if __name__ == '__main__':
 	MRMRBSK.run()                      
