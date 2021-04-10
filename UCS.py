goal=[]
s=[]
class graphInput:
    def Input(self,x):
        d={}
        wd={}
        gR={}
        for i in range(x):
            node=input("Node Name ")
            
            y=int(input("Enter Number of Node child "))
            #huristic.append(pathCost)
            dH={}
            c=[]
            for j in range(y):
                
                child=input("Enter Child Name :")
                pathCost=int(input("Enter Path Cost : "))
                dH[child]=pathCost
                c.append(child)
                print(dH)
                
                #c.append(child)
            d[node]=c
            wd[node]=dH
            gR[node]=c
        PrintValue(d,dH,wd,gR)

class PrintValue:
    def __init__(self,Node,Huristic,Weited,gR):
        print("Node ",Node)
        print("Huristic Value ",Huristic)
        print("Weigth Value ",Weited)
        print("graph",gR)
        startNode=input("Enter The Start Node : ")
        numberOfGoal=int(input("Eneter Number of Goal Node : "))
        
        for i in range(numberOfGoal):
            g=input("Enter Goal Node Name : ")
            goal.append(g)
        print("Start Node ",startNode)
        print("Goal Is ",goal)
        ob=parentCost()
        ob.cost(startNode,Weited,gR,goal) 
        
 
class parentCost:
    
    def cost(self,startNode,Weited,gR,goal):
        parrent={}
        f={}
        f[startNode]=0
        pc={}
        pc[startNode]=0
        
        e=[]
        t=[]
        parrent[startNode]=0
        t.append(startNode)
        temp = startNode
        if startNode in goal:
            print("Goal Found At First With 0 Cost ",frontier)
        else:
            c=True
            while c:
                flag=0
                minValue=min(f.keys(),key=f.get)
                
                value=pc[minValue]
                
                f.pop(minValue)
                for each in goal:
                    if minValue in goal:
                        print("goalFound",minValue)
                        
                        solutionPath(startNode,minValue,parrent)
                        flag=1
                        c=False
                        break
                    
                e.append(minValue)
                pc.pop(minValue)
                print(minValue,"Parent Cost ",value)
                for i in Weited[minValue]:
                   
                    tt=int(Weited[minValue][i])
                    NodeCost=int(tt)+int(value)
                    f[i] = NodeCost
                    NODE = minValue
                
                if flag==1:
                    break
                global s
                ttt=min(f.keys(),key=f.get)
                pc[ttt]=f[ttt]
                s.append(NODE)
                parrent[ttt]=f[ttt]

                #t.append(tt)
                    
                    
class solutionPath:
    def __init__(self,startNode,minValue,parrent):
        
        global s    
       
        #solution=[minValue]
        solution=[]
        solution=s
        solution.append(minValue)
        cn=startNode
        while True:
            
            if cn is startNode:
                break
            solution.append(parrent[cn])
            cn=parrent[cn]
       #solution.reverse()
        print("Goal Found At : ",solution[-1])
       #print("Solution Path : ")
        print("GOAL FOUND AT ")
        solution.pop(0)
        for i in solution:
            if i ==solution[-1]:
                print(i)
            else:
                print(i,"-->",end='')

    
        

n=int(input("Enter Number of Node : "))

graphObject=graphInput()
graphObject.Input(n)