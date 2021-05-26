from manimlib.imports import *

class Node:
    def __init__(self,val):
        self.data = val
        self.text = TextMobject(str(val))
        self.circle = Circle(radius = 0.5,color = WHITE)
        self.location = 0
        self.copyText = TextMobject(str(val))
        self.copyTextlocation = 0
        self.startingpoint = [0,0,0]
        self.endingpoint = [0,0,0]
        self.line = Line(self.startingpoint,self.endingpoint)
        
    def createNode(self,type,place,runtime):
        self.text.move_to(place)
        self.circle.move_to(self.text)
        self.location = place
        type.play(Write(self.text),ShowCreation(self.circle),run_time=runtime)

    def fall(self,type,place,runtime):
        type.play(self.text.shift,place,self.circle.shift,place,run_time=runtime)

    def drawLine(self,type,node,runtime):
        self.startingpoint = self.circle
        self.endingpoint = node.circle
        self.line = Line(self.startingpoint,self.endingpoint)

        type.play(ShowCreation(self.line),run_time = runtime)
    
    def createNewNode(self,type,node,place,height):
        self.createNode(type,3.5*UP,0.3)
        self.fall(type, 1.5*DOWN, 0.25)
        if place=='l':
            self.location = node.location+ (0.8*LEFT) + height*DOWN
            self.fall(type, self.location, 0.5)
        elif place=='r': 
            self.location = node.location + (0.8*RIGHT) + height*DOWN 
            self.fall(type, self.location, 0.5)

    def compare(self,type,node,opt,runtime):
        self.circle.set_fill(RED, opacity=0.5)
        node.circle.set_fill(RED, opacity=0.5)
        type.play(self.circle.scale,1.2,node.circle.scale,1.2,self.text.scale,1.2,node.text.scale,1.2,run_time=runtime)
        
        if opt=="Min":
            if(self.data<node.data):
                self.line,node.line=node.line,self.line
                self.location,node.location = node.location,self.location
                type.play(self.circle.move_to,node.circle,self.text.move_to,node.text,node.circle.move_to,self.circle,node.text.move_to,self.text,run_time=runtime)
        elif opt=="Max":
            if(self.data>node.data):
                self.line,node.line=node.line,self.line
                self.location,node.location = node.location,self.location
                type.play(self.circle.move_to,node.circle,self.text.move_to,node.text,node.circle.move_to,self.circle,node.text.move_to,self.text,run_time=runtime)
        self.circle.set_fill(RED, opacity=0)
        node.circle.set_fill(RED, opacity=0)
        type.play(self.circle.scale,0.825,node.circle.scale,0.825,self.text.scale,0.825,node.text.scale,0.825,run_time=runtime)

    def compareWithArray(self,type,node,opt,runtime):
        self.circle.set_fill(RED, opacity=0.5)
        node.circle.set_fill(RED, opacity=0.5)
        type.play(self.circle.scale,1.2,node.circle.scale,1.2,self.text.scale,1.2,node.text.scale,1.2,run_time=runtime)
        
        if opt=="Min":
            if(self.data<node.data):
                self.line,node.line=node.line,self.line
                self.copyTextlocation,node.copyTextlocation= node.copyTextlocation,self.copyTextlocation
                self.location,node.location = node.location,self.location
                type.play(self.copyText.set_fill,RED,node.copyText.set_fill,RED)
                type.play(self.circle.move_to,node.circle,self.text.move_to,node.text,node.circle.move_to,self.circle,node.text.move_to,self.text,self.copyText.move_to,node.copyText,node.copyText.move_to,self.copyText,run_time=runtime)
                type.play(self.copyText.set_fill,WHITE,node.copyText.set_fill,WHITE)
        elif opt=="Max":  
            if(self.data>node.data):
                self.line,node.line=node.line,self.line
                self.location,node.location = node.location,self.location
                type.play(self.copyText.set_fill,RED,node.copyText.set_fill,RED)
                type.play(self.circle.move_to,node.circle,self.text.move_to,node.text,node.circle.move_to,self.circle,node.text.move_to,self.text,self.copyText.move_to,node.copyText,node.copyText.move_to,self.copyText,run_time=runtime)
                type.play(self.copyText.set_fill,WHITE,node.copyText.set_fill,WHITE)
        self.circle.set_fill(RED, opacity=0)
        node.circle.set_fill(RED, opacity=0)
        type.play(self.circle.scale,0.825,node.circle.scale,0.825,self.text.scale,0.825,node.text.scale,0.825,run_time=runtime)
    
            
    def compareMultiNodes(self,type,node,node1,opt,runtime):
        node.circle.set_fill(RED, opacity=0.5)
        node1.circle.set_fill(RED, opacity=0.5)
        type.play(node1.circle.scale,1.2,node.circle.scale,1.2,run_time = runtime)
        node.circle.set_fill(RED, opacity=0)
        node1.circle.set_fill(RED, opacity=0)
        type.play(node1.circle.scale,0.825,node.circle.scale,0.825,run_time = runtime)

        if opt=="Min":
            if(node1.data<node.data):
                self.compare(type,node1,"Max",runtime)
                    
            else:
                self.compare(type,node,"Max",runtime)

        elif opt=="Max":
            if(node1.data>node.data):
                self.compare(type,node1,"Min",runtime)
            else:
                self.compare(type,node,"Min",runtime)


    def compareWithArrayBox(self,type,node,node1,opt,runtime):
        node.circle.set_fill(RED, opacity=0.5)
        node1.circle.set_fill(RED, opacity=0.5)
        type.play(node1.circle.scale,1.2,node.circle.scale,1.2,run_time = runtime)
        node.circle.set_fill(RED, opacity=0)
        node1.circle.set_fill(RED, opacity=0)
        type.play(node1.circle.scale,0.825,node.circle.scale,0.825,run_time = runtime)
        if opt=="Min":
            if(node1.data<node.data):
                self.compareWithArray(type,node1,"Max",runtime)
                    
            else:
                self.compareWithArray(type,node,"Max",runtime)

        elif opt=="Max":
            if(node1.data>node.data):
                self.compareWithArray(type,node1,"Min",runtime)
            else:
                self.compareWithArray(type,node,"Min",runtime)

            
    def remove(self,type,runtime,node=None):
        if(node==None):
            type.play(FadeOut(self.circle),FadeOut(self.text),run_time=runtime)
        else:
            self.removeLine(type,node,run_time=runtime)
            type.play(FadeOut(self.circle),FadeOut(self.text),run_time=runtime)
        
    def swapWithArray(self,type,node,runtime):
        self.location,node.location = node.location,self.location
        node.location = self.location + 2*UP
        type.play(self.copyText.set_fill,RED,node.copyText.set_fill,RED,node.circle.move_to,node.location,node.text.move_to,node.location,self.circle.move_to,self.location,self.text.move_to,self.location,run_time=runtime)
        type.play(self.copyText.set_fill,WHITE,node.copyText.set_fill,WHITE)

    def swap(self,type,node,runtime):
        self.location,node.location = node.location,self.location
        node.location = self.location + 2*UP
        type.play(self.circle.move_to,self.location,self.text.move_to,self.location,node.circle.move_to,node.location,node.text.move_to,node.location,run_time=runtime)
        
        
    def removeLine(self,type,node,runtime):
        type.play(FadeOut(self.line),run_time = runtime)

    def createArray(self,type,place,runtime,no=None):
        if no==None:
            self.copyTextlocation = 3.5*DOWN+place
            self.copyText.move_to(self.circle)
            type.play(self.copyText.move_to,3.5*DOWN+place,run_time = runtime)
        
        else:
            number = TextMobject(str(no))
            self.copyTextlocation = 3.5*DOWN+place
            self.copyText.move_to(self.circle)
            number.move_to(place+2.5*DOWN)
            type.play(Write(number),self.copyText.move_to,3.5*DOWN+place,run_time = runtime)
        
    def appendArray(self,type,node,runtime,no=None):
        if no==None:
            self.copyTextlocation = node.copyTextlocation+0.9*RIGHT
            self.copyText.move_to(self.circle)
            type.play(self.copyText.move_to,self.copyTextlocation,run_time = runtime)
        
        else:
            number = TextMobject(str(no))
            self.copyTextlocation = node.copyTextlocation+0.9*RIGHT
            self.copyText.move_to(self.circle)
            number.move_to(node.copyTextlocation+0.9*RIGHT+UP)
            type.play(Write(number),self.copyText.move_to,self.copyTextlocation,run_time = runtime)
    
    def updateData(self,val):
        self.data = val
        self.text = TextMobject(str(val))
        self.text.move_to(self.location)

class Heap(Scene):
    def construct(self):
        self.intro('1')
        minheap = VGroup() 

        for mob in self.mobjects:   ## shi ta mya objects tway a kone uu thone lyk tar.
            minheap.add(mob)
        self.play(FadeOut(minheap))
         
        self.intro('2')
        maxheap = VGroup()
        for mob in self.mobjects:   ## shi ta mya objects tway a kone uu thone lyk tar.
            maxheap.add(mob)
        self.play(FadeOut(maxheap))

        minheap.scale(0.4)
        minheap.to_edge(LEFT)
        maxheap.scale(0.5)
        maxheap.to_edge(RIGHT)
        self.play(FadeIn(minheap),FadeIn(maxheap))
            
        self.intro('3')
        self.wait()
        
        self.intro('4')
        self.intro('5')
        self.intro('6')
        self.wait()

    def intro(self,opt):
        if opt == '1':
            text = TextMobject("Heap").to_edge(UP)
            text1 = TextMobject("Heap is a form of priority queue").move_to(2*UP)
            textext = TextMobject("and is one of the most used data structure").move_to(UP)
            text2 = TextMobject("Today we are gonna cover binary heaps")

            self.play(Write(text))
            self.play(Write(text1))
            self.play(Write(textext))
            self.play(Write(text2))
            self.wait()
            self.play(FadeOut(text),FadeOut(text1),FadeOut(text2),FadeOut(textext))
            text3 = TextMobject("Min Heap").move_to(6*LEFT)
            text4 = TextMobject("Max Heap").move_to(6*RIGHT)
            line1 = Line(text,text3)
            line2 = Line(text,text4)
            self.play(Write(text),Write(text3),Write(text4),ShowCreation(line1),ShowCreation(line2))
            self.play(FadeOut(text),FadeOut(text3),FadeOut(text4),FadeOut(line1),FadeOut(line2))
            self.wait()
            
            text = TextMobject("Min Heap Property")
            text.to_edge(UP)
            text1 = TextMobject("The parent node must always be smaller than the children").to_edge(DOWN)
            self.play(Write(text),Write(text1))
            runtime = 0.6
            a = Node("1")
            a.createNode(self,2*UP,runtime)

            b = Node("3")
            b.createNode(self,UP+4*LEFT,runtime)
            b.drawLine(self,a,runtime)

            c = Node("10")
            c.createNode(self,UP+4*RIGHT,runtime)
            c.drawLine(self,a,runtime)

            d = Node("4")
            d.createNode(self,5.5*LEFT,runtime/2)
            d.drawLine(self,b,runtime/2)
        
            e = Node("5")
            e.createNode(self,2.5*LEFT,runtime/2)
            e.drawLine(self,b,runtime/2)

            f = Node("16")
            f.createNode(self,2.5*RIGHT,runtime/2)
            f.drawLine(self,c,runtime/2)
        
            g = Node("100")
            g.createNode(self,5.5*RIGHT,runtime/2) 
            g.drawLine(self,c,runtime/2)
            self.play(FadeOut(text),FadeOut(text1))
            self.wait()
            
        
        if opt == '2':
            text = TextMobject("Max Heap Property")
            text.to_edge(UP)
            text1 = TextMobject("The parent node must always be bigger than the children").move_to(text).move_to(DOWN)
            text1.to_edge(DOWN)
            self.play(Write(text),Write(text1))
            runtime = 0.6
            a = Node("100")
            a.createNode(self,2*UP,runtime)

            b = Node("50")
            b.createNode(self,UP+4*LEFT,runtime)
            b.drawLine(self,a,runtime)

            c = Node("10")
            c.createNode(self,UP+4*RIGHT,runtime)
            a.drawLine(self,c,runtime)

            d = Node("45")
            d.createNode(self,5.5*LEFT,runtime/2)
            b.drawLine(self,d,runtime/2)
        
            e = Node("8")
            e.createNode(self,2.5*LEFT,runtime/2)
            e.drawLine(self,b,runtime/2)

            f = Node("5")
            f.createNode(self,2.5*RIGHT,runtime/2)
            f.drawLine(self,c,runtime/2)
        
            g = Node("9")
            g.createNode(self,5.5*RIGHT,runtime/2)
            g.drawLine(self,c,runtime/2)
            
            self.play(FadeOut(text),FadeOut(text1))
            self.wait()
            

        if(opt=='3'):
            
            text = TextMobject("Min Heap")
            text.shift(3.5*LEFT+1*DOWN)
            text1 = TextMobject("Max Heap")
            text1.shift(3.5*RIGHT+1*DOWN)
            self.play(Write(text),Write(text1))
            self.wait(3)
            object = VGroup()
            for mob in self.mobjects:   
                object.add(mob)
            self.play(FadeOut(object))

            self.wait()

        if(opt == '4'):
            runtime = 0.3
            a = Node(100)
            a.createNode(self,2*UP,runtime)

            b = Node(50)
            b.createNode(self,UP+4*LEFT,runtime)
            b.drawLine(self,a,runtime)
            c = Node(10)
            c.createNode(self,UP+4*RIGHT,runtime)
            c.drawLine(self,a,runtime)

            d = Node(45)
            d.createNode(self,5.5*LEFT,runtime/2)
            d.drawLine(self,b,runtime/2)

            e = Node(8)
            e.createNode(self,2.5*LEFT,runtime/2)
            b.drawLine(self,e,runtime/2)
    
            f = Node(5)
            f.createNode(self,2.5*RIGHT,runtime/2)
            f.drawLine(self,c,runtime/2)
            g = Node(9)
            g.createNode(self,5.5*RIGHT,runtime/2)
            g.drawLine(self,c,runtime/2)
            self.wait()
            
            text = TextMobject("Insert[1000,500,10,30,5,999,100,80]")
            text.to_edge(LEFT+DOWN)
            self.play(Write(text),run_time=1)

            runtime = 0.8
            newNode = Node(1000)
            newNode.createNewNode(self,d,'l',3)
            newNode.drawLine(self,d,runtime)

            newNode.compare(self,d,"Max",runtime)
            newNode.compare(self,b,"Max",runtime)
            newNode.compare(self,a,"Max",runtime)
            
            newNode2 = Node(500)
            newNode2.createNewNode(self,b,'r',3)
            newNode2.drawLine(self,b,runtime)
            newNode2.compare(self,b,"Max",runtime)
            newNode2.compare(self,a,"Max",runtime)
            newNode2.compare(self,newNode,"Max",runtime)
            
            newNode3 = Node(10)
            newNode3.createNewNode(self,e,'l',3)
            newNode3.drawLine(self,e,runtime)
            newNode3.compare(self,e,"Max",runtime)
            newNode3.compare(self,newNode2,"Max",runtime)

            newNode4 = Node(30)
            newNode4.createNewNode(self,newNode3,'r',3)
            newNode4.drawLine(self,newNode3,runtime)
            newNode4.compare(self,newNode3,"Max",runtime)
            newNode4.compare(self,newNode2,"Max",runtime)

            ##End of left side
            runtime = 0.1
            rightNode1 = Node(5)
            rightNode1.createNewNode(self,f,'l',3)
            rightNode1.drawLine(self,f,runtime)
            rightNode1.compare(self,f,"Max",runtime)
            
            rightNode2 = Node(999)
            rightNode2.createNewNode(self,f,'r',3)
            rightNode2.drawLine(self,f,runtime)
            rightNode2.compare(self,f,"Max",runtime)
            rightNode2.compare(self,c,"Max",runtime)
            rightNode2.compare(self,newNode,"Max",runtime)

            rightNode3 = Node(100)
            rightNode3.createNewNode(self,g,'l',3)
            rightNode3.drawLine(self,g,runtime)
            rightNode3.compare(self,g,"Max",runtime)
            rightNode3.compare(self,rightNode2,"Max",runtime)

            rightNode4 = Node(80)
            rightNode4.createNewNode(self,rightNode3,'r',3)
            rightNode4.drawLine(self,rightNode3,runtime)
            rightNode4.compare(self,rightNode3,"Max",runtime)

            self.wait(5)
            self.play(FadeOut(text),run_time=1)
            #INERSION FINISHED
            text = TextMobject("Remove[80]")
            text.to_edge(LEFT+DOWN)
            text1 = TextMobject("O(1)")
            text1.to_edge(DOWN)
            self.play(Write(text),run_time=1)
            rightNode4.remove(self,0.3)
            rightNode4.removeLine(self,rightNode3,runtime)
            
            self.play(Write(text1),run_time=1)
            self.play(FadeOut(text),FadeOut(text1),run_time=runtime)
            del rightNode4
            self.wait(3)

            rightNode4 = Node(80)
            rightNode4.createNode(self,6.3*RIGHT+DOWN, runtime)
            rightNode4.drawLine(self,rightNode3,runtime)
            self.wait(3)
            text = TextMobject("Remove root")
            text.to_edge(LEFT+DOWN)
            self.play(Write(text),run_time=1)
            text1 = TextMobject("O(log(n))")
            text1.to_edge(DOWN)
            self.play(Write(text),run_time=1)
            
            rightNode4.removeLine(self,rightNode3,runtime)
            rightNode4.swap(self,newNode,2)
            self.wait(3)
            newNode.remove(self,0.3)
            rightNode4.compareMultiNodes(self,newNode2,rightNode2,"Max",runtime)
            self.wait() 

            rightNode4.compareMultiNodes(self,rightNode3,c,"Max",runtime)
            
            self.wait(3)

            g.removeLine(self,g,runtime)
            g.swap(self,rightNode2,1)
            rightNode2.remove(self,1)
            g.compareMultiNodes(self,newNode2,rightNode3,"Max",1)
            g.compareMultiNodes(self,newNode4,a,"Max",1)
            g.compareMultiNodes(self,d,b,"Max",1)
            self.play(Write(text1),run_time=1)
            self.wait()
            self.play(FadeOut(text),FadeOut(text1),run_time=runtime)
            self.wait()
            object = VGroup()
            for mob in self.mobjects:   ## shi ta mya objects tway a kone uu thone lyk tar.
                object.add(mob)
            self.play(FadeOut(object))


        if opt=='5':
            runtime = 0.3
            a = Node(0)
            a.createNode(self,2*UP,runtime)

            b = Node(1)
            b.createNode(self,UP+4*LEFT,runtime)
            a.drawLine(self,b,runtime)

            c = Node(2)
            c.createNode(self,UP+4*RIGHT,runtime)
            a.drawLine(self,c,runtime)

            d = Node(3)
            d.createNode(self,6*LEFT,runtime/2)
            b.drawLine(self,d,runtime/2)

            e = Node(4)
            e.createNode(self,2*LEFT,runtime/2)
            b.drawLine(self,e,runtime/2)
    
            f = Node(5)
            f.createNode(self,2*RIGHT,runtime/2)
            c.drawLine(self,f,runtime/2)
            
            g = Node(6)
            g.createNode(self,6*RIGHT,runtime/2)
            c.drawLine(self,g,runtime/2)

            h = Node(7)
            h.createNode(self,d.location+(0.8*LEFT)+DOWN,runtime)
            d.drawLine(self,h,runtime/2)

            i = Node(8)
            i.createNode(self,d.location+(0.8*RIGHT)+DOWN,runtime)
            d.drawLine(self,i,runtime)

            j = Node(9)
            j.createNode(self,e.location+(0.8*LEFT)+DOWN,runtime)
            e.drawLine(self,j,runtime)

            k = Node(10)
            k.createNode(self,e.location+(0.8*RIGHT)+DOWN,runtime/2)
            e.drawLine(self,k,runtime/2)

            l = Node(11)
            l.createNode(self,f.location+(0.8*LEFT)+DOWN,runtime/2)
            f.drawLine(self,l,runtime/2)
    
            m = Node(12)
            m.createNode(self,f.location+(0.8*RIGHT)+DOWN,runtime/2)
            f.drawLine(self,m,runtime/2)
            
            n = Node(13)
            n.createNode(self,g.location+(0.8*LEFT)+DOWN,runtime/2)
            g.drawLine(self,n,runtime/2)

            o = Node(14)
            o.createNode(self,g.location+(0.8*RIGHT)+DOWN,runtime/2)
            g.drawLine(self,o,runtime/2)

            self.wait()

            NodeList = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
            a.createArray(self,6.5*LEFT,1)

            object = VGroup()
            for i in range(1,len(NodeList)):
                NodeList[i].appendArray(self,NodeList[i-1],1)
            object = VGroup()
            for mob in self.mobjects:   ## shi ta mya objects tway a kone uu thone lyk tar.
                object.add(mob)
            
            self.wait()
            self.play(FadeOut(object),run_time = 3)

        if opt=='6':
            runtime = 0.2
            a = Node(18)
            a.createNode(self,2*UP,runtime)

            b = Node(100)
            b.createNode(self,UP+4*LEFT,runtime)
            b.drawLine(self,a,runtime)

            c = Node(23)
            c.createNode(self,UP+4*RIGHT,runtime)
            c.drawLine(self,a,runtime)

            d = Node(13)
            d.createNode(self,5.5*LEFT,runtime/2)
            d.drawLine(self,b,runtime/2)

            e = Node(4)
            e.createNode(self,2.5*LEFT,runtime/2)
            e.drawLine(self,b,runtime/2)
    
            f = Node(245)
            f.createNode(self,2.5*RIGHT,runtime/2)
            f.drawLine(self,c,runtime/2)
            
            g = Node(123)
            g.createNode(self,5.5*RIGHT,runtime/2)
            g.drawLine(self,c,runtime/2)

            h = Node(9)
            h.createNode(self,d.location+(0.8*LEFT)+DOWN,runtime)
            h.drawLine(self,d,runtime/2)

            i = Node(1)
            i.createNode(self,d.location+(0.8*RIGHT)+DOWN,runtime)
            i.drawLine(self,d,runtime)

            j = Node(87)
            j.createNode(self,e.location+(0.8*LEFT)+DOWN,runtime)
            j.drawLine(self,e,runtime)

            k = Node(64)
            k.createNode(self,e.location+(0.8*RIGHT)+DOWN,runtime/2)
            k.drawLine(self,e,runtime/2)

            l = Node(31)
            l.createNode(self,f.location+(0.8*LEFT)+DOWN,runtime/2)
            l.drawLine(self,f,runtime/2)
    
            m = Node(127)
            m.createNode(self,f.location+(0.8*RIGHT)+DOWN,runtime/2)
            m.drawLine(self,f,runtime/2)
            
            n = Node(555)
            n.createNode(self,g.location+(0.8*LEFT)+DOWN,runtime/2)
            n.drawLine(self,g,runtime/2)

            o = Node(234)
            o.createNode(self,g.location+(0.8*RIGHT)+DOWN,runtime/2)
            o.drawLine(self,g,runtime/2)

            a.createArray(self,6.5*LEFT,0.1,0)
            NodeList = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
            for i in range(1,len(NodeList)):
                NodeList[i].appendArray(self,NodeList[i-1],0.1,i)

            self.wait(10)
            runtime = 1
            NodeList[3].compareWithArrayBox(self,NodeList[7],NodeList[8],"Max",runtime)
            NodeList[4].compareWithArrayBox(self,NodeList[9],NodeList[10],"Max",runtime)
            NodeList[1].compareWithArrayBox(self,NodeList[3],NodeList[9],"Max",runtime)

            NodeList[5].compareWithArrayBox(self,NodeList[11],NodeList[12],"Max",runtime)
            NodeList[6].compareWithArrayBox(self,NodeList[13],NodeList[14],"Max",runtime)
            NodeList[2].compareWithArrayBox(self,NodeList[6],NodeList[13],"Max",runtime)
            NodeList[2].compareWithArrayBox(self,NodeList[6],NodeList[14],"Max",runtime)
            NodeList[0].compareWithArrayBox(self,NodeList[1],NodeList[13],"Max",runtime)

            runtime = 0.01
            NodeList[0].compareWithArrayBox(self,NodeList[5],NodeList[14],"Max",runtime)
            NodeList[0].compareWithArrayBox(self,NodeList[11],NodeList[12],"Max",runtime)

            NodeList[2].removeLine(self,NodeList[14],0.2)
            NodeList[2].swapWithArray(self,NodeList[13],1)
            NodeList[13].remove(self,0.2)
            NodeList[2].compareWithArrayBox(self,NodeList[1],NodeList[5],"Max",runtime)
            NodeList[2].compareWithArrayBox(self,NodeList[12],NodeList[14],"Max",runtime)
            NodeList[2].compareWithArray(self,NodeList[6],"Min",runtime)

            NodeList[2].removeLine(self,NodeList[6],runtime)
            NodeList[2].swapWithArray(self,NodeList[5],runtime)
            NodeList[5].remove(self,runtime)
            NodeList[2].compareWithArrayBox(self,NodeList[1],NodeList[14],"Max",runtime)
            NodeList[2].compareWithArrayBox(self,NodeList[12],NodeList[6],"Max",runtime)
            NodeList[2].compareWithArrayBox(self,NodeList[11],NodeList[0],"Max",runtime)

            NodeList[0].removeLine(self,NodeList[11],runtime)
            NodeList[0].swapWithArray(self,NodeList[14],runtime)
            NodeList[14].remove(self,runtime)
            NodeList[0].compareWithArrayBox(self,NodeList[1],NodeList[12],"Max",runtime)
            NodeList[0].compareWithArrayBox(self,NodeList[11],NodeList[6],"Max",runtime)

            NodeList[2].removeLine(self,NodeList[11],runtime)    
            NodeList[2].swapWithArray(self,NodeList[12],runtime)
            NodeList[12].remove(self,runtime)
            NodeList[2].compareWithArrayBox(self,NodeList[1],NodeList[6],"Max",runtime)
            NodeList[2].compareWithArrayBox(self,NodeList[11],NodeList[0],"Max",runtime)

            NodeList[10].removeLine(self,NodeList[9],runtime)
            NodeList[10].swapWithArray(self,NodeList[6],runtime)
            NodeList[6].remove(self,runtime)
            NodeList[10].compareWithArrayBox(self,NodeList[1],NodeList[11],"Max",runtime)
            NodeList[10].compareWithArrayBox(self,NodeList[3],NodeList[9],"Max",runtime)
            NodeList[10].compareWithArray(self,NodeList[4],"Min",runtime)

            NodeList[4].removeLine(self,NodeList[10],runtime)
            NodeList[4].swapWithArray(self,NodeList[1],runtime)
            NodeList[1].remove(self,runtime)
            NodeList[4].compareWithArrayBox(self,NodeList[9],NodeList[11],"Max",runtime)
            NodeList[4].compareWithArrayBox(self,NodeList[10],NodeList[3],"Max",runtime)

            NodeList[8].removeLine(self,NodeList[3],runtime)
            NodeList[8].swapWithArray(self,NodeList[9],runtime)
            NodeList[9].remove(self,runtime)
            NodeList[8].compareWithArrayBox(self,NodeList[10],NodeList[11],"Max",runtime)
            NodeList[8].compareWithArrayBox(self,NodeList[3],NodeList[4],"Max",runtime)
            NodeList[8].compareWithArray(self,NodeList[7],"Min",runtime)

            NodeList[8].removeLine(self,NodeList[7],runtime)
            NodeList[8].swapWithArray(self,NodeList[10],runtime)
            NodeList[10].remove(self,runtime)
            NodeList[8].compareWithArrayBox(self,NodeList[3],NodeList[11],"Max",runtime)
            NodeList[8].compareWithArrayBox(self,NodeList[2],NodeList[0],"Max",runtime)

            NodeList[0].removeLine(self,NodeList[2],runtime)
            NodeList[0].swapWithArray(self,NodeList[11],runtime)
            NodeList[11].remove(self,runtime)
            NodeList[0].compareWithArrayBox(self,NodeList[3],NodeList[2],"Max",runtime)
            NodeList[0].compareWithArray(self,NodeList[8],"Min",runtime)

            NodeList[8].removeLine(self,NodeList[2],runtime)
            NodeList[8].swapWithArray(self,NodeList[2],runtime)
            NodeList[2].remove(self,runtime)
            NodeList[8].compareWithArrayBox(self,NodeList[3],NodeList[0],"Max",runtime)

            NodeList[4].removeLine(self,NodeList[3],runtime)
            NodeList[4].swapWithArray(self,NodeList[0],runtime)
            NodeList[0].remove(self,runtime)
            NodeList[4].compareWithArrayBox(self,NodeList[3],NodeList[7],"Max",runtime)
            NodeList[4].compareWithArray(self,NodeList[7],"Min",runtime)

            NodeList[4].removeLine(self,NodeList[7],runtime)
            NodeList[4].swapWithArray(self,NodeList[3],runtime)
            NodeList[3].remove(self,runtime)
            NodeList[4].compareWithArrayBox(self,NodeList[8],NodeList[7],"Max",runtime)

            NodeList[8].removeLine(self,NodeList[3],runtime)
            NodeList[8].swapWithArray(self,NodeList[7],runtime)
            NodeList[7].remove(self,runtime)
            NodeList[8].compareWithArray(self,NodeList[4],"Min",runtime)

            NodeList[8].removeLine(self,NodeList[3],runtime)
            NodeList[8].swapWithArray(self,NodeList[4],runtime)
            NodeList[4].remove(self,runtime)
            NodeList[8].remove(self,runtime)
            




            


