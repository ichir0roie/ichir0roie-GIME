import os
print(os.getcwd())

data_path='Data/youon.html'

with open(data_path,'r',encoding='utf-8')as f:
    text=f.read()
    text=text.replace('\n', '')
    text=text.replace('\t', '')
    text=text.replace('<td class="td_uline">', '\n<td class="td_uline">')
    lines=text.split('\n')

class KeyPair:
    def __init__(self,input_,output):
        self.input=input_
        self.output=output
    def print(self):
        print('{}\t{}'.format(self.input,self.output))
    
key_pair_list=[]

for line in lines:
    if not  'td_uline' in line:continue

    line=line.replace('<td class="td_uline">', '')
    line=line.replace('<br>', '\t')
    line=line.replace('）', '')
    line=line.replace('（', '')
    line=line.replace(' ', '')
    pos=line.find('</td>')
    line=line[:pos]
    output,input_=line.split('\t')
    key_pair_list.append(KeyPair(input_, output))

with open('Maps/getaroShiftEcoBase.tsv','r',encoding='utf-8')as f:
    text=f.read()
    lines=text.split('\n')
    exist_outputs=[]
    for line in lines:
        in_,out_=line.split('\t')
        exist_outputs.append(out_)

key_pair_list.append(KeyPair('uxa','うぁ'))
key_pair_list.append(KeyPair('uxi','うぃ'))
key_pair_list.append(KeyPair('uxu','うぅ'))
key_pair_list.append(KeyPair('uxe','うぇ'))
key_pair_list.append(KeyPair('uxo','うぉ'))

with open('Maps/getaroShiftEcoEasy_OUT.tsv','w',encoding='utf-8')as f:
    for key_pair in key_pair_list:
        if key_pair.output in exist_outputs:
            continue
        new_key='L'+key_pair.input.lower()
        f.write('{}\t{}\n'.format(new_key,key_pair.output))
    
    
    