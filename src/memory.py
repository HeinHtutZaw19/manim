from manimlib.imports import *
import numpy as np

class memoryDiagram(MovingCameraScene):

    def construct(self):
        self.introText()

    def introText(self):
        text = TextMobject("Let's talk about memory").set_color(YELLOW)
        self.play(Write(text))
        self.wait()
        self.TransformText(text,"So what exactly is memory?",1,3,YELLOW)
        self.TransformText(text,"Memory",1,1,BLUE)
        self.play(text.to_edge,UP)
        self.wait()

        Harddrive = Rectangle(width=2,height=2).set_color(PINK).to_edge(LEFT).shift(0.5*RIGHT).set_fill(PINK,opacity=0.5)
        hdd_text = TextMobject("HDD").move_to(Harddrive)
        Ram = Rectangle(width=2,height=4).set_color(ORANGE).shift(2*LEFT).set_fill(ORANGE,opacity=0.5)
        ram_text = TextMobject("RAM").move_to(Ram)
        RamObject = VGroup()
        RamObject.add(Ram,ram_text)
        hdd_to_ram,ram_to_hdd = self.CreateArrows(Harddrive,RIGHT)
        Cache = Rectangle(width=1.5,height=1.5).set_color(BLUE).shift(0.8*RIGHT+UP).set_fill(BLUE,opacity=0.5)
        cache_text = TextMobject("Cache").move_to(Cache).scale(0.8)
        cache_to_cpu,cpu_to_cache = self.CreateArrows(Cache,RIGHT)
        ram_to_cache,cache_to_ram = self.CreateArrows(Cache,LEFT)
        Cpu = Rectangle(width=2,height=4).set_color(YELLOW).shift(1.5*RIGHT).set_fill(YELLOW,opacity=0.5)
        cpu_text = TextMobject("CPU").move_to(Cpu)
        cpu_to_ram,ram_to_cpu = self.CreateArrows(Ram,1.5*RIGHT)
        object = VGroup()
        object.add(Harddrive,Ram,hdd_to_ram,ram_to_hdd,ram_text,hdd_text)
        CpuObject = VGroup()
        CpuObject.add(cpu_to_ram,ram_to_cpu,Cpu,cpu_text)
        
        self.play(GrowFromCenter(object),GrowFromCenter(CpuObject))
        self.wait(5)
        cpu_to_ram1,ram_to_cpu1 = self.CreateArrows(Ram,2.5*RIGHT,opt=True)
        cpu_to_ram1.shift(1.5*DOWN)
        ram_to_cpu1.shift(1.5*DOWN)
        self.play(CpuObject.shift,2*RIGHT,Transform(cpu_to_ram,cpu_to_ram1),Transform(ram_to_cpu,ram_to_cpu1))
        self.wait()
        cacheObject = VGroup()
        cacheObject.add(Cache,cache_text,cache_to_cpu,cpu_to_cache,ram_to_cache,cache_to_ram)
        self.play(FadeIn(cacheObject))
        self.wait(5)
        self.camera_frame.save_state()
        self.play(
            self.camera_frame.set_height,RamObject.get_width()*1.2,
            self.camera_frame.move_to,RamObject
        )
        self.wait()
        stack = Rectangle(width=0.5,height=0.5).set_color(YELLOW).set_fill(YELLOW,opacity=0.5).move_to(Ram).shift(0.8*UP)
        heap = Rectangle(width=0.5,height=0.5).set_color(BLUE).set_fill(BLUE,opacity=0.5).move_to(Ram).shift(0.8*DOWN)
        stack_text = TextMobject("stack").scale(0.3).move_to(stack)
        heap_text = TextMobject("heap").scale(0.3).move_to(heap)
        extraObjects = VGroup()
        extraObjects.add(stack,heap,stack_text,heap_text)
        self.play(DrawBorderThenFill(extraObjects,rate_func=linear))
        self.wait(8)        
        self.play(Restore(self.camera_frame))
        self.wait()
        cache_hit_text = TextMobject("cache hit").set_color(RED).scale(0.6).next_to(Cache,0.6*UP)
        cache_miss_text = TextMobject("cache miss").set_color(RED).scale(0.6).next_to(ram_to_cpu,0.5*DOWN)
        
        self.play(FadeIn(cache_hit_text))
        self.wait(3)
        self.play(FadeIn(cache_miss_text))
        self.wait(4)

        

    def TransformText(self,text1,text2,runtime,delay,color):
        arbitaryText = TextMobject(str(text2)).set_color(color)
        self.play(Transform(text1,arbitaryText))
        self.wait(delay)

    def CreateArrows(self,object,position,opt=False):
        if(opt):
            arrow1 = Arrow(3*LEFT,0.1*RIGHT).set_color(GREEN).next_to(object,position)
            arrow2 = Arrow(3*RIGHT,0.1*LEFT).set_color(GREEN).next_to(object,position)
            return arrow1,arrow2
        arrow1 = Arrow(LEFT,0.1*RIGHT).set_color(GREEN).next_to(object,position)
        arrow2 = Arrow(RIGHT,0.1*LEFT).set_color(GREEN).next_to(object,position)
        return arrow1,arrow2

class Intro(MovingCameraScene):
    def construct(self):
        text = TextMobject("HI!").set_color(YELLOW).scale(1.5)
        self.play(Write(text))
        self.wait()
        self.TransformText(text,"MEMORY",1,1,YELLOW,scale=1.5)
        self.wait(5)
        self.play(FadeOut(text))
        text = TextMobject("1. Memory").set_color(RED)
        text2 = TextMobject("2. Stack and Heap memory").shift(DOWN).set_color(RED).align_to(text,LEFT)
        text3 = TextMobject("3. Garbage Collector").shift(2*DOWN).set_color(RED).align_to(text,LEFT)
        object = VGroup(text,text2,text3).move_to(0)
        self.play(GrowFromCenter(object))
        self.wait(8) 
        Group = VGroup()
        for objects in self.mobjects:
            Group.add(objects)
        self.play(FadeOut(Group))

        memory = Rectangle(width = 10,height = 1)
        self.play(GrowFromCenter(memory))
        memoryObject = VGroup()
        
        coe = 1
        for i in range(4):
            line = Line().scale(0.5).move_to(4*LEFT).shift(coe*RIGHT).rotate(PI/2)
            self.play(Write(line))
            coe += 2
            memoryObject.add(line)

        address = 0
        addressObject = VGroup()
        dataObject = VGroup()
        addressTextList = []
        addressString=np.array(["1","0.5","3.1419","'a'","1"])
        typeString = ["int","float","double","char","bool"]
        color = [RED,GREEN,PURPLE,YELLOW,BLUE]
        for i in range(5):
            string = "0x000" + str(address)
            addressText = TextMobject(string).move_to(4*LEFT).shift(address*2*RIGHT).set_color(BLUE)
            addressText2 = TextMobject(addressString[i]).move_to(addressText).set_color(color[i])
            typeText = TextMobject(typeString[i]).set_color(color[i]).move_to(addressText2).shift(UP)
            addressTextList.append(addressText)
            addressObject.add(addressText)
            dataObject.add(addressText2,typeText)
            address += 1
        self.play(Write(addressObject))
        self.wait(5)
        self.play(Transform(addressObject,dataObject))
        memoryObject.add(memory,dataObject)
        self.wait(5)

        self.camera_frame.save_state()
        intBytes = VGroup()
        floatBytes = VGroup()
        for i in range(2):
            circle = Circle(radius = addressTextList[0].get_width()/2).set_color(RED).set_fill(RED,opacity=0.5).move_to(addressTextList[0]).shift(i*0.5*RIGHT+0.25*LEFT+0.25*UP)
            circle1 = Circle(radius = addressTextList[0].get_width()/2).set_color(RED).set_fill(RED,opacity=0.5).move_to(addressTextList[0]).shift(i*0.5*RIGHT+0.25*LEFT+0.25*DOWN)
            intBytes.add(circle,circle1)
            circle = Circle(radius = addressTextList[0].get_width()/2).set_color(GREEN).set_fill(GREEN,opacity=0.5).move_to(addressTextList[1]).shift(i*0.5*RIGHT+0.25*LEFT+0.25*UP)
            circle1 = Circle(radius = addressTextList[0].get_width()/2).set_color(GREEN).set_fill(GREEN,opacity=0.5).move_to(addressTextList[1]).shift(i*0.5*RIGHT+0.25*LEFT+0.25*DOWN)
            floatBytes.add(circle,circle1)
            
        doubleBytes = VGroup()
        for i in range(4):
            circle = Circle(radius = addressTextList[0].get_width()/2).set_color(PURPLE).set_fill(PURPLE,opacity=0.5).move_to(addressTextList[2]).shift(i*0.3*RIGHT+0.5*LEFT+0.25*UP)
            circle1 = Circle(radius = addressTextList[0].get_width()/2).set_color(PURPLE).set_fill(PURPLE,opacity=0.5).move_to(addressTextList[2]).shift(i*0.3*RIGHT+0.5*LEFT+0.25*DOWN)
            doubleBytes.add(circle,circle1)

        charCircle = Circle(radius = addressTextList[0].get_width()/2).set_color(YELLOW).set_fill(YELLOW,opacity=0.5).move_to(addressTextList[3])
        boolCircle = Circle(radius = addressTextList[0].get_width()/2).set_color(BLUE).set_fill(BLUE,opacity=0.5).move_to(addressTextList[4])
        
        self.play(Transform(addressTextList[0],intBytes),Transform(addressTextList[1],floatBytes),\
                  Transform(addressTextList[2],doubleBytes),Transform(addressTextList[3],charCircle),\
                  Transform(addressTextList[4],boolCircle))
        
        self.wait()
        self.play(Restore(self.camera_frame))
        self.wait(5)
        bitObject = VGroup()
        place = 4*LEFT
        for i in range(8):
            bitObject.add(Circle().scale(0.3).move_to(place).set_color(BLUE).set_fill(BLUE,opacity=0.5))
            place+=RIGHT
        bitObject.move_to(0)
        
        bits_text = TextMobject("One bit is equal to 8 bytes").set_color(RED).scale(0.8).shift(DOWN)
        self.play(Transform(text,bitObject),Write(bits_text))
        self.wait(5)

        


    def TransformText(self,text1,text2,runtime,delay,color,scale=1):
        arbitaryText = TextMobject(str(text2)).set_color(color).scale(scale)
        self.play(Transform(text1,arbitaryText))
        self.wait(delay)