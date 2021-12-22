

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
keyboardAlphaLower=[]
keyboardAlphaUpper=[]

import string

shiftKeys=["S","L"]

for row in lines[0:3]:
    keyboardAlphaLower.extend(row.split("\t"))
for row in lines[3:6]:
    keyboardAlphaUpper.extend(row.split("\t"))
for row in lines[6:9]:
    keyboardPriority.extend(row.split("\t"))

print(keyboardPriority)

maxPriority=len(keyboardPriority)-3

typeListPriority=[None for i in range(maxPriority+1)]
for i in range(len(keyboardPriority)):
    if int(keyboardPriority[i])<0 :
        continue
    typeListPriority[int(keyboardPriority[i])]=keyboardAlphaUpper[i]


# add shift shift

extendTypeList=[]
for threeKey in typeListPriority:
    threeKey=threeKey.lower()
    keyS="S"+threeKey
    keyL="L"+threeKey
    extendTypeList.append(keyS)
    extendTypeList.append(keyL)
typeListPriority.extend(extendTypeList)
print(typeListPriority)

# create gime

gimeList={}

for c,keyChar in enumerate(listChar):
    gimeList[typeListPriority[c]]=keyChar

for key in gimeList.keys():
    value=gimeList[key]
    print("{}\t{}".format(key,value))

print("----------------------------------------------------------------------------------")
for row in lines[3:6]:
    text=""
    for item in row.split("\t"):
        if item in shiftKeys:
            text+="  "+"\t"
            continue
        text+=gimeList[item]+"\t"
    print(text)
print("----------------------------------------------------------------------------------")
for row in lines[3:6]:
    text=""
    for item in row.split("\t"):
        key="S"+item.lower()
        if item in shiftKeys or not key in gimeList.keys():
            text+="  "+"\t"
            continue
        text+=gimeList[key]+"\t"
    print(text)
print("----------------------------------------------------------------------------------")
for row in lines[3:6]:
    text=""
    for item in row.split("\t"):
        key="L"+item.lower()
        if item in shiftKeys or not key in gimeList.keys():
            text+="  "+"\t"
            continue
        text+=gimeList[key]+"\t"
    print(text)
print("----------------------------------------------------------------------------------") 




