import random
import time
import graphing_methods

graphing_methods.init_data(100)

for i in range(100):
    graphing_methods.update_graph(random.randrange(0, 20))
    time.sleep(0.1)
    
