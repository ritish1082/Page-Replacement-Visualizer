from collections import deque

def fifo(pages,nframes):
    res=[]
    hit=0
    ls=deque()
    for page in pages:
        s=""
        if len(ls) < nframes:
            if page not in ls:
                ls.appendleft(page)
                s,c=convert(ls,nframes)
                s+="m"
                res.append(s)
            else:
                s,c=convert(ls,nframes)  
                s+="h"
                res.append(s)
                hit+=1
        else:
            if page in ls:
                s,c=convert(ls,nframes)
                s+="h"
                res.append(s)
                hit+=1
            else:
                ls.pop()
                ls.appendleft(page)
                s,c=convert(ls,nframes)
                s+="m"
                res.append(s)
    return (res,hit)

def convert(ls,nframes):
    s=""
    c=0
    for i in ls:
        c+=1
        s+=str(i)
    s+=" "*(nframes-c)
    return (s,c)