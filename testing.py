from json import dumps


class XMLVisitor():
    def __init__(self):
        self.data={"industrial":[],
                   "residential":[]}

    def industrial(self,building:Industrial):
        self.data["industrial"].append({"CO2":building.CO2})

    def residential(self,building:Residential):
        self.data["residential"].append({"slaapkamers":building.slaapKamers,"oppervlakte":building.oppervlakte})

    def export(self):
        res=""
        ind=""

        for r in self.data["residential"]:
            res+=("  <residential>\n"
                  f"    <slaapkamers>{r['slaapkamers']}</slaapkamers>\n"
                  f"    <oppervlakte>{r['oppervlakte']}</oppervlakte>\n"
                  "  </residential>\n")
        for b in self.data["industrial"]:
            ind+=("  <industrial>\n"
                  f"    <CO2>{b['CO2']}</CO2>\n"
                  "  </industrial>\n")

        return f"<data>\n{res}{ind}</data>"


class JSONVisitor():
    def __init__(self):
        self.data={"industrial":[],
                   "residential":[]}
        self.rcount=0

    def industrial(self,building:Industrial):
        self.data["industrial"].append({"CO2":building.CO2})
        self.rcount+=1

    def residential(self,building:Residential):
        self.data["residential"].append({"slaapkamers":building.slaapKamers,"oppervlakte":building.oppervlakte})
        self.rcount+=1

    def export(self):
        return dumps(self.data,indent=3)


    



class Industrial():
    def __init__(self,CO2):
        self.CO2=CO2


    def accept(self,visitor):
        visitor.industrial(self)


class Residential():
    def __init__(self,slaapKamers,oppervlakte):
        self.slaapKamers=slaapKamers
        self.oppervlakte=oppervlakte


    def accept(self,visitor):
        visitor.residential(self)



r1=Residential(2,120)
r2=Residential(3,20)
r3=Residential(1,10)
i1=Industrial(30)
i2=Industrial(120)
i3=Industrial(999)
buildings=[r1,r2,r3,i1,i2,i3]
Jvisitor=JSONVisitor()
XVisitor=XMLVisitor()
for building in buildings:
    building.accept(Jvisitor)
    building.accept(XVisitor)
    

print(Jvisitor.rcount)
print(XVisitor.export())



    


    

