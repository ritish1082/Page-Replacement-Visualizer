def optimal(pages,nframes):
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
        elif len(ls) < nframes:
            ls.append(pages[i])
            s=convert(ls)
            s+=" "*(nframes-len(ls))
            s+="m"
            res.append(s)
        else:
            k=predict(ls,pages,nframes,i+1)
            ls[k]=pages[i]
            s=convert(ls)
            s+=" "*(nframes-len(ls))
            s+="m"
            res.append(s)
    return (res,hit)


def predict(ls,pages,nframes,idx):
    farthest=idx
    res=-1
    flag=0
    for i in range(0,nframes):
        for j in range(idx,len(pages)):
            if ls[i]==pages[j]:
                if j > farthest:
                    farthest=j
                    res=i
                    flag=1
                break
        if flag==0:
            return i        
    return res


def convert(ls):
    s=""
    for i in ls:
        s+=str(i)
    return s
