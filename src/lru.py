def lru(pages,nframes):
    res=[]
    hit=0
    ls=[]
    for i in range(0,len(pages)):
        s=""
        if pages[i] in ls:
            hit+=1
            s=convert(ls)
            s+=" "*(nframes-len(ls))
            s+="h"
            res.append(s)
        elif  len(ls) < nframes:
            ls.append(pages[i])
            s=convert(ls)
            s+=" "*(nframes-len(ls))
            s+="m"
            res.append(s)
        else:
            k=least(ls,pages,nframes,i-1)
            ls[k]=pages[i]
            s=convert(ls)
            s+=" "*(nframes-len(ls))
            s+="m"
            res.append(s)
    return (res,hit)

def least(ls,pages,nframes,idx):
    recent=idx
    res=-1
    for i in range(0,nframes):
        for j in range(idx,-1,-1):
            if ls[i]==pages[j]:
                if j < recent:
                    recent=j
                    res=i
                break
    return res

def convert(ls):
    s=""
    for i in ls:
        s+=str(i)
    return s