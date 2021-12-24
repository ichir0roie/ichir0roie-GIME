

import os
dataPath = "Data/"
outPath = "OutPut/"
if not os.path.exists(outPath):
    os.mkdir(outPath)


'''文字マップの作成'''

with open(dataPath+"mainTwoChars", mode="r", encoding="utf-8")as f:
    text = f.read()

# 配列のNoが優先度に対応
listChar = text.split("\n")
print(listChar)

'''キーボード優先度マップの作成'''

# keyboardPriority
with open(dataPath+"keyboardPriority.txt",mode="r",encoding="utf-8")as f:
    text=f.read()
    lines=text.split("\n")
keyboardPriority=[]
keyboardPriorityForRightShift=[]
keyboardPriorityForLeftShift=[]
keyboardAlpha=[]

import string

shiftKeys=["S","L"]

for row in lines[0:3]:
    keyboardAlpha.extend(row.split("\t"))
for row in lines[3:6]:
    keyboardPriority.extend(row.split("\t"))
for row in lines[6:9]:
    keyboardPriorityForRightShift.extend(row.split("\t"))
for row in lines[9:12]:
    keyboardPriorityForLeftShift.extend(row.split("\t"))

print(keyboardPriority)


def getThreeKey(key:str):
    key = key.upper()
    if key ==",":
        key="<"
    elif key ==".":
        key=">"
    return key

maxPriority=len(listChar)
typeListPriority=[None for i in range(maxPriority+1)]

for i in range(len(keyboardPriority)):
    if int(keyboardPriority[i])<0 :
        continue
    item=getThreeKey(keyboardAlpha[i])
    typeListPriority[int(keyboardPriority[i])]=item


baseMax=max([int(x) for x in keyboardPriority if int(x)>=0])+1
rightShiftKey="L"
for i,number in enumerate(keyboardPriorityForRightShift):
    if number =="":
        continue
    setPlace=baseMax+int(number)*2
    if setPlace>=maxPriority:
        continue
    typeListPriority[setPlace]=rightShiftKey+getThreeKey(keyboardAlpha[i])

leftShiftKey="S"
for i,number in enumerate(keyboardPriorityForLeftShift):
    if number =="":
        continue
    setPlace=baseMax+int(number)*2+1
    if setPlace>=maxPriority:
        continue
    typeListPriority[setPlace]=leftShiftKey+getThreeKey(keyboardAlpha[i])


# add shift shift

typeListPriority=[x for x in typeListPriority if x is not None]



# create gime

gimeList={}

for c,keyChar in enumerate(listChar):
    gimeList[typeListPriority[c]]=keyChar

for key in gimeList.keys():
    value=gimeList[key]
    print("{}\t{}".format(key,value))


def saveShiftEco():
    with open("Maps/getaroShiftEco.tsv",mode="w",encoding="utf-8")as f:
        for key in gimeList.keys():
            f.write("{}\t{}\n".format(key,gimeList[key]))
saveShiftEco()

saveText=""
def setText(text:str):
    global saveText
    saveText+=text+"\n"
    print(text)

setText("----------------------------------------------------------------------------------")
for row in lines[0:3]:
    text=""
    for item in row.split("\t"):
        item = getThreeKey(item)
        if item in shiftKeys:
            text+=item.upper()+"\t"
            continue
        text+=gimeList[item]+"\t"
    setText(text)
setText("----------------------------------------------------------------------------------")
for row in lines[0:3]:
    text=""
    for item in row.split("\t"):
        key="S"+getThreeKey(item)
        if item=="s":
            text+="S"+"\t"
            continue
        elif not key in gimeList.keys():
            text+="  "+"\t"
            continue
        text+=gimeList[key]+"\t"
    setText(text)
setText("----------------------------------------------------------------------------------")
for row in lines[0:3]:
    text=""
    for item in row.split("\t"):
        key="L"+getThreeKey(item)
        if item=="l":
            text+="L"+"\t"
            continue
        elif not key in gimeList.keys():
            text+="  "+"\t"
            continue
        text+=gimeList[key]+"\t"
    setText(text)
setText("----------------------------------------------------------------------------------") 

with open("OutPut/ShiftEcoView.tsv",mode="w",encoding="utf-8")as f:
    f.write(saveText)


