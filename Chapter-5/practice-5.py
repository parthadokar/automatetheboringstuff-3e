#spam = 5
#assert spam >= 10

#eggs = 'hello'
#bacon = 'hello'
#assert eggs.lower() != bacon.lower()

#assert False

import logging 
logging.basicConfig(level=logging.DEBUG)
logging.debug("This debug message will appear")

logging.basicConfig(filename='programlog.txt',level=logging.DEBUG)

#DEBUG, INFO, WARN (Warning), ERROR, and FATAL (or CRITICAL)

logging.disable(logging.CRITICAL)

# logging makes it easy to debug and also removes the need to add unnecssary prints to check for status.


