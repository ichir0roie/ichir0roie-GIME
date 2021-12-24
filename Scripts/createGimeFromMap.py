




class createGimeFormMap:
    def __init__(self):
        self.gimes=[]
        self.gimeCombined=[]
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
        self.gimeCombined=[]

        for gime in self.gimes:
            for key in gime.keys():
                self.gimeCombined.append([key,gime[key]])
            self.gimeCombined.append(None)

    def print(self):
        for item in self.gimeCombined:
            if item is None:
                print("\n")
                continue
            key=item[0]
            value=item[1]
            print("{}\t:\t{}".format(key,value))
    
    def save(self,mapName:str):
        with open("Output/{}.tsv".format(mapName),mode="w",encoding="utf-8")as f:
            for item in self.gimeCombined:
                if item is None:
                    f.write("\n")
                    continue
                f.write("{}\t{}".format(item[0],item[1])+"\n")

    
if __name__=="__main__":
    cgf=createGimeFormMap()
    gimeList=[
        "getaroBase",
        # "getaroShift",
        "getaroShiftEco",
        "getaroSpecial",
    ]
    cgf.loadGimes(gimeList)
    cgf.combineGimes()
    cgf.print()
    cgf.save("gimeGetaroEco")
