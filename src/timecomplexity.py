from manimlib.imports import *
import numpy as np
from numpy import random

def Range(in_val, end_val, step=1):
    return list(np.arange(in_val, end_val+step, step))


class TimeComplexityGraph(GraphScene, MovingCameraScene):
    CONFIG = {
        "y_max": 1000,
        "y_min": 0,
        "x_max": 100,
        "x_min": 0,
        "y_tick_frequency": 100,
        "x_tick_frequency": 10,
        "graph_origin": [-4, -3, 0],
        "y_axis_label": None,  # Don't write y axis label
        "x_axis_label": None,
    }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        text = TextMobject("Common Time Complexity Graph")
        self.play(Write(text))
        self.wait()
        self.play(FadeOut(text))
        self.wait()
        self.timecomplexityGraph()
        

    def timecomplexityGraph(self):
        self.setup_axes() 
        #self.camera_frame.set_height(500)
        two_n = self.get_graph(lambda x: 2 ** x,
                                 color=RED,
                                 x_min=0,
                                 x_max=10,
                                 )
        two_n_line = Line().scale(0.5)
        two_n_line.set_color(RED)
        two_n_line.rotate(TAU/2)

        log_n = self.get_graph(lambda x: np.log(x),
                                 color=GREEN,
                                 x_min=0.1,
                                 x_max=100,
                                 )
        log_n_line = Line().scale(0.5)
        log_n_line.set_color(GREEN)
        log_n_line.rotate(TAU/2)

        n_log_n = self.get_graph(lambda x: x*np.log(x),
                               color=BLUE,
                               x_min=0.001,  ## Don't change to zero. It is not defined.
                               x_max=100,
                               )
        n_log_n_line = Line().scale(0.5)
        n_log_n_line.set_color(BLUE)
        n_log_n_line.rotate(TAU/2)

        n_square = self.get_graph(lambda x: x ** 2,
                                 color=ORANGE,
                                 x_min=0,
                                 x_max=33,
                                 )
        n_square_line = Line().scale(0.5)
        n_square_line.set_color(ORANGE)
        n_square_line.rotate(TAU/2)

        n = self.get_graph(lambda x: x,
                                  color=WHITE,
                                  x_min=0,
                                  x_max=100,
                                  )
        n_line = Line().scale(0.5)
        n_line.set_color(WHITE)
        n_line.rotate(TAU/2)

        one = self.get_graph(lambda x: 1,
                                  color=PURPLE,
                                  x_min=0,
                                  x_max=100,
                                  )
        one_line = Line().scale(0.5)
        one_line.set_color(PURPLE)
        one_line.rotate(TAU/2)

        n.set_stroke(width=3)
        log_n.set_stroke(width=3)
        n_square.set_stroke(width=3)
        n_log_n.set_stroke(width=3)
        two_n.set_stroke(width=3)
        one.set_stroke(width=3)

        self.play(Write(two_n),Write(n), Write(log_n), Write(n_log_n), Write(n_square),  Write(one))
        place = 3*RIGHT+3.5*UP
        line_array = [two_n_line,n_square_line,n_log_n_line,n_line,log_n_line,one_line]
        text_array = [TextMobject("$O(2^n)$"),TextMobject("$O(n^2)$"),TextMobject("O(nlogn)"),TextMobject("O(n)"),TextMobject("O(logn)"),TextMobject("O(1)")]
        color_array = [RED,ORANGE,BLUE,WHITE,GREEN,PURPLE]

        
        
        for i in range(6):
            line_array[i].move_to(place)
            text_array[i].set_color(color_array[i])
            text_array[i].move_to(place+1.5*RIGHT)
            text_array[i].scale(0.8)
            place+=0.5*DOWN
            self.play(Write(line_array[i]),Write(text_array[i]))
            
        self.wait()
        arrow = Vector(2.5*DOWN-0.1*UP).set_color(GREEN).shift(3.5*UP+2*RIGHT)
        self.play(Write(arrow))
        self.wait()
        text = TextMobject("more efficient").set_color(GREEN).shift(2*UP+0.7*RIGHT).scale(0.8)
        self.play(Write(text))
        
        self.wait(10)
        IntroObject = VGroup()
        for mob in self.mobjects:
            IntroObject.add(mob)
        self.play(FadeOut(IntroObject))
        self.wait()
        

    def setup_axes(self):
        GraphScene.setup_axes(self)
        # width of edges
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        # color of edges
        self.x_axis.set_color(YELLOW)
        self.y_axis.set_color(YELLOW)

        self.play(
            *[Write(objeto) 
              for objeto in [
                  self.y_axis,
                  self.x_axis
              ]
              ],
            run_time=2
        )

ReplaceObject = VGroup()
class CompareComplexity(GraphScene, MovingCameraScene):
    CONFIG = {
        "y_max": 1000,
        "y_min": 0,
        "x_max": 32,
        "x_min": 0,
        "y_tick_frequency": 100,
        "x_tick_frequency": 5,
        "graph_origin": [-4, -7, 0],
        "y_axis_label": None,  # Don't write y axis label
        "x_axis_label": None,
    }

    def writeText(self,place,time,*string,remove,color,scale,arbitaryPosition=None,position=LEFT,delay=0.1,increase=0):
        global ReplaceObject
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
        ReplaceObject.add(object)

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.timecomplexityGraph()
        
    def timecomplexityGraph(self):
        global ReplaceObject
        self.camera_frame.set_height(15)
        text = TextMobject("Big O Notation").scale(1.5).set_color(BLUE).shift(6*UP)
        self.play(Write(text))
        self.writeText(5*UP,0.5,"f=O(g(n)) if there exist constants N and c so that",\
                       "for all n>=N, f(n)<=c.g(n)",remove=False,color=WHITE,scale=1.3,increase=0.5)
        self.wait(10)
        text1 =TextMobject("$f(n) = 3n^2+4n+1$").scale(1.3).set_color(GREEN).shift(UP+6*LEFT)
        self.play(Write(text1))
        replaceText = TextMobject("$g(n) = n^2$").scale(1.3).set_color(RED).shift(UP+6*RIGHT)
        self.play(Write(replaceText))
        
        self.wait(3)

        self.setup_axes() 
        fOfN= self.get_graph(lambda x: 3*x*x+4*x+1,
                                 color=GREEN,
                                 x_min=0,
                                 x_max=18,
                                 )
        fOfNtext = TextMobject("f(n)").set_color(GREEN).shift(RIGHT).scale(1.2)
        gOfN = self.get_graph(lambda x: x*x,
                                  color=RED,
                                  x_min=0,
                                  x_max=31.6,
                                  )
        gOfNtext = TextMobject("g(n)").set_color(RED).shift(6*RIGHT+2*DOWN).scale(1.2)
         
        cOfgOfN = self.get_graph(lambda x: 4*x*x,
                                  color=RED,
                                  x_min=0,
                                  x_max=16,
                                  )
        cOfgOfNtext = TextMobject("c.g(n)").set_color(RED).shift(LEFT).scale(1.2)
        
        self.play(Write(fOfN),Write(fOfNtext))
        self.play(Write(gOfN),Write(gOfNtext))
        self.wait(8)
        self.play(Transform(gOfN,cOfgOfN),Transform(gOfNtext,cOfgOfNtext))
        self.wait(3)

        newText = TextMobject("since f(n)<=c.g(n),  f(n)=O(g(n))").set_color(GREEN).shift(UP).scale(1.2)
        newText2 = TextMobject("$O(n^2)$").set_color(GREEN).shift(UP).scale(1.2)
        self.play(FadeOut(replaceText),Transform(text1,newText))
        self.wait(3)
        self.play(Transform(text1,newText2))
        self.wait()
        newText2 =TextMobject("$f(n) = 3n^2+4n+1$").scale(1.3).set_color(GREEN).shift(UP+6*LEFT)

        self.play(Transform(text1,newText2))
        self.play(Write(replaceText))
        self.wait()
        ReplaceObject.add(text,text1)
        text2 = TextMobject("f grows no faster than g(n)").shift(2.5*UP).scale(1.3).set_color(BLUE)
        self.play(Write(text2))
        self.wait(4)

        gOfNagain = self.get_graph(lambda x: x*x,
                                  color=RED,
                                  x_min=0,
                                  x_max=31.6,
                                  )
        gOfNtextagain = TextMobject("g(n)").set_color(RED).shift(6*RIGHT+2*DOWN).scale(1.2)
         
        self.play(Transform(gOfN,gOfNagain),Transform(gOfNtext,gOfNtextagain))
        

        #text3 = TextMobject("Worst case").shift(2*UP).scale(1.2).set_color(YELLOW)
        #self.play(Write(text3))
        self.wait(8)
        self.play(FadeOut(gOfN),FadeOut(gOfNtext))
        self.play(Transform(replaceText,TextMobject("g(n) = n").scale(1.3).set_color(RED).shift(UP+6*RIGHT)))
        self.wait(3)
        gOfN = self.get_graph(lambda x: x,
                                  color=RED,
                                  x_min=0,
                                  x_max=32,
                                  )
        gOfNtext = TextMobject("g(n)").set_color(RED).shift(6*RIGHT+6*DOWN).scale(1.2)
        self.play(Write(gOfN),Write(gOfNtext))
        
        self.wait(3)

        cOfgOfN1 = self.get_graph(lambda x: 10*x,
                                  color=RED,
                                  x_min=0,
                                  x_max=32,
                                  )
        cOfgOfNtext1 = TextMobject("c.g(n)").set_color(RED).shift(6*RIGHT+5*DOWN).scale(1.2)
        self.play(Transform(gOfN,cOfgOfN1),Transform(gOfNtext,cOfgOfNtext1))
        self.wait(3) 

        cOfgOfN2 = self.get_graph(lambda x: 100*x,
                                  color=RED,
                                  x_min=0,
                                  x_max=10,
                                  )
        self.play(Transform(gOfN,cOfgOfN2),gOfNtext.move_to,2*LEFT)
        self.wait(15)
        ReplaceObject.add(gOfNtext,replaceText,fOfNtext,text2)
        self.play(FadeOut(ReplaceObject))

        cOfgOfN = self.get_graph(lambda x: 100*x,
                                  color=RED,
                                  x_min=0,
                                  x_max=80,
                                  )
        NewfOfN = self.get_graph(lambda x: 3*x*x+4*x+1,
                                  color=GREEN,
                                  x_min=0,
                                  x_max=50,
                                  )

        self.play(Transform(gOfN,cOfgOfN),Transform(fOfN,NewfOfN))
        self.wait()
        self.play(self.camera_frame.set_height,100)
        self.wait(10)
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))
        


    def setup_axes(self):
        GraphScene.setup_axes(self)
        # width of edges
        self.x_axis.set_stroke(width=2) 
        self.y_axis.set_stroke(width=2)
        # color of edges
        self.x_axis.set_color(YELLOW)
        self.y_axis.set_color(YELLOW)

        self.play(
            *[Write(objeto) 
              for objeto in [
                  self.y_axis,
                  self.x_axis
              ]
              ],
            run_time=2
        )

ReplaceObject = VGroup()
class CompareComplexity2(GraphScene, MovingCameraScene):
    CONFIG = {
        "y_max": 1000,
        "y_min": 0,
        "x_max": 32,
        "x_min": 0,
        "y_tick_frequency": 100,
        "x_tick_frequency": 5,
        "graph_origin": [-4, -7, 0],
        "y_axis_label": None,  # Don't write y axis label
        "x_axis_label": None,
    }

    def writeText(self,place,time,*string,remove,color,scale,arbitaryPosition=None,position=LEFT,delay=0.1,increase=0):
        global ReplaceObject
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
        ReplaceObject.add(object)

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.timecomplexityGraph()
        
    def timecomplexityGraph(self):
        global ReplaceObject
        self.camera_frame.set_height(15)
        text = TextMobject("Big").scale(1.5).set_color(BLUE).shift(6*UP+1.5*LEFT)
        text2 = TextMobject("Notation").scale(1.5).set_color(BLUE).shift(6*UP+2*RIGHT)
        text3 = TextMobject("$\Omega$").scale(1.5).set_color(BLUE).shift(6*UP)
        self.play(Write(text),Write(text3),Write(text2))
        self.writeText(5*UP,0.5,"if there exist constants N and c so that",\
                       "for all n>=N, f(n)>=c.g(n)",remove=False,color=WHITE,scale=1.3,increase=0.5)
        self.wait(3)
        text1 =TextMobject("$f(n) = 3n^2+4n+1$").scale(1.3).set_color(GREEN).shift(UP+6*LEFT)
        self.play(Write(text1))   
        replaceText = TextMobject("g(n) = n").scale(1.3).set_color(RED).shift(UP+6*RIGHT)
        self.play(Write(replaceText))

        self.setup_axes() 
        fOfN= self.get_graph(lambda x: 3*x*x+4*x+1,
                                 color=GREEN,
                                 x_min=0,
                                 x_max=18,
                                 )
        fOfNtext = TextMobject("f(n)").set_color(GREEN).shift(RIGHT).scale(1.2)
        gOfN = self.get_graph(lambda x: x,
                                  color=RED,
                                  x_min=0,
                                  x_max=31.6,
                                  )
        gOfNtext = TextMobject("g(n)").set_color(RED).shift(6*RIGHT+6*DOWN).scale(1.2)
         
        cOfgOfN = self.get_graph(lambda x: 50*x,
                                  color=RED,
                                  x_min=0,
                                  x_max=23,
                                  )
        cOfgOfNtext = TextMobject("c.g(n)").set_color(RED).shift(3*RIGHT).scale(1.2)
        
        self.play(Write(fOfN),Write(gOfN),Write(fOfNtext),Write(gOfNtext))
        self.play(Transform(gOfN,cOfgOfN),Transform(gOfNtext,cOfgOfNtext))
        newText = TextMobject("since f(n)>=c.g(n),  f(n)=$\Omega(g(n))$").set_color(GREEN).shift(UP).scale(1.2)
        newText2 = TextMobject("$\Omega(n)$").set_color(GREEN).shift(UP).scale(1.2)
        self.play(FadeOut(replaceText),Transform(text1,newText))
        self.wait(3)
        self.play(Transform(text1,newText2))
        self.wait()
        newText2 =TextMobject("$f(n) = 3n^2+4n+1$").scale(1.3).set_color(GREEN).shift(UP+6*LEFT)

        self.play(Transform(text1,newText2))
        self.play(Write(replaceText)) 
        self.wait()
        ReplaceObject.add(text3,text1)
        text2 = TextMobject("f grows no faster than c.g(n)").shift(2.5*UP).scale(1.3).set_color(BLUE)
        self.play(Write(text2))
        self.wait()
        text3 = TextMobject("Best case").shift(2*UP).scale(1.2).set_color(YELLOW)
        self.play(Write(text3))
        self.wait(5)
        ReplaceObject.add(text3,text2,replaceText,fOfN,gOfN,fOfNtext,gOfNtext)
        self.play(FadeOut(ReplaceObject))
        self.wait()

        text3 = TextMobject("$\Theta$").scale(1.5).set_color(BLUE).shift(6*UP)
        self.play(Write(text3))
        
        self.writeText(5*UP,0.5,"if f(n) is O(g(n)) and also $\Omega(g(n))$",\
                       "for all n>=N, f(n)<=c1.g(n) , c2.g(n)>=f(n)",remove=False,color=WHITE,scale=1.3,increase=0.5)
        self.wait(5)
        text1 =TextMobject("$f(n) = 3n^2+4n+1$").scale(1.3).set_color(GREEN).shift(UP+6*LEFT)
        self.play(Write(text1))
        replaceText = TextMobject("$g(n) = n^2$").scale(1.3).set_color(RED).shift(UP+6*RIGHT)
        self.play(Write(replaceText))
        self.wait(3)

        self.setup_axes() 
        fOfN= self.get_graph(lambda x: 3*x*x+4*x+1,
                                 color=GREEN,
                                 x_min=0,
                                 x_max=18,
                                 )
        fOfNtext = TextMobject("f(n)").set_color(GREEN).shift(RIGHT).scale(1.2)
        gOfN = self.get_graph(lambda x: x**2,
                                  color=RED,
                                  x_min=0,
                                  x_max=31.6,
                                  )
        gOfNtext = TextMobject("g(n)").set_color(RED).shift(6*RIGHT+2*DOWN).scale(1.2)
         
        cOfgOfN = self.get_graph(lambda x: 1.5*x**2,
                                  color=RED,
                                  x_min=0,
                                  x_max=25,
                                  )
        cOfgOfNtext = TextMobject("c1.g(n)").set_color(RED).shift(2*DOWN+4*RIGHT).scale(1.2)
        
        cOfgOfN1 = self.get_graph(lambda x: 10*x**2,
                                  color=RED,
                                  x_min=0,
                                  x_max=10,
                                  )
        cOfgOfNtext1 = TextMobject("c2.g(n)").set_color(RED).shift(0.5*DOWN+2*LEFT).scale(1.2)
        
        self.play(Write(fOfN),Write(gOfN),Write(fOfNtext),Write(gOfNtext))
        self.wait(3)
        self.play(Transform(gOfN,cOfgOfN),Transform(gOfNtext,cOfgOfNtext),Write(cOfgOfN1),Write(cOfgOfNtext1))
        self.wait(3)
        newText = TextMobject("since f(n)>=c1.g(n) and f(n)<=c2.g(n) ,  f(n)=$\Theta(g(n))$").set_color(GREEN).shift(UP).scale(1.2)
        newText2 = TextMobject("$\Theta(n^2)$").set_color(GREEN).shift(UP).scale(1.2)
        self.play(FadeOut(replaceText),Transform(text1,newText))
        self.wait(3)
        self.play(Transform(text1,newText2))
        self.wait()
        newText2 =TextMobject("$f(n) = 3n^2+4n+1$").scale(1.3).set_color(GREEN).shift(UP+6*LEFT)

        self.play(Transform(text1,newText2))
        self.play(Write(replaceText))
        self.wait()
        ReplaceObject.add(text,text1)
        text2 = TextMobject("f grows approximately the same rate as g").shift(2.5*UP).scale(1.3).set_color(BLUE)
        self.play(Write(text2))
        self.wait()
        text3 = TextMobject("Average case").shift(2*UP).scale(1.2).set_color(YELLOW)
        self.play(Write(text3))
        self.wait(5)
        
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))
        self.wait()


    def setup_axes(self):
        GraphScene.setup_axes(self)
        # width of edges
        self.x_axis.set_stroke(width=2) 
        self.y_axis.set_stroke(width=2)
        # color of edges
        self.x_axis.set_color(YELLOW)
        self.y_axis.set_color(YELLOW)

        self.play(
            *[Write(objeto) 
              for objeto in [
                  self.y_axis,
                  self.x_axis
              ]
              ],
            run_time=2
        )

        
AllObject = VGroup()
AllObject2 = VGroup()
AllObject3 = VGroup()

class AlgorithmComparison(GraphScene, MovingCameraScene):
    CONFIG = {
        "y_max": 2000,
        "y_min": 0,
        "x_max": 7,
        "x_min": 0,
        "y_tick_frequency": 200,
        "x_tick_frequency": 1,
        "graph_origin": [-4, -3, 0],
        "y_axis_label": None,  # Don't write y axis label
        "x_axis_label": None,
    }
    def writeText(self,place,time,*string,remove,color,scale,arbitaryPosition=None,position=LEFT,delay=0.1,increase=0,opt=0):
        global ReplaceObject
        global AllObject,AllObject2,AllObject3
        Place = place
        object = VGroup()
        a=0
        for i in string:
            if arbitaryPosition is not None:
                try:
                    Place = Place+scale/2*DOWN+increase*DOWN+arbitaryPosition[a]*position-arbitaryPosition[a-1]*position
                except IndexError:
                    Place = Place+scale/2*DOWN+increase*DOWN+arbitaryPosition[a]*position
            else:
                if(str(Place)==str(place)):
                    Place = Place+scale/2*DOWN
                else:
                    Place = Place+scale/2*DOWN+increase*DOWN
            text = TextMobject(i)
            text.scale(scale)
            text.set_color(color)
            text.move_to(Place)
            object.add(text)
            self.play(Write(text),run_time=time)
            a += 1
        
        
        if(remove is True):
            ReplaceObject.add(object)

        if(opt==1):
            AllObject.add(object)
        elif(opt==2):
            AllObject2.add(object)
        elif(opt==3):
            AllObject3.add(object)
        else:
            print("Bad")

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.timecomplexityGraph()
        
    def timecomplexityGraph(self):
        global ReplaceObject
        global AllObject,AllObject2,AllObject3
        titleText = TextMobject("Which algorithm is more efficient?")
        self.play(Write(titleText))
        self.wait(2)
        self.play(FadeOut(titleText))
        nyimalayText = TextMobject("nyimalay").set_color(RED).move_to(5*LEFT+2.5*UP).scale(0.8)
        self.play(Write(nyimalayText),run_time=0.3)
        line = Line().scale(1.8).rotate(TAU/4).move_to(5*LEFT+0.3*UP)
        line2 = Line().move_to(5*LEFT+1.38*UP).scale(1.4)

        self.writeText(6*LEFT+2*UP,0.2,"n","100","1000","10000","100000","1000000",remove=True,color=RED,scale=0.8,increase=0.2)
        self.writeText(4*LEFT+2*UP,0.2,"Time(s)","0.1","3","58","597","2052",remove=False,color=RED,scale=0.8,opt=1,increase=0.2)
        self.play(Write(line),Write(line2))
        
        mamaText = TextMobject("mama").set_color(GREEN).move_to(5*RIGHT+2.5*UP).scale(0.8)
        self.play(Write(mamaText),run_time=0.3)
        line1 = Line().scale(1.8).rotate(TAU/4).move_to(5*RIGHT+0.3*UP)
        line12 = Line().move_to(5*RIGHT+1.38*UP).scale(1.4)

        self.writeText(4*RIGHT+2*UP,0.2,"n","100","1000","10000","100000","1000000",remove=True,color=GREEN,scale=0.8,increase=0.2)
        self.writeText(6*RIGHT+2*UP,0.2,"Time(s)","0.01","0.9","15","247","900",remove=False,color=GREEN,scale=0.8,opt=1,increase=0.2)
        self.play(Write(line1),Write(line12))
        self.play(FadeOut(ReplaceObject))
        self.wait(4)
        self.writeText(6*LEFT+2*UP,0.2,"log(n)","2","3","4","5","6",remove=False,color=RED,scale=0.8,increase=0.2,opt=2)
        self.writeText(4*RIGHT+2*UP,0.2,"log(n)","2","3","4","5","6",remove=False,color=GREEN,scale=0.8,increase=0.2,opt=2)
        self.wait()
        
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(object.scale,1.3,object.shift,UP,self.camera_frame.set_height,10)
        
        self.wait(3)
        self.setup_axes()
        nyimalay = self.get_graph(lambda x: 72 * x ** 3 - 622 * x ** 2 + 1745 * x - 1578,
                                  color=RED,
                                  x_min=2,
                                  x_max=6,
                                  )
        
        mama = self.get_graph(lambda x: (409 / 12) * x ** 3 - (1201 / 4) * x ** 2 + (2564 / 3) * x - 781,
                                  color=GREEN,
                                  x_min=2,
                                  x_max=6,
                                  )



        self.play(Write(nyimalay),Write(mama))
        self.wait(10)
        self.play(FadeOut(AllObject))
        self.wait(3)
        self.writeText(5.2*LEFT+3.3*UP,0.3,"Time(s)","0.05","2","49","500","1800",remove=False,color=RED,scale=0.9,increase=0.33,opt=2)
        self.writeText(7.5*RIGHT+3.3*UP,0.3,"Time(s)","0.03","2","35","410","1100",remove=False,color=GREEN,scale=0.9,increase=0.33,opt=2)
        self.wait()
        nyimalay2 = self.get_graph(lambda x: 761 / 12 * x ** 3 - 2193 / 4 * x ** 2 + 4615 / 3 * x - 1391,
                                  color=RED,
                                  x_min=2,
                                  x_max=6,
                                  )
        
        mama2 = self.get_graph(lambda x: (151 / 4) * x ** 3 - (1297 / 4) * x ** 2 + 906 * x - 817,
                                  color=GREEN,
                                  x_min=2,
                                  x_max=6,
                                  )
        self.play(Transform(nyimalay,nyimalay2),Transform(mama,mama2),run_time=0.3)
        self.wait(10)

        self.writeText(5*LEFT+2*DOWN,0.3,"for a in n+1:",\
                       "for b in n+1:",\
                       "for c in n+1:",\
                       "if (a+b+c = n):",\
                       " assign a,b,c",remove=False,opt=3,color=YELLOW,scale=0.9,arbitaryPosition=[0.1,0.5,1,2,2.5],position=RIGHT)
        
        self.writeText(7*RIGHT+2*DOWN,0.5,"for a in n+1:",\
                       "for b in n+1:",\
                       "c = n-(a+b)",\
                       "if (c>=0):",\
                       " assign a,b,c",remove=False,opt=3,color=YELLOW,scale=0.9,arbitaryPosition=[0.1,0.5,1,1,1.5],position=RIGHT)
        self.wait(10)
        firstLocation = 6*LEFT+3.75*DOWN
        secondLocation = 6*LEFT+3.7*DOWN
        thirdLocation = 6.3*LEFT+3.5*DOWN
        checkBox = Rectangle(height=1.5,width=4.5).set_color(RED).move_to(firstLocation)
        self.play(ShowCreation(checkBox),run_time=0.3)
        self.wait()
        text = TextMobject("(n+1)").scale(0.9).move_to(firstLocation).set_color(RED)
        text1 = TextMobject("(n+1)").scale(0.9).move_to(firstLocation).set_color(RED)
        text2 = TextMobject("(n+1)").scale(0.9).move_to(firstLocation).set_color(RED)
        TextGroup = VGroup()
        self.play(text.shift,3.5*RIGHT,run_time=0.2)
        self.play(Transform(checkBox,Rectangle(height=2,width=5).set_color(RED).move_to(secondLocation)))
        self.play(text1.shift,5*RIGHT,run_time=0.2)
        self.wait()
        self.play(Transform(checkBox,Rectangle(height=2.5,width=5).set_color(RED).move_to(thirdLocation)))
        self.play(text2.shift,6.5*RIGHT,run_time=0.2)
        TextGroup.add(text,text1,text2)
        self.play(Transform(TextGroup,TextMobject("$(n+1)^3$").scale(0.9).move_to(firstLocation).shift(5*RIGHT).set_color(RED)))
        self.play(FadeOut(checkBox))
        self.wait(5)

        firstLocation1 = 6*RIGHT+3.7*DOWN
        secondLocation1 = 6.3*RIGHT+3.5*DOWN
        checkBox1 = Rectangle(height=2,width=4).set_color(GREEN).move_to(firstLocation1)
        TextGroup1 = VGroup()
        self.play(ShowCreation(checkBox1),run_time=0.5)
        text4 = TextMobject("(n+1)").scale(0.9).move_to(firstLocation1).set_color(GREEN)
        text5 = TextMobject("(n+1)").scale(0.9).move_to(firstLocation1).set_color(GREEN)
        self.play(text4.shift,4.5*LEFT,run_time=0.2)
        self.play(Transform(checkBox1,Rectangle(height=2.5,width=4.5).set_color(GREEN).move_to(secondLocation1)))
        self.play(text5.shift,3*LEFT,run_time=0.2)
        TextGroup1.add(text4,text5)
        self.play(Transform(TextGroup1,TextMobject("$(n+1)^2$").scale(0.9).move_to(firstLocation1).shift(3.5*LEFT).set_color(GREEN)))
        self.play(FadeOut(checkBox1))
        self.wait()
        self.play(FadeOut(nyimalay),FadeOut(mama))
        nyimalay = self.get_graph(lambda x: 50*(x)**3,
                                  color=RED,
                                  x_min=0,
                                  x_max=3.5,
                                  )
        
        mama = self.get_graph(lambda x: 50*(x)**2,
                                  color=GREEN,
                                  x_min=0,
                                  x_max=6,
                                  )

        self.play(FadeOut(AllObject2))
        self.wait()
        
        self.play(Write(nyimalay),Write(mama),run_time=0.3)
        self.writeText(7.2*LEFT+3.3*UP,0.3,"n","20","40","60","80","100",remove=False,opt=3,color=RED,scale=0.9,increase=0.33)
        self.writeText(5.2*LEFT+3.3*UP,0.3,"Count","9261","68921","226981","531441","1030301",opt=3,remove=False,color=RED,scale=0.9,increase=0.33)
        self.writeText(5.5*RIGHT+3.3*UP,0.3,"n","20","40","60","80","100",remove=False,opt=3,color=GREEN,scale=0.9,increase=0.33)
        self.writeText(7.5*RIGHT+3.3*UP,0.3,"Count","441","1681","3721","6561","10201",opt=3,remove=False,color=GREEN,scale=0.9,increase=0.33)
        
        self.wait(5)

        self.play(Transform(TextGroup,TextMobject("$n^3+3n^2+3n+1$").scale(0.9).move_to(firstLocation).shift(5*RIGHT).set_color(RED)),\
                  Transform(TextGroup1,TextMobject("$n^2+2n+1$").scale(0.9).move_to(firstLocation1).shift(3.5*LEFT).set_color(GREEN)))
        self.wait(5)
        AllObject3.add(TextGroup1,TextGroup,nyimalayText,mamaText,line,line2,line1,line12)
        self.play(Transform(TextGroup,TextMobject("$O(n^3)$").scale(0.9).move_to(firstLocation).shift(3.5*RIGHT).set_color(RED)),\
                  Transform(TextGroup1,TextMobject("$O(n^2)$").scale(0.9).move_to(firstLocation1).shift(3.5*LEFT).set_color(GREEN)))
        self.wait(5)
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        # width of edges
        self.x_axis.set_stroke(width=2) 
        self.y_axis.set_stroke(width=2)
        # color of edges
        self.x_axis.set_color(YELLOW)
        self.y_axis.set_color(YELLOW)

        self.play(
            *[Write(objeto) 
              for objeto in [
                  self.y_axis,  
                  self.x_axis
              ]
              ],
            run_time=2
        )

class BigOComparison(GraphScene, MovingCameraScene):
    CONFIG = {
        "y_max": 1000,
        "y_min": 0,
        "x_max": 10,
        "x_min": 0,
        "y_tick_frequency": 100,
        "x_tick_frequency": 1,
        "graph_origin": [-4, -3, 0],
        "y_axis_label": None,  # Don't write y axis label
        "x_axis_label": None,
    }
    def writeText(self,place,time,*string,remove,color,scale,arbitaryPosition=None,position=LEFT,delay=0.1,increase=0,opt=0):
        global ReplaceObject
        global AllObject,AllObject2,AllObject3
        Place = place
        object = VGroup()
        a=0
        for i in string:
            if arbitaryPosition is not None:
                try:
                    Place = Place+scale/2*DOWN+increase*DOWN+arbitaryPosition[a]*position-arbitaryPosition[a-1]*position
                except IndexError:
                    Place = Place+scale/2*DOWN+increase*DOWN+arbitaryPosition[a]*position
            else:
                if(str(Place)==str(place)):
                    Place = Place+scale/2*DOWN
                else:
                    Place = Place+scale/2*DOWN+increase*DOWN
            text = TextMobject(i)
            text.scale(scale)
            text.set_color(color)
            text.move_to(Place)
            object.add(text)
            self.play(Write(text),run_time=time)
            a += 1
        
        
        if(remove is True):
            ReplaceObject.add(object)

        if(opt==1):
            AllObject.add(object)
        elif(opt==2):
            AllObject2.add(object)
        elif(opt==3):
            AllObject3.add(object)
        else:
            print("Bad")

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.timecomplexityGraph()
        
    def timecomplexityGraph(self):
        self.setup_axes()
        real = self.get_graph(lambda x: (x+1)**3,
                                  color=RED,
                                  x_min=0,
                                  x_max=9,
                                  )
        
        estimate= self.get_graph(lambda x: (x)**3,
                                  color=GREY,
                                  x_min=0,
                                  x_max=10,
                                  )
        text = TextMobject("$n^2$").set_color(GREY).to_edge(UP+RIGHT)
        text1 = TextMobject("$(n+1)^2$").set_color(RED).to_edge(UP+RIGHT).shift(DOWN)
        self.play(Write(text1),Write(text),run_time=0.3)
        self.wait(5)
        self.play(Write(real),Write(estimate))
        self.play(FadeOut(text),FadeOut(text1))
        self.wait(3)
        real2 = self.get_graph(lambda x: (x+1)**3,
                                  color=RED,
                                  x_min=0,
                                  x_max=40,
                                  )
        
        estimate2= self.get_graph(lambda x: (x)**3,
                                  color=GREY,
                                  x_min=0,
                                  x_max=40,
                                  )
        self.play(Transform(real,real2),Transform(estimate,estimate2),self.camera_frame.set_height,500,run_time=5)
        self.wait(4)
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        # width of edges
        self.x_axis.set_stroke(width=2) 
        self.y_axis.set_stroke(width=2)
        # color of edges
        self.x_axis.set_color(YELLOW)
        self.y_axis.set_color(YELLOW)

        self.play(
            *[Write(objeto) 
              for objeto in [
                  self.y_axis,  
                  self.x_axis
              ]
              ],
            run_time=2
        )


RemoveObject = VGroup()
class Bird(Scene):
    
    def construct(self): 
        text = TextMobject("Today, we are gonna talk about Computational Complexity Analysis").scale(0.8)
        self.play(Write(text))
        self.wait()
        self.play(Transform(text,TextMobject("So, let's talk about the famous Big O Notation")))
        self.wait(2)
        self.play(Transform(text,TextMobject("Big O Notation").set_color(BLUE)))
        self.play(text.to_edge,UP)
        self.wait()
        global RemoveObject
        self.wait(4)#DELAY 1
        bird = SVGMobject("hummingbird").set_color(YELLOW).shift(3*RIGHT+3*DOWN).rotate(-TAU).flip().scale(0.5)
        building = SVGMobject("house-building").set_color(GREY).shift(3*LEFT+UP)
        computer= SVGMobject("computer").set_color(BLUE).shift(3*RIGHT)
        memory = SVGMobject("memory").set_color(BLUE).shift(3*RIGHT+2*UP).scale(0.3)

        self.play(DrawBorderThenFill(bird,rate_func=linear),DrawBorderThenFill(building,rate_func=linear),\
                  DrawBorderThenFill(computer,rate_func=linear),DrawBorderThenFill(memory,rate_func=linear))
        self.wait(6)#DELAY 2
        self.play(bird.move_to,3*LEFT+UP,memory.shift,2*LEFT+0.3*UP,run_time=3)
        self.play(FadeOut(bird),memory.shift,2*LEFT,run_time=3)
        self.play(memory.move_to,3*LEFT+UP,run_time=3)
        self.play(FadeOut(memory))  
        self.wait()

        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)

        explain = VGroup()
        bird = SVGMobject("hummingbird").set_color(YELLOW).shift(2*UP+3*LEFT).rotate(-TAU).flip().scale(0.8)
        computer= SVGMobject("computer").set_color(BLUE).shift(3*RIGHT+2*UP).scale(0.6)
        self.wait(8)
        explain.add(bird,computer)
        self.play(Transform(object,explain))
        self.wait(3)
        self.writeText(3*LEFT,0.3,"100MB\n60min","500MB\t60min","1GB\t60min","4GB\t60min",\
                        remove = False, color = YELLOW, increase = 0.5,scale = 0.8)
        self.writeText(3*RIGHT,0.3,"100MB\t10min","500MB\t50min","1GB\t1000min","4GB\t4000min",\
                        remove = False, color = YELLOW, increase = 0.5,scale = 0.8)
        
        self.wait(5)
        NewObject = VGroup()
        NewObject.add(TextMobject("O(1)").set_color(GREEN).shift(3*LEFT),\
                      TextMobject("O(n)").set_color(RED).shift(3*RIGHT))
        self.play(Transform(RemoveObject,NewObject))
        self.wait(6)
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))
        self.wait()
        
    def writeText(self,place,time,*string,remove,color,scale,arbitaryPosition=None,position=LEFT,delay=0.1,increase=0):
        global RemoveObject
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
        
        RemoveObject.add(object)
        if(remove is True):
            self.wait(delay)
            self.play(FadeOut(object))
    
class AlgorithmExample(Scene):
    def construct(self):
        equation = TextMobject("a+b+c = n").set_color(BLUE).to_edge(UP)
        self.play(Write(equation))
        text = TextMobject("find a,b,c which are non-negative numbers that satisfy this equation").set_color(BLUE).shift(2.5*UP).scale(0.8)
        self.play(Write(text)) 
        self.wait(3)
        nyimalay = TextMobject("nyi ma lay").set_color(RED).to_edge(LEFT).shift(1.5*UP+2*RIGHT).scale(0.8)
        mama = TextMobject("mama").set_color(GREEN).to_edge(RIGHT).shift(1.5*UP+2*LEFT).scale(0.8)
        self.play(Write(nyimalay),Write(mama))
        self.wait(2)

        aLocation = 5*LEFT
        bLocation = 4*LEFT
        cLocation = 3*LEFT
        
        a = TextMobject(str(0)).shift(aLocation).scale(0.8).set_color(RED)
        b = TextMobject(str(0)).shift(bLocation).scale(0.8).set_color(BLUE)
        c = TextMobject(str(0)).shift(cLocation).scale(0.8).set_color(GREEN)
        aText = TextMobject("a").shift(aLocation+0.5*UP).scale(0.8).set_color(RED)
        bText = TextMobject("b").shift(bLocation+0.5*UP).scale(0.8).set_color(BLUE)
        cText = TextMobject("c").shift(cLocation+0.5*UP).scale(0.8).set_color(GREEN)
        
        aLocation1 = 3*RIGHT
        bLocation1 = 4*RIGHT
        cLocation1 = 5*RIGHT
        
        a1 = TextMobject(str(0)).shift(aLocation1).scale(0.8).set_color(RED)
        b1 = TextMobject(str(0)).shift(bLocation1).scale(0.8).set_color(BLUE)
        c1 = TextMobject(str(0)).shift(cLocation1).scale(0.8).set_color(GREEN)
        aText1 = TextMobject("a").shift(aLocation1+0.5*UP).scale(0.8).set_color(RED)
        bText1 = TextMobject("b").shift(bLocation1+0.5*UP).scale(0.8).set_color(BLUE)
        cText1 = TextMobject("c").shift(cLocation1+0.5*UP).scale(0.8).set_color(GREEN)
        
        self.play(Write(a),Write(b),Write(c),Write(aText),Write(bText),Write(cText)\
                  ,Write(a1),Write(b1),Write(c1),Write(aText1),Write(bText1),Write(cText1))

        self.writeText(3.5*LEFT+0.5*DOWN,0.5,"for a in n+1:",\
                       "for b in n+1:",\
                       "for c in n+1:",\
                       "if (a+b+c = n):",\
                       " assign a,b,c",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[0.1,0.5,1,2,2.5],position=RIGHT)
        self.wait(5)
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if(i+j+k==3):
                        self.play(Transform(a,TextMobject(str(k)).shift(aLocation).scale(0.8).set_color(RED)),\
                                  Transform(b,TextMobject(str(j)).shift(bLocation).scale(0.8).set_color(BLUE)),\
                                  Transform(c,TextMobject(str(i)).shift(cLocation).scale(0.8).set_color(GREEN)),run_time=0.3)
                        self.wait(0.2)

        line1 = Line().shift(bLocation1).rotate(-1 * TAU / 2).set_color(RED).scale(1.2)
        text = TextMobject("a+b+c = n").move_to(3.5*RIGHT+2*DOWN).set_color(YELLOW).scale(0.8)
        text1 = TextMobject("c = n-(a+b)").move_to(3.5*RIGHT+2*DOWN).set_color(YELLOW).scale(0.8)
        self.play(Write(text))
        self.wait(4)
        self.play(Transform(text,text1))
        self.wait(4)
        self.play(FadeOut(text))
        self.wait()

        self.writeText(3.5*RIGHT+0.5*DOWN,0.5,"for a in n+1:",\
                       "for b in n+1:",\
                       "c = n-(a+b)",\
                       "if (c>=0):",\
                       " assign a,b,c",remove=False,color=YELLOW,scale=0.8,arbitaryPosition=[0.1,0.5,1,1,1.5],position=RIGHT)
        self.wait(5)
        for i in range(4):
            for j in range(4):
                k = 3-(i+j)
                if k>=0:
                    self.play(Transform(c1,TextMobject(str(k)).shift(cLocation1).scale(0.8).set_color(GREEN)),\
                              Transform(b1,TextMobject(str(j)).shift(bLocation1).scale(0.8).set_color(BLUE)),\
                              Transform(a1,TextMobject(str(i)).shift(aLocation1).scale(0.8).set_color(RED)),run_time=0.3)
                    self.wait(0.2)
                else:
                    self.play(Transform(c1,TextMobject(str(k)).shift(cLocation1).scale(0.8).set_color(GREEN)),\
                              Transform(b1,TextMobject(str(j)).shift(bLocation1).scale(0.8).set_color(BLUE)),\
                              Transform(a1,TextMobject(str(i)).shift(aLocation1).scale(0.8).set_color(RED)),run_time=0.3)
                    
                    self.play(Write(line1),run_time=0.2)
                    self.wait(0.2)
                    self.play(FadeOut(line1),run_time=0.2)
                    
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))
        self.wait()
    
    def writeText(self,place,time,*string,remove,color,scale,arbitaryPosition=None,position=LEFT,delay=0.1,increase=0):
        global ReplaceObject
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
        ReplaceObject.add(object)

class Intro(Scene):
    def construct(self):
        self.wait(1)
        text = TextMobject("Computer Science").scale(1.2)
        text.set_color(YELLOW)
        self.play(Write(text))
        self.wait(8)
        self.play(text.to_edge,UP)
        infoCircle = Circle().set_fill(BLUE,opacity=0.5)
        infoCircle.shift(4*UP)
        infoText = TextMobject("Data").set_color(BLUE).move_to(0.1*DOWN).set_color(WHITE)
        subTitleText = TextMobject("What does it consist of?").set_color(YELLOW).to_edge(DOWN)
        self.play(Write(subTitleText),infoCircle.move_to,0.1*DOWN)
        text1 = TextMobject("Data Structure").scale(1.2).set_color(BLUE).to_edge(UP)
        self.play(Transform(text,text1))
        box1= Rectangle(height=2,width=2).scale(0.5).shift(LEFT)
        box2= Rectangle(height=2,width=2).scale(0.5)
        box3= Rectangle(height=2,width=2).scale(0.5).shift(RIGHT)
        box4= Rectangle(height=2,width=2).scale(0.5).shift(2*RIGHT)
        object = VGroup()
        object.add(box1,box2,box3,box4)
        self.play(Write(infoText))
        self.wait(1)
        self.play(FadeOut(infoText),FadeOut(subTitleText))
        self.play(Transform(infoCircle,object))
        self.wait()

        box_key = Rectangle(height=1,width=1).shift(2*LEFT)
        box_pointer =  Rectangle(height=1,width=1).shift(2*LEFT+DOWN)
        box2_key = Rectangle(height=1,width=1)
        box2_pointer =  Rectangle(height=1,width=1).shift(DOWN)
        box3_key = Rectangle(height=1,width=1).shift(2*RIGHT)
        box3_pointer =  Rectangle(height=1,width=1).shift(2*RIGHT+DOWN)
        vector1 = Vector(0-2*LEFT+UP).shift(2*LEFT+DOWN).set_color(BLUE)
        vector2 = Vector(2*RIGHT+UP-0).shift(DOWN).set_color(BLUE)
        linkedlistobject = VGroup()
        linkedlistobject.add(box_key,box_pointer,box2_key,box2_pointer,box3_key,box3_pointer,\
                             vector1,vector2)
        
        self.play(Transform(infoCircle,linkedlistobject))
        self.wait()
        
        circle1 = Circle().shift(2*UP).scale(0.5)
        circle2 = Circle().shift(2.5*LEFT).scale(0.5)
        circle3 = Circle().shift(2.5*RIGHT).scale(0.5)
        circle4 = Circle().shift(DOWN+4*LEFT).scale(0.5)
        circle5 = Circle().shift(DOWN+LEFT).scale(0.5)
        circle6 = Circle().shift(DOWN+RIGHT).scale(0.5)
        circle7 = Circle().shift(DOWN+4*RIGHT).scale(0.5)
        
        line1 = Line(circle1,circle2)
        line2 = Line(circle1,circle3)
        line3 = Line(circle2,circle4)
        line4 = Line(circle2,circle5)
        line5 = Line(circle3,circle6)
        line6 = Line(circle3,circle7)
        
        TreeObject = VGroup()
        TreeObject.add(circle1,circle2,circle3,circle4,circle5,circle6,circle7,\
                       line1,line2,line3,line4,line5,line6)
        self.play(Transform(infoCircle,TreeObject))
        self.wait()
        DataStrucutreObject = VGroup()
        CurrentObject= VGroup()
        
        for mob in self.mobjects:
            CurrentObject.add(mob)
        
        DataStrucutreObject.add(circle1,circle2,circle3,circle4,circle5,circle6,circle7,\
                                line1,line2,line3,line4,line5,line6,text1)
        text1=TextMobject("Algorithms").scale(1.2).set_color(BLUE).to_edge(UP)
        self.play(ReplacementTransform(CurrentObject,text1))
        DataStrucutreObject.scale(0.5).shift(4*LEFT+UP)
        
        L = 5
        N = 5
        b = L/N
        Max = 10

        rand = random.randint(Max, size=N)
        data = [0]*N
        sorted_data = []
        h = []

        for n in range(N):
            h.append(rand[n]*3/Max)
            data[n] = Rectangle(width=b, height=h[-1], color=WHITE, fill_opacity=1, fill_color=WHITE)
            data[n].move_to([-(L/2)+(b/2)+b*n, 0, 0]).shift(UP*h[-1]/2)

        for n in range(N):
            self.play(Write(data[n]), run_time=1/N)

        for n in range(N):
            current_minimum = rand[0]
            index = 0
            for m in range(len(rand)):
                current = rand[m]
                if current < current_minimum:
                    current_minimum = current
                    index = m
            data[index].set_color(RED)
            self.play(data[index].shift, DOWN*3, run_time=1/N)
            sorted_data.append(data[index])
            data.pop(index)

            for n in range(index):
                self.play(data[index-n-1].shift, RIGHT*b, run_time=1/N)
            if len(data) != 0:
                target = data[0].get_center()
                dx = target[0]-b
                dy = h[index]/2
                self.play(sorted_data[-1].move_to, [dx, dy, 0],
                          sorted_data[-1].set_color, GREEN, run_time=1/N)
            else:
                target = sorted_data[-2].get_center()
                dx = target[0]+b
                dy = h[index]/2
                self.play(sorted_data[-1].move_to, [dx, dy, 0],
                          sorted_data[-1].set_color, GREEN, run_time=1/N)
            rand = np.delete(rand, index)
            h = np.delete(h, index)
        for n in range(N):
            self.play(sorted_data[n].set_color, WHITE, run_time=1/N)

        self.wait()
        CurrentObject = VGroup()
        AlgorithmObject = VGroup()
        for mob in self.mobjects:
            AlgorithmObject.add(mob)
            CurrentObject.add(mob)
        text2=TextMobject("Computational complexity").scale(1.2).set_color(BLUE).to_edge(UP)
        computational_complexity = SVGMobject("discrete_maths").shift(2*RIGHT+2*DOWN).scale(1.2)
        self.play(ShowCreation(computational_complexity))
        self.play(FadeOut(CurrentObject))
        self.play(Write(text2),computational_complexity.shift,2*LEFT+2*UP)
        CC = VGroup()
        CC.add(text2,computational_complexity)
        self.wait(3)
        self.play(FadeOut(CC))
        CC.scale(0.5).shift(4*RIGHT+UP)
        AlgorithmObject.scale(0.5)

        text2=TextMobject("GraphTheory").scale(1.2).set_color(BLUE).to_edge(UP)
        graph = SVGMobject("graph_theory")
        graph.set_color(PURPLE)
        self.play(Write(text2),DrawBorderThenFill(graph,rate_func=linear))
        self.wait() 
        GraphTheory = VGroup()
        GraphTheory.add(text2,graph)
        self.play(GraphTheory.scale,0.5,GraphTheory.shift,3*LEFT+3*DOWN)
        
        text2 = TextMobject("Cryptography").scale(1.2).set_color(BLUE).to_edge(UP)
        encrypt = SVGMobject("encryption").set_color(RED)
        self.play(Write(text2),DrawBorderThenFill(encrypt,rate_func=linear))
        Cryptography = VGroup()
        Cryptography.add(text2,encrypt)
        self.play(Cryptography.scale,0.5,Cryptography.shift,3*DOWN)

        text2 = TextMobject("Programming").scale(1.2).set_color(BLUE).to_edge(UP)
        program = SVGMobject("programming").set_color(YELLOW)
        self.play(Write(text2),DrawBorderThenFill(program,rate_func=linear))
        Programming = VGroup()
        Programming.add(text2,program)
        self.play(Programming.scale,0.5,Programming.shift,3*RIGHT+3*DOWN)
        self.play(FadeIn(DataStrucutreObject),FadeIn(AlgorithmObject),FadeIn(CC))
        self.wait(3)
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))

        self.play(Write(TextMobject("Where is it used?").set_color(YELLOW).to_edge(UP)))
        robot = SVGMobject("roboticarm").set_color(BLUE).shift(2*LEFT+UP)
        ai = SVGMobject("ai").set_color(PINK).shift(2*RIGHT+UP)
        hacker = SVGMobject("hacker").set_color(RED).shift(3*LEFT+2.5*DOWN)
        iot = SVGMobject("gps").set_color(YELLOW).shift(3*RIGHT+2.5*DOWN)
        bigdata = SVGMobject("bigdata").set_color(PURPLE).shift(2.5*DOWN)
        self.play(DrawBorderThenFill(robot,rate_func=linear),DrawBorderThenFill(ai,rate_func=linear))
        self.wait(7) 
        self.play(DrawBorderThenFill(hacker,rate_func=linear),DrawBorderThenFill(iot,rate_func=linear),DrawBorderThenFill(bigdata,rate_func=linear),)
        self.wait(7)
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(FadeOut(object))
        self.wait(1)

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

class Outro(Scene):
    def construct(self):
        reducible = ImageMobject("reducible")
        williamFest = ImageMobject("williamfest").scale(2)
        self.play(FadeIn(reducible))
        self.play(reducible.scale,2,run_time=2)
        self.wait(8)
        self.play(FadeOut(reducible))
        self.play(FadeIn(williamFest),run_time=2)
        self.wait(10)
        self.play(FadeOut(williamFest))
        self.wait()

        a = Box(1)
        a.move(UP+3*LEFT)
        a.construct(self)
        
        b = Box(2,a)
        b.construct(self)
        a.constructPointer(self,b)

        c = Box(3,b)
        c.construct(self)
        b.constructPointer(self,c)
        c.endOfList(self)
        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)
        self.play(object.shift,2*LEFT,object.scale,0.8)
        self.play(FadeOut(object))
        a = ArrayBox(0,0,2*LEFT)
        b = ArrayBox(1,1,LEFT)
        c = ArrayBox(2,2,0)
        a.construct(self,0.3,False)
        b.construct(self,0.3,False)
        c.construct(self,0.3,False)
        self.wait()
        object2 = VGroup()
        for mob in self.mobjects:
            object2.add(mob)
        self.play(object2.shift,3*RIGHT,object2.scale,0.8)
        self.play(FadeIn(object))
        self.wait(3)
        object2 = VGroup()
        for mob in self.mobjects:
            object2.add(mob)
        self.play(FadeOut(object2))
        
        self.wait(3)

class Outro(MovingCameraScene):
    def construct(self):
        title = TextMobject("Why do we have to know this?")
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))
        self.wait(3)
        place = 3*LEFT
        object = VGroup()
        for i in range(8):
            circle = Circle().scale(0.25).set_fill(BLUE,opacity=0.5)
            circle.move_to(place)
            place += RIGHT
            object.add(circle)

        
        self.play(Write(object))

        for circles in object:
            self.play(circles.move_to,4*LEFT,run_time=0.4)
            self.play(FadeOut(circles),run_time=0.4)
        
        object = VGroup()
        object1 = VGroup()
        place = 0.5*DOWN+1.5*LEFT
        for i in range(4):
            circle = Circle().scale(0.25).set_fill(BLUE,opacity=0.5)
            circle.move_to(place)
            circle1 = Circle().scale(0.25).set_fill(RED,opacity=0.5)
            circle1.move_to(UP+place)
            place += RIGHT
            object.add(circle)
            object1.add(circle1)
        
        self.play(FadeIn(object1),FadeIn(object))

        for i in range(4):
            self.play(object[i].move_to,0.5*DOWN+4*LEFT,object1[i].move_to,0.5*UP+4*LEFT,run_time=0.4)
            self.play(FadeOut(object[i]),FadeOut(object1[i]))

        infoCircle = VGroup()
        box1= Rectangle(height=2,width=2).scale(0.5).shift(LEFT)
        box2= Rectangle(height=2,width=2).scale(0.5)
        box3= Rectangle(height=2,width=2).scale(0.5).shift(RIGHT)
        box4= Rectangle(height=2,width=2).scale(0.5).shift(2*RIGHT)
        infoCircle.add(box1,box2,box3,box4)
        self.play(Write(infoCircle))
        self.wait()

        box_key = Rectangle(height=1,width=1).shift(2*LEFT)
        box_pointer =  Rectangle(height=1,width=1).shift(2*LEFT+DOWN)
        box2_key = Rectangle(height=1,width=1)
        box2_pointer =  Rectangle(height=1,width=1).shift(DOWN)
        box3_key = Rectangle(height=1,width=1).shift(2*RIGHT)
        box3_pointer =  Rectangle(height=1,width=1).shift(2*RIGHT+DOWN)
        vector1 = Vector(0-2*LEFT+UP).shift(2*LEFT+DOWN).set_color(BLUE)
        vector2 = Vector(2*RIGHT+UP-0).shift(DOWN).set_color(BLUE)
        linkedlistobject = VGroup()
        linkedlistobject.add(box_key,box_pointer,box2_key,box2_pointer,box3_key,box3_pointer,\
                             vector1,vector2)

        linkedlistobject1 = VGroup()
        linkedlistobject1.add(box_key,box_pointer,box2_key,box2_pointer,box3_key,box3_pointer,\
                             vector1,vector2)


        
        self.play(Transform(infoCircle,linkedlistobject))
        self.wait()
        
        circle1 = Circle().shift(2*UP).scale(0.5)
        circle2 = Circle().shift(2.5*LEFT).scale(0.5)
        circle3 = Circle().shift(2.5*RIGHT).scale(0.5)
        circle4 = Circle().shift(DOWN+4*LEFT).scale(0.5)
        circle5 = Circle().shift(DOWN+LEFT).scale(0.5)
        circle6 = Circle().shift(DOWN+RIGHT).scale(0.5)
        circle7 = Circle().shift(DOWN+4*RIGHT).scale(0.5)
        
        line1 = Line(circle1,circle2)
        line2 = Line(circle1,circle3)
        line3 = Line(circle2,circle4)
        line4 = Line(circle2,circle5)
        line5 = Line(circle3,circle6)
        line6 = Line(circle3,circle7)
        
        TreeObject = VGroup()
        TreeObject.add(circle1,circle2,circle3,circle4,circle5,circle6,circle7,\
                       line1,line2,line3,line4,line5,line6)
        self.play(Transform(infoCircle,TreeObject))
        self.wait()
        self.camera_frame.save_state()
        self.play(
            self.camera_frame.set_height,circle4.get_width()*1.2,
            self.camera_frame.move_to,circle4
        )

        linkedlistobject1.scale(0.1).move_to(DOWN+4*LEFT)
        self.play(Write(linkedlistobject1))
        
        self.wait(3)
        self.play(Restore(self.camera_frame))
        place = [2*UP,2.5*LEFT,2.5*RIGHT,DOWN+LEFT,DOWN+RIGHT,DOWN+4*RIGHT]
        object = VGroup()
        
        duplicateObjects = VGroup()
        for i in range(6):
            box_key = Rectangle(height=1,width=1).shift(2*LEFT)
            box_pointer =  Rectangle(height=1,width=1).shift(2*LEFT+DOWN)
            box2_key = Rectangle(height=1,width=1)
            box2_pointer =  Rectangle(height=1,width=1).shift(DOWN)
            box3_key = Rectangle(height=1,width=1).shift(2*RIGHT)
            box3_pointer =  Rectangle(height=1,width=1).shift(2*RIGHT+DOWN)
            vector1 = Vector(0-2*LEFT+UP).shift(2*LEFT+DOWN).set_color(BLUE)
            vector2 = Vector(2*RIGHT+UP-0).shift(DOWN).set_color(BLUE)
            duplicate = VGroup()
            duplicate.add(box_key,box_pointer,box2_key,box2_pointer,box3_key,box3_pointer,\
                             vector1,vector2)
            duplicate.scale(0.1).move_to(place[i])
            duplicateObjects.add(duplicate)

        self.play(Write(duplicateObjects),run_time=0.5)
        self.wait(3)

        object = VGroup()
        for mob in self.mobjects:
            object.add(mob)

        self.play(FadeOut(mob))
        self.wait()