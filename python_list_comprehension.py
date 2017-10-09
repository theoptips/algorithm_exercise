# python list comprehension
# times table example
times_table = [i*j for i in range(1,10) for j in range(1,10)]
print (times_table)

# coursera exercise list of all possible ids letterletterdigitsdigits e.g. xy04
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [str(i)+str(j)+str(k)+str(m) for i in lowercase for j in lowercase for k in digits for m in digits]
#correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]
print(answer)