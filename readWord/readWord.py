import docx

def readFile(fileName):
    file = docx.Document(fileName)
    return file



