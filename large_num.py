import array
a = array.array('I', xrange(10**8))
import random
random.shuffle(a)
text_file = open("Output.txt", "w")
text_file.write(a)
text_file.close()
