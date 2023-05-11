import sys
import time
for i in range(10):

    sys.stdout.write("\r{}".format(i))
    sys.stdout.flush()
    time.sleep(0.1)
    
print()