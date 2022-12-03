def txt2string(file:str) -> str:
    with open(file, "r") as f:
        return f.read()
    
def txt2list(file:str) -> list[str]:
    textstring = txt2string(file)
    return textstring.split("\n")

def txt2listoftuples(file:str, delimiter=" ") -> list[tuple]:
    textlist = txt2list(file)
    return [tuple(x.split(delimiter)) for x in textlist]

  