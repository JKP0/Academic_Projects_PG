#from mrjob.step import MRStep
from mrjob.protocol import JSONProtocol
#from mrjob.protocol import RawValueProtocol
from mrjob.job import MRJob


class MRMRJ(MRJob):
    #OUTPUT_PROTOCOL=RawValueProtocol
    INPUT_PROTOCOL=JSONProtocol
    OUTPUT_PROTOCOL=JSONProtocol
    
    def mapper(self, key, line):
        #words = line.split(',')
        #yield words[0], words[1]
        #yield int(words[0]), words[1]
        yield key, line
        yield int(key), line
            
    #def reducer(self, key, line):
    	  #yield key, line
    		    
    		
            
if __name__ == '__main__':
 	MRMRJ.run()                      

