import xml.etree.ElementTree as et
import pandas
from unidecode import unidecode

stopwords = pandas.read_csv('stopwords.csv')['palavras'].values

csvFile = open("questions.csv", "a")
csvFile.write("id, title\n")

xtree = et.parse("Posts.xml")
xroot = xtree.getroot()

def titleClear(title):
    title = unidecode(title)
    title = title.lower()
    words = title.split(" ")
    for word in words:
        notAlpha = not word.isalpha()
        if (word in stopwords or notAlpha ):
            words.remove(word)
    return " ".join(words)

for node in xroot:
    id = node.attrib.get("Id")
    title = node.attrib.get("Title")
    type = node.attrib.get("PostTypeId")
    if(type == 1):
            print("---------------------------------------------------------")
            print(title)
            title = titleClear(title)
            print(title)
            print("Id: " + id + ", Title: " + title)
            csvFile.write(id +","+title+"\n")
