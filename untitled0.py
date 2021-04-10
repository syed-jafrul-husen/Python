#import time
from collections import defaultdict 
import tkinter
from tkinter import *
window = tkinter.Tk()
import time

window.title("         ************************-------------------------              Navigating Between Points!!            --------------------------*************************!!")
window.geometry("1100x680")


def disLevel():
    L1 = Label(c, text='3200m', fg='white', bg='grey')
    c.create_window(149, 22, window=L1)
    L2 = Label(c, text='750m', fg='white', bg='grey')
    c.create_window(351, 22, window=L2)
    L3 = Label(c, text='400m', fg='white', bg='grey')
    c.create_window(555, 22, window=L3)
    L4 = Label(c, text='2300m', fg='white', bg='grey')
    c.create_window(55, 117, window=L4)
    L5 = Label(c, text='778m', fg='white', bg='grey')
    c.create_window(150, 177, window=L5)
    L6 = Label(c, text='620m', fg='white', bg='grey')
    c.create_window(350, 177, window=L6)
    L7 = Label(c, text='320m', fg='white', bg='grey')
    c.create_window(248,110, window=L7)
    L8 = Label(c, text='230m', fg='white', bg='grey')
    c.create_window(452, 110, window=L8)
    L9 = Label(c, text='643m', fg='white', bg='grey')
    c.create_window(650, 110, window=L9)
    L10 = Label(c, text='283m', fg='white', bg='grey')
    c.create_window(55, 265, window=L10)
    L11 = Label(c, text='940m', fg='white', bg='grey')
    c.create_window(150, 325, window=L11)
    L12 = Label(c, text='1220m', fg='white', bg='grey')
    c.create_window(255, 265, window=L12)
    L13 = Label(c, text='705m', fg='white', bg='grey')
    c.create_window(352, 327, window=L13)
    L14 = Label(c, text='523m', fg='white', bg='grey')
    c.create_window(650, 265, window=L14)
    L15 = Label(c, text='1180m', fg='white', bg='grey')
    c.create_window(155, 487, window=L15)
    L16 = Label(c, text='1470m', fg='white', bg='grey')
    c.create_window(370, 487, window=L16)
    L17 = Label(c, text='423m', fg='white', bg='grey')
    c.create_window(118, 420, window=L17)
    L18 = Label(c, text='2600m', fg='white', bg='grey')
    c.create_window(535, 410, window=L18)
    L19 = Label(c, text='325m', fg='white', bg='grey')
    c.create_window(517, 260, window=L19)


def IDSinput():
    g.addEdge('Mojumdar','Amborkhana') 
    g.addEdge('Mojumdar', 'Pirmoholla') 
    g.addEdge('Amborkhana', 'Dorgah Gate') 
    g.addEdge('Amborkhana', 'Housing State') 
    g.addEdge('Dorgah Gate', 'Chuhatta') 
    g.addEdge('Dorgah Gate', 'Rajar Goli') 
    g.addEdge('Chuhatta','Rikabi Bazar' ) 
    g.addEdge('Pirmoholla','Housing State') 
    g.addEdge('Pirmoholla','Kolapara' ) 
    g.addEdge('Housing State','Rajar Goli') 
    g.addEdge('Housing State','Subid Bazar' ) 
    g.addEdge('Rikabi Bazar','Kajal Shah' ) 
    g.addEdge('Rikabi Bazar', 'Mirer Moydan') 
    g.addEdge('Kolapara','Subuid Bazar' ) 
    g.addEdge('Subid Bazar','Mirer Moydan' ) 
    g.addEdge('Subid Bazar','Pathan Tula' ) 
    g.addEdge('Kajal Shah','Bagh Bari')
    g.addEdge('Pathan Tula','Modina Market')
    g.addEdge('Modina Market','Bagh Bari')
    
    g.addEdge('Amborkhana','Mojumdar') 
    g.addEdge('Pirmoholla','Mojumdar') 
    g.addEdge('Amborkhana', 'Amborkhana') 
    g.addEdge( 'Housing State','Amborkhana') 
    g.addEdge( 'Chuhatta','Dorgah Gate') 
    g.addEdge( 'Rajar Goli','Dorgah Gate') 
    g.addEdge('Rikabi Bazar' ,'Chuhatta') 
    g.addEdge('Housing State','Pirmoholla') 
    g.addEdge('Kolapara','Pirmoholla') 
    g.addEdge('Rajar Goli','Housing State') 
    g.addEdge('Subid Bazar' ,'Housing State') 
    g.addEdge('Kajal Shah', 'Rikabi Bazar') 
    g.addEdge( 'Mirer Moydan','Rikabi Bazar') 
    g.addEdge('Subuid Bazar' ,'Kolapara') 
    g.addEdge('Mirer Moydan','Subid Bazar' ) 
    g.addEdge('Pathan Tula','Subid Bazar' ) 
    g.addEdge('Bagh Bari','Kajal Shah')
    g.addEdge('Modina Market','Pathan Tula')
    g.addEdge('Bagh Bari','Modina Market')



def resetLine(src,i):
    #time.sleep(2)
    if(src=='Mojumdar' and i=='Amborkhana'):
        moAm = c.create_line(100,35,198,35,width=5,fill='red')
    elif(i=='Mojumdar' and src=='Amborkhana'):
        moAm= c.create_line(100,35,198,35,width=5,fill='red')
    elif(src=='Amborkhana' and i=='Dorgah Gate'):
        amDo = c.create_line(302,35,400,35,width=5,fill='red')
    elif(i=='Amborkhana' and src=='Dorgah Gate'):
        amDo = c.create_line(302,35,400,35,width=5,fill='red')
    elif(src=='Dorgah Gate' and i=='Chuhatta'):
        doCh = c.create_line(510,35,600,35,width=5,fill='red')
    elif(i=='Dorgah Gate' and src=='Chuhatta'):
        doCh = c.create_line(510,35,600,35,width=5,fill='red')
    elif(src=='Mojumdar' and i=='Pirmoholla'):
        mopi = c.create_line(55,70,55,160,width=5,fill='red')
    elif(i=='Mojumdar' and src=='Pirmoholla'):
        mopi = c.create_line(55,70,55,160,width=5,fill='red')
    elif(src=='Pirmoholla' and i=='Housing State'):
        piHs = c.create_line(100,190,193,190,width=5,fill='red')
    elif(i=='Pirmoholla' and src=='Housing State'):
        piHs = c.create_line(100,190,193,190,width=5,fill='red')
    elif(src=='Housing State' and i=='Rajar Goli'):
        hsRg = c.create_line(307,190,400,190,width=5,fill='red')
    elif(i=='Housing State' and src=='Rajar Goli'):
        hsRg = c.create_line(307,190,400,190,width=5,fill='red')
    elif(src=='Housing State' and i=='Amborkhana'):
        hsAm = c.create_line(248,70,248,160,width=5,fill='red')
    elif(i=='Housing State' and src=='Amborkhana'):
        hsAm = c.create_line(248,70,248,160,width=5,fill='red')
    elif(src=='Dorgah Gate' and i=='Rajar Goli'):
        doRg = c.create_line(455,70,455,160,width=5,fill='red')
    elif(i=='Dorgah Gate' and src=='Rajar Goli'):
        doRg = c.create_line(455,70,455,160,width=5,fill='red')
    elif(src=='Chuhatta' and i=='Rikabi Bazar'):
        cuRk = c.create_line(650,70,650,160,width=5,fill='red')
    elif(i=='Chuhatta' and src=='Rikabi Bazar'):
        cuRk = c.create_line(650,70,650,160,width=5,fill='red')
    elif(src=='Pirmoholla' and i=='Kolapara'):
        piKo = c.create_line(55,220,55,310,width=5,fill='red')
    elif(i=='Pirmoholla' and src=='Kolapara'):
        piKo = c.create_line(55,220,55,310,width=5,fill='red')
    elif(src=='Kolapara' and i=='Subid Bazar'):
        koSU = c.create_line(100,340,198,340,width=5,fill='red')
    elif(i=='Kolapara' and src=='Subid Bazar'):
        koSU = c.create_line(100,340,198,340,width=5,fill='red')
    elif(src=='Housing State' and i=='Subid Bazar'):
        hsSu = c.create_line(255,220,255,310,width=5,fill='red')
    elif(i=='Housing State' and src=='Subid Bazar'):
        hsSu = c.create_line(255,220,255,310,width=5,fill='red')
    elif(src=='Subid Bazar' and i=='Mirer Moydan'):
        suMi = c.create_line(302,340,395,340,width=5,fill='red')
    elif(i=='Subid Bazar' and src=='Mirer Moydan'):
        suMi = c.create_line(302,340,395,340,width=5,fill='red')
    elif(src=='Kajal Shah' and i=='Rikabi Bazar'):
        kaRk = c.create_line(650,220,650,310,width=5,fill='red')
    elif(i=='Kajal Shah' and src=='Rikabi Bazar'):
        kaRk = c.create_line(650,220,650,310,width=5,fill='red')
    elif(src=='Modina Market' and i=='Pathan Tula'):
        moPa = c.create_line(103,500,200,500,width=5,fill='red')
    elif(i=='Modina Market' and src=='Pathan Tula'):
        moPa = c.create_line(103,500,200,500,width=5,fill='red')
    elif(src=='Modina Market' and i=='Bagh Bari'):
        moBa = c.create_line(322,500,420,500,width=5,fill='red')
    elif(i=='Modina Market' and src=='Bagh Bari'):
        moBa = c.create_line(322,500,420,500,width=5,fill='red')
    elif(src=='Pathan Tula' and i=='Subid Bazar'):
        paSu = c.create_line(55,475,258,368,width=5,fill='red')
    elif(i=='Pathan Tula' and src=='Subid Bazar'):
        paSu = c.create_line(55,475,258,368,width=5,fill='red')
    elif(src=='Bagh Bari' and i=='Kajal Shah'):
        baKj = c.create_line(470,472,650,368,width=5,fill='red')
    elif(i=='Bagh Bari' and src=='Kajal Shah'):
        baKj = c.create_line(470,472,650,368,width=5,fill='red')
    elif(src=='Mirer Moydan' and i=='Rikabi Bazar'):
        miRi = c.create_line(450,313,652,218,width=5,fill='red')
    elif(i=='Mirer Moydan' and src=='Rikabi Bazar'):
        miRi = c.create_line(450,313,652,218,width=5,fill='red')


def resetOval(src,tar):
    if(src=="Mojumdar" or tar=="Mojumdar"):
        mojumdar = c.create_oval(10, 10, 100, 70, width=2, fill='red')
        mojumdarL = Label(c, text='Mojumdar',fg='black', bg='snow3',font='bold')
        c.create_window(55, 40, window=mojumdarL)
    if(src=="Amborkhana" or tar=="Amborkhana"):
        amborkhana = c.create_oval(198, 10, 302, 70, width=2, fill='red')
        amborkhanaL = Label(c, text='Amborkhana',fg='black', bg='snow3',font='bold')
        c.create_window(250, 40, window=amborkhanaL)
    if(src=="Dorgah Gate" or tar=="Dorgah Gate"):
        dorgahGate = c.create_oval(400, 10, 510, 70, width=2, fill='red')
        dorgahGateL = Label(c, text='Dorgah Gate',fg='black', bg='snow3',font='bold')
        c.create_window(455, 40, window=dorgahGateL)
    if(src=="Chuhatta" or tar=="Chuhatta"):
        chuhatta = c.create_oval(600, 10, 700, 70, width=2, fill='red')
        chuhattaL = Label(c, text='Chuhatta',fg='black', bg='snow3',font='bold')
        c.create_window(650, 40, window=chuhattaL)
    if(src=="Pirmoholla" or tar=="Pirmoholla"):
        Pirmoholla = c.create_oval(10, 160, 100, 220, width=2, fill='red')
        PirmohollaL = Label(c, text='Pirmoholla',fg='black', bg='snow3',font='bold')
        c.create_window(53, 190, window=PirmohollaL)
    if(src=="Housing State" or tar=="Housing State"):
        housingState = c.create_oval(193, 160, 307, 220, width=2, fill='red')
        housingStateL = Label(c, text='Housing State',fg='black', bg='snow3',font='bold')
        c.create_window(250, 190, window=housingStateL)
    if(src=="Rajar Goli" or tar=="Rajar Goli"):
        rajarGoli = c.create_oval(400, 160, 500, 220, width=2, fill='red')
        rajarGoliL = Label(c, text='Rajar Goli', fg='black', bg='snow3',font='bold')
        c.create_window(450, 190, window=rajarGoliL)
    if(src=="Rikabi Bazar" or tar=="Rikabi Bazar"):
        rikabiBazar = c.create_oval(595, 160, 705, 220, width=2, fill='red')
        rikabiBazarL = Label(c, text='Rikabi Bazar', fg='black', bg='snow3',font='bold')
        c.create_window(650, 190, window=rikabiBazarL)
    if(src=="Kolapara" or tar=="Kolapara"):
        kolapara = c.create_oval(10, 310, 100, 370, width=2, fill='red')
        kolaparaL = Label(c, text='Kolapara', fg='black', bg='snow3',font='bold')
        c.create_window(55, 340, window=kolaparaL)
    if(src=="Subid Bazar" or tar=="Subid Bazar"):
        subidBazar = c.create_oval(198, 310, 302, 370, width=2, fill='red')
        subidBazarL = Label(c, text='Subid Bazar',fg='black', bg='snow3',font='bold')
        c.create_window(250, 340, window=subidBazarL)
    if(src=="Mirer Moydan" or tar=="Mirer Moydan"):
        mirerMoydan = c.create_oval(395, 310, 505, 370, width=2, fill='red')
        mirerMoydanL = Label(c, text='Mirer Moydan', fg='black', bg='snow3',font='bold')
        c.create_window(450, 340, window=mirerMoydanL)
    if(src=="Kajal Shah" or tar=="Kajal Shah"):
        kajalShah = c.create_oval(600, 310, 700, 370, width=2, fill='red')
        kajalShahL = Label(c, text='Kajal Shah', fg='black', bg='snow3',font='bold')
        c.create_window(650, 340, window=kajalShahL)
    if(src=="Pathan Tula" or tar=="Pathan Tula"):
        pathanTula = c.create_oval(7, 470, 103, 530, width=2, fill='red')
        pathanTulaL = Label(c, text='Pathan Tula', fg='black', bg='snow3',font='bold')
        c.create_window(55, 500, window=pathanTulaL)
    if(src=="Modina Market" or tar=="Modina Market"):
        modinaMarket  = c.create_oval(200, 470, 322, 530, width=2, fill='red')
        modinaMarketL = Label(c, text='Modina Market', fg='black', bg='snow3',font='bold')
        c.create_window(261, 500, window=modinaMarketL)
    if(src=="Bagh Bari" or tar=="Bagh Bari"):
        baghBari= c.create_oval(420, 470, 520, 530, width=2, fill='red')
        baghBariL = Label(c, text='Bagh Bari', fg='black', bg='snow3',font='bold')
        c.create_window(470, 500, window=baghBariL)
        
        
class solutionPath:
    def __init__(self,parent,src,target):
        for key,value in parent.items():
            print(key,'-->',value)
            resetOval(key,value)
            resetLine(key,value)
            
class DijsolutionPath:
    def __init__(self,path,src,target):
        n = len(path)
        for x in range(n-1):
            key = path[x]
            value = path[x+1]
            print(key,'-->',value)
            resetOval(key,value)
            resetLine(key,value)
            
            

def setLine():
    #print("resetColor")
    moAm = c.create_line(100,35,198,35,width=5,fill='snow')
    amDo = c.create_line(302,35,400,35,width=5,fill='snow')
    doCh = c.create_line(510,35,600,35,width=5,fill='snow')
    mopi = c.create_line(55,70,55,160,width=5,fill='snow')
    piHs = c.create_line(100,190,193,190,width=5,fill='snow')
    hsRg = c.create_line(307,190,400,190,width=5,fill='snow')
    hsAm = c.create_line(248,70,248,160,width=5,fill='snow')
    doRg = c.create_line(455,70,455,160,width=5,fill='snow')
    cuRk = c.create_line(650,70,650,160,width=5,fill='snow')
    piKo = c.create_line(55,220,55,310,width=5,fill='snow')
    koSU = c.create_line(100,340,198,340,width=5,fill='snow')
    hsSu = c.create_line(255,220,255,310,width=5,fill='snow')
    suMi = c.create_line(302,340,395,340,width=5,fill='snow')
    kaRk = c.create_line(650,220,650,310,width=5,fill='snow')
    moPa = c.create_line(103,500,200,500,width=5,fill='snow')
    moBa = c.create_line(322,500,420,500,width=5,fill='snow')
    paSu = c.create_line(55,475,258,368,width=5,fill='snow')
    baKj = c.create_line(470,472,650,368,width=5,fill='snow')
    miRi = c.create_line(450,313,652,218,width=5,fill='snow')
    
    
    
def setOval():
    mojumdar = c.create_oval(10, 10, 100, 70, width=2, fill='snow3')
    mojumdarL = Label(c, text='Mojumdar',fg='black', bg='snow3',font='bold')
    c.create_window(55, 40, window=mojumdarL)
    
    amborkhana = c.create_oval(198, 10, 302, 70, width=2, fill='snow3')
    amborkhanaL = Label(c, text='Amborkhana',fg='black', bg='snow3',font='bold')
    c.create_window(250, 40, window=amborkhanaL)
    
    dorgahGate = c.create_oval(400, 10, 510, 70, width=2, fill='snow3')
    dorgahGateL = Label(c, text='Dorgah Gate',fg='black', bg='snow3',font='bold')
    c.create_window(455, 40, window=dorgahGateL)
    
    chuhatta = c.create_oval(600, 10, 700, 70, width=2, fill='snow3')
    chuhattaL = Label(c, text='Chuhatta',fg='black', bg='snow3',font='bold')
    c.create_window(650, 40, window=chuhattaL)    
    
    Pirmoholla = c.create_oval(10, 160, 100, 220, width=2, fill='snow3')
    PirmohollaL = Label(c, text='Pirmoholla',fg='black', bg='snow3',font='bold')
    c.create_window(53, 190, window=PirmohollaL)
        
    housingState = c.create_oval(193, 160, 307, 220, width=2, fill='snow3')
    housingStateL = Label(c, text='Housing State',fg='black', bg='snow3',font='bold')
    c.create_window(250, 190, window=housingStateL)    
    
    rajarGoli = c.create_oval(400, 160, 500, 220, width=2, fill='snow3')
    rajarGoliL = Label(c, text='Rajar Goli', fg='black', bg='snow3',font='bold')
    c.create_window(450, 190, window=rajarGoliL)    
    
    rikabiBazar = c.create_oval(595, 160, 705, 220, width=2, fill='snow3')
    rikabiBazarL = Label(c, text='Rikabi Bazar', fg='black', bg='snow3',font='bold')
    c.create_window(650, 190, window=rikabiBazarL)    
    
    kolapara = c.create_oval(10, 310, 100, 370, width=2, fill='snow3')
    kolaparaL = Label(c, text='Kolapara', fg='black', bg='snow3',font='bold')
    c.create_window(55, 340, window=kolaparaL)    
    
    subidBazar = c.create_oval(198, 310, 302, 370, width=2, fill='snow3')
    subidBazarL = Label(c, text='Subid Bazar',fg='black', bg='snow3',font='bold')
    c.create_window(250, 340, window=subidBazarL)    
    
    mirerMoydan = c.create_oval(395, 310, 505, 370, width=2, fill='snow3')
    mirerMoydanL = Label(c, text='Mirer Moydan', fg='black', bg='snow3',font='bold')
    c.create_window(450, 340, window=mirerMoydanL)    
    
    kajalShah = c.create_oval(600, 310, 700, 370, width=2, fill='snow3')
    kajalShahL = Label(c, text='Kajal Shah', fg='black', bg='snow3',font='bold')
    c.create_window(650, 340, window=kajalShahL)    
        
    pathanTula = c.create_oval(7, 470, 103, 530, width=2, fill='snow3')
    pathanTulaL = Label(c, text='Pathan Tula', fg='black', bg='snow3',font='bold')
    c.create_window(55, 500, window=pathanTulaL)
        
    modinaMarket  = c.create_oval(200, 470, 322, 530, width=2, fill='snow3')
    modinaMarketL = Label(c, text='Modina Market', fg='black', bg='snow3',font='bold')
    c.create_window(261, 500, window=modinaMarketL)
        
    baghBari= c.create_oval(420, 470, 520, 530, width=2, fill='snow3')
    baghBariL = Label(c, text='Bagh Bari', fg='black', bg='snow3',font='bold')
    c.create_window(470, 500, window=baghBariL)
    


c = Canvas(window,height=1100,width=680,bg='gray')
c.pack(expand=YES, fill=BOTH)
BLOCK = c.create_rectangle(750, 70, 1050, 400, width=2, fill='white')
setOval()
setLine()



sourceL = Label(c, text='Enter Source:         ', fg='black', bg='sky blue',font='bold')
c.create_window(100, 570, window=sourceL)
sourceE = Entry(c, bd =4,width=25,justify=CENTER,fg='red',bg='white',font='bold')
sourceE.pack(side = RIGHT)
c.create_window(290, 570, window=sourceE)


destinationL = Label(c, text='Enter Destination: ', fg='black', bg='sky blue',font='bold')
c.create_window(100, 620, window=destinationL)
destinationE = Entry(c, bd =4,width=25,justify=CENTER,fg='red',bg='white',font='bold')
destinationE.pack(side = RIGHT)
c.create_window(290, 620, window=destinationE)


algorithm = Label(c, text=' Select an algorithm:     ', fg='black', bg='deep sky blue',font='bold')
c.create_window(900, 151, window=algorithm)
var = IntVar()
IDS = Checkbutton(c, text = "IDS Search    ", variable = var, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20, fg='black', bg='sky blue')
Astar = Checkbutton(c, text = "Dijsktra          ", variable = var, \
                 onvalue = 2, offvalue = 0, height=2, \
                 width = 20, fg='black', bg='sky blue')
#RBFS = Checkbutton(c, text = "RBFS Search", variable = var, \
#                 onvalue = 3, offvalue = 0, height=2, \
#                 width = 20, fg='black', bg='sky blue')
c.create_window(900, 183, window=IDS)
c.create_window(900, 213, window=Astar)
#c.create_window(900, 243, window=RBFS)


class Graph: 
    def __init__(self,vertices): 
        self.V = vertices 
        self.graph = defaultdict(list) 
        
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def DLS(self,src,target,depthLimit):
        
        parent = {}
        #setOval()
        #setLine()
        
        if src == target :
            print('The solutin path is:-------')
            return True
        if depthLimit <= 0 :
            return False
        for i in self.graph[src]:
            parent[src] = i
            #for key,value in parent.items():
                #print(key,'-->',value)
               # resetOval(key,value)
                #resetLine(key,value)
               # time.sleep(0.1)
               # c.update()
            if(self.DLS(i,target,depthLimit-1)):
                solutionPath(parent,src,target)
                return True
            
        return False
    def IDDFS(self,src, target, maxDepth): 
        for i in range(maxDepth):
            if (self.DLS(src, target, i)): 
                return True
        return False



class GraphDijkstraI():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight



def DIjInput():
    g2.add_edge('Mojumdar','Amborkhana',3200) 
    g2.add_edge('Mojumdar', 'Pirmoholla',2300) 
    g2.add_edge('Amborkhana', 'Dorgah Gate',750) 
    g2.add_edge('Amborkhana', 'Housing State',320) 
    g2.add_edge('Dorgah Gate', 'Chuhatta',400) 
    g2.add_edge('Dorgah Gate', 'Rajar Goli',230) 
    g2.add_edge('Chuhatta','Rikabi Bazar',643) 
    g2.add_edge('Pirmoholla','Housing State',878) 
    g2.add_edge('Pirmoholla','Kolapara',283) 
    g2.add_edge('Housing State','Rajar Goli',620) 
    g2.add_edge('Housing State','Subid Bazar',1220) 
    g2.add_edge('Rikabi Bazar','Kajal Shah',523) 
    g2.add_edge('Rikabi Bazar', 'Mirer Moydan',325) 
    g2.add_edge('Kolapara','Subuid Bazar',940) 
    g2.add_edge('Subid Bazar','Mirer Moydan',705) 
    g2.add_edge('Subid Bazar','Pathan Tula',423) 
    g2.add_edge('Kajal Shah','Bagh Bari',2600)
    g2.add_edge('Pathan Tula','Modina Market',1180)
    g2.add_edge('Modina Market','Bagh Bari',1470)

g2 = GraphDijkstraI()
DIjInput()

def dijsktra(graph, initial, end):
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Goal Not Found"
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    path = path[::-1]
    DijsolutionPath(path,initial,end)
    print(path)
    return path




g = Graph(39)
IDSinput()
disLevel()
def setColor():
    setOval()
    setLine()
restartB = tkinter.Button(c, text ="reset",font='bold',bg='sky blue',activebackground='cyan',height=1,width=8,command=setColor)
c.create_window(850, 300, window=restartB)


def STARTt():
    #print("STARTt")
    target = destinationE.get(); maxDepth = 10; src = sourceE.get()
    m = var.get()
    #print(m)
    if m==1:
        if g.IDDFS(src, target, maxDepth) == True: 
            print ("YES.The Path is reachable") 
        else : 
            print ("NO")
    elif m==2:
        dijsktra(g2, src,target)
    #time.sleep(1)
pathB = tkinter.Button(c, text ="Find path",font='bold',bg='sky blue',activebackground='cyan',height=1,width=8,command=STARTt)
c.create_window(950, 300, window=pathB)


window.mainloop()
