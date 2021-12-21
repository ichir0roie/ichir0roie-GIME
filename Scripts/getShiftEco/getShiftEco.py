

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
baseBoard = [
    [],
    [],
    []
]
boardNums = {
    "base": baseBoard,
    "s": [],
    "d": [],
    "k": [],
    "l": []
}

# keyboardPriority
with open(dataPath+"keyboardPriority.txt",mode="r",encoding="utf-8")as f:
    text=f.read()
    lines=text.split("\n")
keyboardPriority=[]

import string

for row in lines[3:]:
    items=row.split("\t")
    newItems=[]
    text=""
    for item in items:
        if item in ["s","d","k","l"]:
            newItems.append(item)
        elif item in string.ascii_lowercase:
            newItems.append(None)
        else:
            newItems.append(int(item))
    keyboardPriority.append(newItems)

print(keyboardPriority)

# for row in keyboardPriority:
#     text=""
#     for item in row:
#         text+=str(item)+","
#     print(text)

