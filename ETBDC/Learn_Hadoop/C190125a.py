from mrjob.job import MRJob

class MRMRBSK(MRJob):
    def mapper(self, key, line):
        words = line.split(',')
        yield words[0], words[1]
            
    def reducer(self, key, line):
        ls=list(line)
        #yield key, (ls, len(ls))
        yield key, (ls, '#'+str(len(ls)))
            
if __name__ == '__main__':
 	MRMRBSK.run()                      
