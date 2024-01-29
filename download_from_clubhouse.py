import urllib.request
import re, os, sys
from pydub import AudioSegment

regix = "(output\d*)"

with open("./input", "r") as f:
    length = len(f.readlines())
    preogress_width = 30
    progress = ["["]+["." for i in range(preogress_width)]+["]"]

    f.seek(0)
    divder =  length // preogress_width

    for passed, chunck in enumerate(f.readlines()):
        if (chunck.startswith("http")):
            filename = (re.search(regix, chunck).group());
            urllib.request.urlretrieve(chunck, "."+filename+".ts")
            progress[passed // divder] = "#"

            print("".join(progress))
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
