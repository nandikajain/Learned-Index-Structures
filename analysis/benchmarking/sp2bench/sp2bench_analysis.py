import rdflib
import time

g = rdflib.Graph()
g.parse("sp2b.n3")
print(len(g))

# before_time = time.time()
# iter_ = ["1", "2", "3a", "3b", "3c", "4", "5a","5b", "6","7", "8", "9", "10", "11", "12a", "12b", "12c"]

# for i in range(0, 10):
#   for i in iter_:
#     f = open("./sp2b/queries/q"+i+".sparql")   
#     query= f.read()
#     qres = g.query(query)

# clock_diff = time.time()-before_time
# clock_diff /= 10
# clock_diff /= len(iter_)
# string_to_write = "Average time taken is (in seconds):"+ str(clock_diff)

# with open("sp2bench_result.txt",'w',encoding = 'utf-8') as f:
#   f.write(string_to_write)
# print(string_to_write)
