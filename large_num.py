# import array
# a = array.array('I', xrange(10**8))
# import random
# random.shuffle(a)





a = [1]*10000000
output = ' '.join(str(i) for i in a)

text_file = open("Output.txt", "w")
text_file.write(output)
text_file.close()