import enum
import os
from pathlib import Path

def add1stline(rf):
    line = 0
    with open(rf, 'r+', encoding="utf8") as f:
        chapname = os.path.basename(rf).split("-")
        fname = chapname[0]
        print(fname)
        context = f.read()
        f.seek(0,0)
        f.write(fname + "\n")
        f.write(context)
        

def main():
    #pathraw = "d:/txt/raw/"
    pathout = "d:/merge/"
    for rf in os.listdir(pathout):
        if rf.endswith(".txt"):
            #print(rf)
            add1stline((os.path.join(pathout,rf)))
            

if __name__ == "__main__":
    main()