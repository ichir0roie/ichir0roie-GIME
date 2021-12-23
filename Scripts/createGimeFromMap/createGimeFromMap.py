




class createGimeFormMap:
    def __init__(self):
        self.gimes=[]
        self.gimeCombined={}
        return
    
    def loadGime(self,fileName:str):
        path="Maps/"+fileName+".tsv"
        with open(path,mode="r",encoding="utf-8")as f:
            data=f.read()
            pairs=data.split("\n")
        gime={}
        for pair in pairs:
            if not "\t" in pair:
                continue
            key,value=pair.split("\t")
            gime[key]=value
        
        return gime
    

    def loadGimes(self,fileNames:list):
        self.gimes=[]
        for fileName in fileNames:
            gime=self.loadGime(fileName)
            self.gimes.append(gime)

    
    def combineGimes(self):
        self.gimeCombined={}

        for gime in self.gimes:
            self.gimeCombined.update(gime)

    def print(self):
        for key in self.gimeCombined:
            print("{}\t:\t{}".format(key,self.gimeCombined[key]))
    
    def save(self):
        with open("Output/gime.tsv",mode="w",encoding="utf-8")as f:
            for key in self.gimeCombined:
                f.write("{}\t{}".format(key,self.gimeCombined[key])+"\n")

    
if __name__=="__main__":
    cgf=createGimeFormMap()
    gimeList=[
        "getaroBase",
        "getaroSpecial",
        "getaroShift"
    ]
    cgf.loadGimes(gimeList)
    cgf.combineGimes()
    cgf.print()
    cgf.save()
