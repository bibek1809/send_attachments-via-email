import datetime

def log(tag,message):
    datestr = datetime.datetime.now().strftime("[%H:%M:%S]")
    logstr = f"{datestr}= [{tag}] = [{message}]"
    print(logstr)

FILE_PATH = "./out.csv"

    
