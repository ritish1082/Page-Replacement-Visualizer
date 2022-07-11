from collections import deque
from queue import Queue
from flask import Flask, render_template,request
from src import fifo,lru,optimal

# flask app
app = Flask(__name__)

@app.route('/')
def default():
    return render_template('home.html')

@app.route('/visualize', methods=['GET','POST'])
def visulaize():
    title=""
    algo=request.form["algo"]
    pages = request.form["pages"]
    nframes = int(request.form["frames"])
    pages=list(map(str,pages.split()))
    n=len(pages)
    res=[]
    if algo =="1":
        res,hit=fifo.fifo(pages,nframes)
        title="First In First Out (FIFO)"
    elif algo=="2":
        res,hit=optimal.optimal(pages,nframes)
        title="Optimal (LFU)"
    elif algo=="3":
        res,hit=lru.lru(pages,nframes)
        title="Least Recently Used (LRU)"
    return render_template('visualize.html',res=res,algo=title,page_sequence=pages,no_pages=len(pages),frame_size=nframes,hit=hit,miss=n-hit,hit_rate=round((hit/n)*100,2),fault_rate=round(((n-hit)/n)*100,2))

if __name__ == '__main__':
    app.run(debug=True)