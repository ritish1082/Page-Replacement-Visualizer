def size(ls,nf):
    for i in range(nf):
        if ls[i]==-1: return i 
    return nf

def find(ls,x,nframes):
    for i in range(nframes):
        if(x==ls[i]):   return 1
    return 0

def convert(ls,nframes):
    s=""
    for i in ls:
        if i==-1:
            s+=str(" ")
        else:
            s+=str(i)
    s+=" "*(nframes-len(ls))
    return s

def Last(ls, pages, l, count,nf):
    n=len(pages)
    c = [999]*n
    for i in range(n-1,l, -1):
        c[int(pages[i])] = i 
    mx = c[int(ls[0])]; p=0 
    for i in range(1, nf):
        if(c[int(ls[i])] > mx):
            mx = c[int(ls[i])]
            p =i 
        elif(c[int(ls[i])]==mx): 
            if count[p] > count[i]: 
                p = i
                mx = c[int(ls[i])]
    return p



def optimal(pages,nframes):
    p=-1
    res=[]
    ls=[-1]*nframes
    count=[0]*nframes
    hit=0
    for i in range(0,len(pages)):
        if find(ls,pages[i],nframes):
            hit+=1
            s=convert(ls,nframes)
            s+="h"
            res.append(s)
        else:
            if(size(ls,nframes) < nframes):
                p+=1
                ls[p]=pages[i]
                s=convert(ls,nframes)
                s+="m"
                res.append(s)
            else:
                p=Last(ls,pages,i,count,nframes)
                ls[p]=pages[i]
                s=convert(ls,nframes)
                s+="m"
                res.append(s)
            count[p]=i
    return (res,hit)
