from manimlib.imports import *

class ArrayBox:
    def __init__(self,data,index,location):
        self.location = location
        self.ArrayBox  = Rectangle(width=1,height=1).move_to(self.location)
        self.data = TextMobject(str(data)).move_to(self.location)
        self.index = TextMobject(str(index)).move_to(self.location+UP)
        self.index.set_color(BLUE)
    
    def construct(self,type,runtime,opt=True):
        if(opt):
            type.play(FadeIn(self.ArrayBox),Write(self.data),Write(self.index),run_time = runtime)
        else:
            type.play(FadeIn(self.ArrayBox),Write(self.data),run_time = runtime)
            type.play(self.data.shift,UP,run_time=runtime)
            type.play(Write(self.index),run_time=runtime)
        
    def move(self,type,place,runtime):
        self.location+=place
        type.play(self.ArrayBox.shift,place,self.data.shift,place,self.index.shift,place,run_time = runtime)

    def colorChange(self,type):
        self.ArrayBox.set_fill(GREEN,opacity=0.5)
        type.play(self.ArrayBox.scale,1)
        self.ArrayBox.set_fill(GREEN,opacity=0)
        type.play(self.ArrayBox.scale,1)

    def constructForGrid(self,type,data):
        self.data = TextMobject(str(data)).move_to(self.location)
        self.data.scale(0.8)
        self.data.set_color(BLUE)
        type.play(FadeIn(self.ArrayBox),Write(self.data),run_time=0.3)

class Box:
    def __init__(self,key,node=None):
        self.key = TextMobject(str(key))
        self.location = 0
        self.keyStorage = Rectangle(width=1,height=1)
        self.prevPointerStorage = Rectangle(width=1,height=1)
        self.next = Vector([0,0,0])
        self.prev = Vector([0,0,0])
        self.pointerStorage = Rectangle(width=1,height=1)
        self.line = Line().scale(0.6)
        self.prevLine= Line().scale(0.6)
        if(node):
            self.location = node.location + 2*RIGHT

    def construct(self,type):
        self.key.move_to(self.location)
        self.keyStorage.move_to(self.location)
        self.pointerStorage.move_to(self.location+DOWN)
        type.play(FadeIn(self.keyStorage),Write(self.key),FadeIn(self.pointerStorage))

    def constructPointer(self,type,box,opt=True):
        if opt==True:
            self.constructArrow(type,box)
        else:
            self.endOfList(type)

    def constructArrow(self,type,box):
        self.next = Vector(box.location+0.5*LEFT-self.location+UP)
        self.next.move_to(self.location+0.5*DOWN+RIGHT)
        self.next.set_color(BLUE)
        type.play(FadeIn(self.next))
        type.wait()

    def removeFrontPointer(self,type):
        type.play(FadeOut(self.next))
        type.wait()
    

    def endOfList(self,type):
        self.line.move_to(self.location+DOWN)
        self.line.rotate(-3 * TAU / 8)
        type.play(FadeIn(self.line))

    def move(self,place):
        self.location = place

    def clear(self,type):
        type.play(FadeOut(self.key),FadeOut(self.keyStorage),FadeOut(self.next),FadeOut(self.pointerStorage))

    def clearEndNode(self,type):
        type.play(FadeOut(self.key),FadeOut(self.keyStorage),FadeOut(self.next),FadeOut(self.pointerStorage),FadeOut(self.line))
    
    def notEndAnymore(self,type):
        type.play(FadeOut(self.line))

    def move_to(self,type,place):
        runtime = 1
        self.location += place
        type.play(self.pointerStorage.move_to,self.location+UP,self.keyStorage.move_to,self.location+place,run_time = runtime)

    def colorChange(self,type):
        runtime = 1
        self.keyStorage.set_fill(GREEN,opacity=0.5)
        self.pointerStorage.set_fill(GREEN,opacity=0.5)
        type.play(self.keyStorage.scale,1,self.pointerStorage.scale,1,run_time=runtime)
        self.keyStorage.set_fill(GREEN,opacity=0)
        self.pointerStorage.set_fill(RED,opacity=0)
        type.play(self.keyStorage.scale,1,self.pointerStorage.scale,1,run_time=runtime)

    def doubleLinkedList(self,type,node=None):
        self.prevPointerStorage.move_to(self.location+2*DOWN)
        type.play(FadeIn(self.prevPointerStorage))

        if node is not None:
            self.constructPrevPointer(type,node)

    def startofList(self,type):
        self.prevLine.move_to(self.location+2*DOWN)
        self.prevLine.rotate(-3 * TAU/8)
        type.play(FadeIn(self.prevLine))

    def notStartAnymore(self,type):
        type.play(FadeOut(self.prevLine))
    
    def constructPrevPointer(self,type,node):
        self.prev = Vector(node.location+DOWN-self.location+2*UP)
        self.prev.move_to(self.location+1.5*DOWN+LEFT)
        self.prev.set_color(BLUE)
        type.play(FadeIn(self.prev))
        type.wait()

    def removePrevPointer(self,type):
        type.play(FadeOut(self.prev))

headPointer = Vector([0,0,0])
headPointerText = TextMobject("head")
tailPointer = Vector([0,0,0])
tailPointerText = TextMobject("tail")


class ArrayScene(Scene):
    def construct(self):
        self.createArray()

    def createArray(self):
        text = TextMobject("Array")
        self.play(Write(text))
        self.wait()
        self.play(FadeOut(text))
        a = ArrayBox(0,0,2*LEFT)
        b = ArrayBox(1,1,LEFT)
        c = ArrayBox(2,2,0)
        d = ArrayBox(3,3,RIGHT)
        e = ArrayBox(4,4,2*RIGHT)
        a.construct(self,0.3,False)
        b.construct(self,0.3,False)
        c.construct(self,0.3,False)
        d.construct(self,0.3,False)
        e.construct(self,0.3,False)
        self.wait()
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))

        a = ArrayBox(12,0,2*LEFT)
        b = ArrayBox(1,1,LEFT)
        c = ArrayBox(5,2,0)
        d = ArrayBox(19,3,RIGHT)
        e = ArrayBox(9,4,2*RIGHT)
        a.construct(self,0.3,True)
        b.construct(self,0.3,True)
        c.construct(self,0.3,True)
        d.construct(self,0.3,True)
        e.construct(self,0.3,True)
        text = TextMobject("Remove(index 2)").to_edge(DOWN+LEFT)
        text.set_color(YELLOW)
        self.play(Write(text))
        self.wait()
        self.play(FadeOut(c.data))
        text1 = TextMobject("O(1)").to_edge(DOWN+RIGHT)
        self.play(Write(text1))
        self.wait()
        self.play(FadeOut(text),FadeOut(text1))
        
        text = TextMobject("Insert(index 2,3)").to_edge(DOWN+LEFT)
        text.set_color(YELLOW)
        c.data = TextMobject(str(3)).move_to(c.location)
        self.play(Write(text))
        self.play(Write(c.data))
        
        text1 = TextMobject("O(1)").to_edge(DOWN+RIGHT)
        text1.set_color(GREEN)
        self.play(Write(text1))
        self.play(FadeOut(text),FadeOut(text1))
        
        text = TextMobject("Find(3)").to_edge(DOWN+LEFT)
        text.set_color(YELLOW)
        self.play(Write(text))
        a.colorChange(self)
        b.colorChange(self)
        c.colorChange(self)
        text1 = TextMobject("O(n)").to_edge(DOWN+RIGHT)
        text1.set_color(RED)
        self.play(Write(text1))
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))
        self.makeGrid()
    
    def writeText(self,place,time,*string,remove,color,scale,arbitaryPosition=None,position=LEFT,delay=0.1,increase=0):
        object = VGroup()
        a=0
        for i in string:
            if arbitaryPosition is not None:
                try:
                    place = place+scale/2*DOWN+increase*DOWN+arbitaryPosition[a]*position-arbitaryPosition[a-1]*position
                except IndexError:
                    place = place+scale/2*DOWN+increase*DOWN+arbitaryPosition[a]*position
            else:
                place = place+scale/2*DOWN
            text = TextMobject(i)
            text.scale(scale)
            text.set_color(color)
            text.move_to(place)
            object.add(text)
            self.play(Write(text),run_time=time)
            a += 1
        
        if(remove is True):
            self.wait(delay)
            self.play(FadeOut(object))

    def makeGrid(self):
        a = ArrayBox(12,0,DOWN+2*LEFT)
        b = ArrayBox(1,1,DOWN+LEFT)
        c = ArrayBox(5,2,DOWN)
        d = ArrayBox(19,3,DOWN+RIGHT)
        e = ArrayBox(9,4,DOWN+2*RIGHT)
        f = ArrayBox(12,0,2*LEFT)
        g = ArrayBox(1,1,LEFT)
        h = ArrayBox(5,2,0)
        i = ArrayBox(19,3,RIGHT)
        j = ArrayBox(9,4,2*RIGHT)
        k = ArrayBox(12,0,UP+2*LEFT)
        l = ArrayBox(1,1,UP+LEFT)
        m = ArrayBox(5,2,UP+0)
        n = ArrayBox(19,3,UP+RIGHT)
        o = ArrayBox(9,4,UP+2*RIGHT)

        a.constructForGrid(self,[2,0])
        b.constructForGrid(self,[2,1])
        c.constructForGrid(self,[2,2])
        d.constructForGrid(self,[2,3])
        e.constructForGrid(self,[2,4])
        f.constructForGrid(self,[1,0])
        g.constructForGrid(self,[1,1])
        h.constructForGrid(self,[1,2])
        i.constructForGrid(self,[1,3])
        j.constructForGrid(self,[1,4])
        k.constructForGrid(self,[0,0])
        l.constructForGrid(self,[0,1])
        m.constructForGrid(self,[0,2])
        n.constructForGrid(self,[0,3])
        o.constructForGrid(self,[0,4])
        
        row = TextMobject("row").move_to(3.2*LEFT)
        column = TextMobject("column").move_to(2.2*UP)
        row.set_color(YELLOW)
        column.set_color(YELLOW)
        self.play(Write(row),Write(column))
        
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))
        self.writeText(4*UP+3*LEFT,0.3,"Advantages:",\
                               "easy and convenient to use",\
                               remove=False,color=YELLOW,arbitaryPosition=[0,3],position=RIGHT,increase=0.5,scale=0.8)

        
        self.writeText(UP+2.8*LEFT,0.3,"Disadvantages:",\
                               "fixed amount of spaces",\
                               "slightly long time complexity",\
                               remove=False,color=YELLOW,arbitaryPosition=[0,3,3.5],position=RIGHT,increase=0.5,scale=0.8)

        self.wait(3)
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))
        

class LinkedList(Scene):

    def construct(self):
        global headPointer,headPointerText,tailPointer,tailPointerText
        

        self.writeText(0,1,"Linked List",remove=True,color=WHITE,scale=1)
        self.writeText(2*DOWN,1,"It is a sequence of nodes","Each node contains (1) key and (2) next pointer",remove=False,color=WHITE,scale=1)
        a = Box(1)
        a.move(UP+3*LEFT)
        a.construct(self)
        
        b = Box(2,a)
        b.construct(self)
        a.constructPointer(self,b)

        c = Box(3,b)
        c.construct(self)
        b.constructPointer(self,c)
        
        d= Box(4,c)
        d.construct(self)
        c.constructPointer(self,d)
        d.endOfList(self)

        self.wait()
        IntroObject = VGroup()
        for mob in self.mobjects:
            IntroObject.add(mob)
        self.play(FadeOut(IntroObject))

        #start of push front 

        self.writeText(3.5*UP,1,"PushFront(key)",remove=False,color=WHITE,scale=1)
        
        self.writeText(2.5*DOWN+4*LEFT,0.5,"PushFront(10)",remove=False,color=WHITE,scale=0.9)
        a = Box(5)
        a.move(3*LEFT)
        a.construct(self)
        self.createHeadPointer(a)
        c = Box(9, a)
        c.construct(self)
        a.constructPointer(self,c)
        c.endOfList(self)
        self.createTailPointer(c)
        self.writeText(2*UP+4*RIGHT,0.5,"node <- new node",\
                                    "node.key <- key",\
                                    "node.next <- head",remove=False,color=YELLOW,scale=0.8)
         
        self.wait(3)
        b=Box(10)
        b.move(5*LEFT)
        b.construct(self)
        b.constructPointer(self,a)
        
        self.wait(3)
        self.writeText(0.5*UP+4*RIGHT,0.5,"head <- node",remove=False,color=YELLOW,scale=0.8)
        self.play(headPointer.shift,2*LEFT,headPointerText.shift,1.5*LEFT)
        self.wait(3)
        
        self.writeText(4*RIGHT,0.5,"if tail = nil:",\
                                   "   tail<-head",remove=False,color=YELLOW,scale=0.8)
        self.wait(3)

        self.writeText(2.5*DOWN+4*RIGHT,0.5,"O(1)",color=GREEN,remove=False,scale=1)
        self.wait(1)
        pushFrontobject = VGroup()
        for mob in self.mobjects:
            pushFrontobject.add(mob)
        self.play(FadeOut(pushFrontobject))

        #start of pop front
        self.writeText(3.5*UP,1,"PopFront",remove=False,color=WHITE,scale=1)
        self.writeText(2.5*DOWN+4*LEFT,0.5,"PopFront()",remove=False,color=WHITE,scale=0.9)
        
        a = Box(5)
        a.move(UP+2*LEFT)
        a.construct(self)
        self.createHeadPointer(a)
        c = Box(9,a)
        c.construct(self)
        a.constructPointer(self,c)
        c.endOfList(self)
        self.createTailPointer(c)
        self.writeText(2*UP+4*RIGHT,0.5,"if head=nil:",\
                                        "   empty list",\
                                        "head <- head.next",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[1.5,0,1.5])
        self.play(headPointer.shift,2*RIGHT,headPointerText.shift,1.5*RIGHT)
        self.wait(3)
        self.writeText(0.5*UP+4*RIGHT,0.5,"if head=nil:",\
                                        "   tail<-nil",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[1.5,0])
        self.writeText(2.5*DOWN+4*RIGHT,0.5,"O(1)",color=GREEN,remove=False,scale=1)
        self.wait(1)

        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))

        #start of push back
        self.writeText(3.5*UP,1,"PushBack(key)",remove=False,color=WHITE,scale=1)
        
        a = Box(5)
        a.move(UP+5*LEFT)
        a.construct(self)
        self.createHeadPointer(a)
        c = Box(9,a)
        c.construct(self)
        c.endOfList(self)
        self.createTailPointer(c)
        a.constructPointer(self,c)
        
        self.writeText(2.5*DOWN+4*LEFT,0.5,"PushBack(10)",remove=False,color=WHITE,scale=0.9)
        self.writeText(2*UP+4*RIGHT,0.5,"node <- new node",\
                                    "node.key <- key",\
                                    "node.next <- nil",remove=False,color=YELLOW,scale=0.8)
        self.wait(3)

        b = Box(10)
        b.move(UP+LEFT)
        b.construct(self)
        b.endOfList(self)
        
        self.writeText(0.5*UP+4*RIGHT,0.5,"if tail=nil:",\
                                    "head<-tail<-node",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[1.5,0])
        self.wait(3)
        
        self.writeText(0.5*DOWN+4*RIGHT,0.5,"else:",\
                                            "tail.next <- tail",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[2,0])
        c.notEndAnymore(self)
        c.constructPointer(self,b)
        self.writeText(1.5*DOWN+4*RIGHT,0.5,"tail<-next",remove=False,color=YELLOW,scale=0.8)
                   
        self.play(tailPointer.shift,2*RIGHT,tailPointerText.shift,1.5*RIGHT)
        self.wait(3)
        self.writeText(2.5*DOWN+4*RIGHT,0.5,"O(n)",color=RED,remove=False,scale=1)
        self.wait(1)
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))


        #popback
        self.writeText(4*UP,1,"PopBack",remove=False,color=WHITE,scale=1)
        a = Box(5)
        a.move(UP+5*LEFT)
        a.construct(self)
        self.createHeadPointer(a)
        b = Box(9,a)
        b.construct(self)
        a.constructPointer(self,b)
        c = Box(10,b)
        c.construct(self)
        c.endOfList(self)
        b.constructPointer(self,c)
        self.createTailPointer(c)
        
        self.writeText(2.5*DOWN+4*LEFT,0.5,"PopBack()",remove=False,color=WHITE,scale=0.9)
        self.writeText(2*UP+4*RIGHT,0.5,"if head: -> empty list",\
                                        "if head = tail: -> head = tail = nil",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[1.3,0.3])
        self.wait(3)
        self.writeText(1*UP+4*RIGHT,0.5,"else:",\
                                        "p<- head",\
                                        "while p.next.next is not nil:",\
                                        "p<-p.next",remove=False,color=YELLOW,scale=0.8,arbitaryPosition = [2.8,1.7,0,0])
        self.wait(1)
        a.colorChange(self)
        b.colorChange(self)
        self.wait(1)
        self.writeText(1*DOWN+2*RIGHT,0.5,"p.next<-nil",\
                                        "tail<-p",remove=False,color=YELLOW,scale=0.8)
        
        c.notEndAnymore(self)
        b.removeFrontPointer(self)
        b.endOfList(self)
        self.play(tailPointer.shift,2*LEFT,tailPointerText.shift,1.5*LEFT)
        self.wait(3)
        self.writeText(2.5*DOWN+4*RIGHT,0.5,"O(n)",color=RED,remove=False,scale=1)
        self.wait(1)
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))


        #start of add after
        self.writeText(4*UP,1,"AddAfter(node,key)",remove=False,color=WHITE,scale=1)
        
        a = Box(5)
        a.move(UP+5*LEFT)
        a.construct(self)
        self.createHeadPointer(a)
        b = Box(9,a)
        b.construct(self)
        a.constructPointer(self,b)
        c = Box(10,b)
        c.construct(self)
        c.endOfList(self)
        b.constructPointer(self,c)
        self.createTailPointer(c)
        
        self.writeText(2.5*DOWN+4*LEFT,0.5,"AddAfter(9,8)",remove=False,color=WHITE,scale=0.9)
        self.writeText(2*UP+4*RIGHT,0.5,"node2 <- new node",\
                                        "node2.key = key",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[0,0.3])
        self.wait(3)
        d = Box(8)
        d.move(1.4*DOWN+1.8*LEFT)
        d.construct(self)
        self.writeText(UP+4*RIGHT,0.5,"node2.next = node.next",\
                                   "node.next = node2",remove=False,color=YELLOW,scale=0.8,arbitaryPosition = [0,0.3])
        b.removeFrontPointer(self)
        self.play(c.pointerStorage.shift,2*RIGHT,c.keyStorage.shift,2*RIGHT,c.key.shift,2*RIGHT,c.line.shift,2*RIGHT,tailPointer.shift,2*RIGHT,tailPointerText.shift,2*RIGHT)
        c.location += 2*RIGHT
        self.play(d.pointerStorage.shift,1*RIGHT+2.4*UP,d.keyStorage.shift,1*RIGHT+2.4*UP,d.key.shift,1*RIGHT+2.4*UP)
        d.location += 1*RIGHT+2.4*UP
        d.constructPointer(self,c)
        b.constructPointer(self,d)
        
        self.writeText(4*RIGHT,0.5,"if tail = node:",\
                                   "tail <- node2",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[0.3,0])
        self.wait(3)
        self.writeText(2.5*DOWN+4*RIGHT,0.5,"O(1)",color=GREEN,remove=False,scale=1)
        self.wait(1)
        AddAfterObject = VGroup()
        for mob in self.mobjects:
            AddAfterObject.add(mob)
        self.play(FadeOut(AddAfterObject))

        #start of add before
        self.writeText(4*UP,1,"AddBefore(node,key)",remove=False,color=WHITE,scale=1)
        
        a = Box(5)
        a.move(UP+5*LEFT)
        a.construct(self)
        self.createHeadPointer(a)
        b = Box(9,a)
        b.construct(self)
        a.constructPointer(self,b)
        c = Box(10,b)
        c.construct(self)
        c.endOfList(self)
        b.constructPointer(self,c)
        self.createTailPointer(c)
        self.writeText(2.5*DOWN+5*LEFT,0.5,"AddBefore(10,8)",remove=False,color=WHITE,scale=0.9)
        self.writeText(2*UP+4*RIGHT,0.5,"node2 <- new node",\
                                        "node2.key = key",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[0,0.3])
        
        d = Box(8)
        d.move(1.4*DOWN+2.8*LEFT)
        d.construct(self)
        
        self.wait(3)
        self.writeText(UP+4*RIGHT,0.5,"p = head",\
                                        "while p.next is not key:",\
                                        "p<-p.next",remove=False,color=YELLOW,scale=0.8,arbitaryPosition = [0,1.2,1.2],position=RIGHT)
        
        a.colorChange(self)
        b.colorChange(self)
        self.writeText(0.5*DOWN+4*RIGHT,0.5,"node2.next<-p.next",\
                                             "p.next<-node2",remove=False,color=YELLOW,scale=0.8,arbitaryPosition = [0.2,0])

        b.removeFrontPointer(self)
        self.play(c.pointerStorage.shift,1.8*RIGHT,c.keyStorage.shift,1.8*RIGHT,c.key.shift,1.8*RIGHT,c.line.shift,1.8*RIGHT,\
                  tailPointer.shift,1.8*RIGHT,tailPointerText.shift,1.8*RIGHT)
        c.location += 1.8*RIGHT
        self.play(d.pointerStorage.shift,1.7*RIGHT+2.4*UP,d.keyStorage.shift,1.7*RIGHT+2.4*UP,d.key.shift,1.7*RIGHT+2.4*UP)
        d.location += 1.7*RIGHT+2.4*UP
        d.constructPointer(self,c)
        b.constructPointer(self,d)
        self.wait(1)
        self.writeText(2.5*DOWN+4*RIGHT,0.5,"O(n)",color=RED,remove=False,scale=1)
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))

        a.location += 2*RIGHT
        b.location += 2*RIGHT
        c.location += RIGHT+0.8*LEFT
        d.location += 4.1*RIGHT

        #Intro of double linked list
        self.play(FadeIn(IntroObject))
        a.doubleLinkedList(self)
        a.startofList(self)
        b.doubleLinkedList(self,a) 
        c.doubleLinkedList(self,b)
        d.doubleLinkedList(self,c)
        text = TextMobject("(3) prev pointer")
        text.set_color(BLUE)
        text.move_to(3.5*DOWN)
        self.play(Write(text))
        self.wait()
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))

        #start of popback
        self.writeText(4*UP,1,"PopBack",remove=False,color=WHITE,scale=1)
        a = Box(5)
        a.move(UP+5*LEFT)
        a.construct(self)
        self.createHeadPointer(a)
        b = Box(9,a)
        b.construct(self)
        a.constructPointer(self,b)
        c = Box(10,b)
        c.construct(self)
        c.endOfList(self)
        b.constructPointer(self,c)
        self.createTailPointer(c)
        
        self.writeText(2.5*DOWN+4*LEFT,0.5,"PopBack()",remove=False,color=WHITE,scale=0.9)
        self.writeText(2*UP+4*RIGHT,0.5,"if head: -> empty list",\
                                        "if head = tail: -> head = tail = nil",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[1.3,0.3])
        self.wait(3)
        self.writeText(1*UP+4*RIGHT,0.5,"else","tail<-tail.prev","tail.next<-nil",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[1.3,0,0])
        self.play(tailPointer.shift,LEFT,tailPointerText.shift,LEFT)
        c.notEndAnymore(self)
        b.removeFrontPointer(self)
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))

        #start of add before
        self.writeText(4*UP,1,"AddBefore(node,key)",remove=False,color=WHITE,scale=1)
        
        a = Box(5)
        a.move(2*UP+5*LEFT)
        a.construct(self)
        self.createHeadPointer(a)
        a.doubleLinkedList(self)
        a.startofList(self)
        b = Box(9,a)
        b.construct(self)
        a.constructPointer(self,b)
        b.endOfList(self)
        b.doubleLinkedList(self,a)
        self.createTailPointer(b)
        
        self.writeText(2.5*DOWN+5*RIGHT,0.5,"AddBefore(5,8)",remove=False,color=WHITE,scale=0.9)
        
        d = Box(8)
        d.move(a.location+3.5*DOWN)
        d.construct(self)
        d.doubleLinkedList(self)
        self.wait(3)
        
        self.play(a.pointerStorage.shift,2*RIGHT,a.keyStorage.shift,2*RIGHT,a.key.shift,2*RIGHT,headPointer.shift,2*RIGHT,headPointerText.shift,2*RIGHT,\
                  a.prevPointerStorage.shift,2*RIGHT,a.prevLine.shift,2*RIGHT,a.next.shift,2*RIGHT,\
                  b.pointerStorage.shift,2*RIGHT,b.keyStorage.shift,2*RIGHT,b.key.shift,2*RIGHT,tailPointer.shift,2*RIGHT+DOWN,tailPointerText.shift,2*RIGHT+DOWN,\
                  b.prevPointerStorage.shift,2*RIGHT,b.line.shift,2*RIGHT,b.prev.shift,2*RIGHT\
                  )

        a.location += 2*RIGHT
        b.location += 2*RIGHT
        
        self.play(d.pointerStorage.shift,3.5*UP,d.keyStorage.shift,3.5*UP,d.key.shift,3.5*UP,\
                  d.prevPointerStorage.shift,3.5*UP,d.prev.shift,3.5*UP)
        
        d.location += 3.5*UP
        d.constructPointer(self,a)
        a.constructPrevPointer(self,d)
        self.writeText(4*RIGHT,0.5,"if head = node:",\
                                        "head = node2",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[0,0.5],position=RIGHT)
        self.play(headPointer.shift,2*LEFT,headPointerText.shift,2*LEFT)
        self.wait()
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))

        #start of popBack
        self.writeText(4*UP,1,"PopBack",remove=False,color=WHITE,scale=1)
        a = Box(5)
        a.move(UP+5*LEFT)
        a.construct(self)
        self.createHeadPointer(a)
        b = Box(9,a)
        b.construct(self)
        a.constructPointer(self,b)
        c = Box(10,b)
        c.construct(self)
        c.endOfList(self)
        b.constructPointer(self,c)
        self.createTailPointer(c)
        a.doubleLinkedList(self)
        a.startofList(self)
        b.doubleLinkedList(self,a)
        c.doubleLinkedList(self,b)
        self.play(tailPointer.shift,DOWN,tailPointerText.shift,DOWN)

        self.writeText(2.5*DOWN+4*LEFT,0.5,"PopBack()",remove=False,color=WHITE,scale=0.9)
        self.writeText(2*UP+4*RIGHT,0.5,"if head: -> empty list",\
                                        "if head = tail: -> head = tail = nil",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[1.3,0.3])
        self.wait(3)
        self.writeText(1*UP+2.5*RIGHT,0.5,"else","tail<-tail.prev","tail.next<-nil",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[1.3,0,0])
        self.play(tailPointer.shift,2*LEFT,tailPointerText.shift,2*LEFT)
        c.notEndAnymore(self)
        b.removeFrontPointer(self)
        c.removePrevPointer(self)
        b.endOfList(self)
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))

        #time complexity
        self.drawGraph()

    def createHeadPointer(self,node):
        global headPointer,headPointerText
        headPointer = Vector(node.location-(node.location+UP+LEFT))
        headPointer.move_to(node.location+UP+LEFT)
        headPointer.set_color(BLUE)
        headPointerText.move_to(headPointer)
        headPointerText.shift(UP+0.5*LEFT)
        self.play(FadeIn(headPointer),Write(headPointerText))

    def createTailPointer(self,node):
        global tailPointer
        tailPointer = Vector(node.location+DOWN-(node.location+2*DOWN+RIGHT))
        tailPointer.move_to(node.location+2*DOWN+RIGHT)
        tailPointer.set_color(BLUE)
        tailPointerText.move_to(tailPointer)
        tailPointerText.shift(DOWN+0.5*RIGHT)
        self.play(FadeIn(tailPointer),Write(tailPointerText))

    def drawGraph(self):
        increase_by= 0.4
        title = TextMobject("Single Linked List ")
        title.to_edge(DOWN)
        title.shift(LEFT)
        title.set_color(YELLOW)
        title.scale=1
        self.play(Write(title))
        self.writeText(3*UP+3.5*LEFT,0.3,"PushFront(key)","TopFront()","PopFront()",\
                  "PushBack(key)","TopBack()","PopBack()",\
                  "Find(key)","Erase(key)","Empty()",\
                  "AddBefore(node,key)","AddAfter(node,key)",remove=False,color=BLUE,scale=0.8,increase=increase_by)

        self.wait()
        subtitle = TextMobject("no tail")
        subtitle.move_to(3.5*UP+RIGHT)
        subtitle.shift(LEFT)
        subtitle.set_color(BLUE)
        subtitle.scale=1
        self.play(Write(subtitle))
        self.writeText(3*UP,0.3,"O(1)","O(1)","O(1)","O(n)","O(n)","O(n)","O(n)","O(n)","O(1)","O(n)","O(1)",\
                       remove=True,color=YELLOW,scale=0.8,delay=3,increase=increase_by)
        
        self.play(FadeOut(subtitle))
        subtitle = TextMobject("with tail")
        subtitle.move_to(3.5*UP+RIGHT)
        subtitle.shift(LEFT)
        subtitle.set_color(BLUE)
        subtitle.scale=1
        self.play(Write(subtitle))
        self.writeText(3*UP,0.3,"O(1)","O(1)","O(1)","O(1)","O(1)","O(n)","O(n)","O(n)","O(1)","O(n)","O(1)",\
                       remove=True,color=YELLOW,scale=0.8,delay=3,increase=increase_by)
        
        self.play(FadeOut(title))
        title = TextMobject("Double Linked List ")
        title.to_edge(DOWN)
        title.shift(LEFT)
        title.set_color(YELLOW)
        title.scale=1
        self.play(Write(title))
        self.writeText(3*UP,0.3,"O(1)","O(1)","O(1)","O(1)","O(1)","O(1)","O(n)","O(n)","O(1)","O(1)","O(1)",\
                       remove=True,color=YELLOW,scale=0.8,delay=3,increase=increase_by)
        object = VGroup()
        
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))


