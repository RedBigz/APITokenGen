import sys, random
tkn=int(sys.argv[1])
done=[]
while True:
    a = random.randrange(65,65+26)
    b = random.randrange(65,65+26)
    c = tkn-(a+b)
    print((chr(a)+chr(b)+chr(c)).replace("\\","\\\\"))
    exit()