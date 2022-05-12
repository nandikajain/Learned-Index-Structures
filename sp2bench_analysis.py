import rdflib
import time

iter_ = ["1", "2", "3a", "3b", "3c", "4", "5a","5b", "6","7", "8", "9", "10", "11", "12a", "12b", "12c"]
def calculate_time(fileName):
      g = rdflib.Graph()
      g.parse(fileName)
      print(fileName, len(g))
      
      before_time = time.time()
      for i in iter_:
            f = open("./sp2b/queries/q"+i+".sparql")   
            query= f.read()
            qres = g.query(query)

      clock_diff = time.time()-before_time
      clock_diff /= len(iter_)
      string_to_write = "Average time taken is (in seconds) for "+fileName+" :"+ str(clock_diff)+"\n"
      print(string_to_write)
      return string_to_write
            
string_to_write = ""
file_names = ["sp2b_50k.n3", "sp2b_100k.n3"]
for i in file_names:
      string_to_write += calculate_time(i)
with open("sp2bench_result.txt",'w',encoding = 'utf-8') as f:
  f.write(string_to_write)
