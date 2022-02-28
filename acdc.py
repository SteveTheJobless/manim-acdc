from manim import *

class CircuitElements():

    #DC COMPONENTS
    def get_resistor(stroke_width=3,color=WHITE,stroke_opacity=1):
        resistor_points = np.array(([0,0,0],[1,0,0]))
        jag_space = np.array([2,0,0])
        first_point = np.array([1,0,0])
        jag_points = [first_point+jag_space*x/12 for x in range(1,12,2)]
        for i,x in enumerate(jag_points):
            if i%2==0:
                jag_points[i]+=UP/3
            else : jag_points[i]+=DOWN/3
        resistor_points=np.vstack((resistor_points,jag_points))
        resistor_points=np.vstack((resistor_points,np.array(([3,0,0],[4,0,0]))))
        trace = VMobject(color=color,stroke_width=stroke_width,stroke_opacity=stroke_opacity).set_points_as_corners(resistor_points).scale(0.25).move_to(ORIGIN)
        return trace

    def get_cell(stroke_width=3,color=WHITE,stroke_opacity=1):
        trace_1 = VMobject(color=color,stroke_width=stroke_width).set_points_as_corners(np.array(([0,0,0],[1,0,0],[1,1,0],[1,-1,0])))
        trace_2 = VMobject(color=color,stroke_width=stroke_width*2).set_points_as_corners(np.array(([1.25,0.5,0],[1.25,-0.5,0])))
        trace_3 = VMobject(color=color,stroke_width=stroke_width).set_points_as_corners(np.array(([1.25,0,0],[2,0,0])))
        trace=VGroup(trace_1,trace_2,trace_3).scale(0.5).move_to(ORIGIN)
        return trace

    def get_closed_switch(stroke_width=3,color=WHITE):
        trace_1 = Circle(radius=0.1,stroke_width=stroke_width*0.5,stroke_color=color).move_to(np.array([0.5,0,0]))
        trace_2 = Circle(radius=0.1, stroke_width=stroke_width * 0.5, stroke_color=color).move_to(np.array([1.5, 0, 0]))
        trace_3 = VMobject(color=color,stroke_width=stroke_width).set_points_as_corners([ORIGIN,np.array([0.4,0,0])])
        trace_4 = VMobject(color=color,stroke_width=stroke_width).set_points_as_corners(np.array(([0.6,0,0],[1.4,0,0])))
        trace_5 = VMobject(color=color,stroke_width=stroke_width).set_points_as_corners(np.array(([1.6,0,0],[2,0,0])))
        trace = VGroup(trace_1,trace_2,trace_3,trace_4,trace_5).scale(0.5).move_to(ORIGIN)
        return trace

    def get_open_switch(stroke_width=3,color=WHITE):
        trace_1 = VMobject(color=color, stroke_width=stroke_width).set_points_as_corners([ORIGIN, np.array([0.4, 0, 0])])
        trace_2 = Circle(radius=0.1, stroke_width=stroke_width * 0.5, stroke_color=color).move_to(np.array([0.5, 0, 0]))
        trace_3 = VMobject(color=color, stroke_width=stroke_width).set_points_as_corners([trace_2.get_center()+[0.1,0.1,0],trace_2.point_from_proportion(0.15)+[0.7,0.7,0]])
        trace_4 = Circle(radius=0.1, stroke_width=stroke_width * 0.5, stroke_color=color).move_to(np.array([1.5, 0, 0]))
        trace_5 = VMobject(color=color, stroke_width=stroke_width).set_points_as_corners(np.array(([1.6, 0, 0], [2, 0, 0])))
        box = Rectangle(height=2,width=2,fill_opacity=0,stroke_opacity=0).shift(RIGHT)
        trace = VGroup(trace_1, trace_2, trace_3, trace_4, trace_5,box).scale(0.5).move_to(ORIGIN)
        return trace

    def get_ground(stroke_width=3, color=RED):
        trace_1 = Triangle(color=color, stroke_width=stroke_width * 2).scale(0.6).move_to(ORIGIN).rotate(-PI / 2).shift(
            RIGHT / 2)
        trace_2 = VMobject(color=color, stroke_width=stroke_width).set_points_as_corners(
            [LEFT, trace_1.get_critical_point(LEFT)])
        bounds = Rectangle(height=2, width=2, fill_opacity=0, stroke_opacity=0)
        trace = VGroup(trace_1, trace_2, bounds).scale(0.25).rotate(-PI / 2).move_to(ORIGIN)
        return trace



    #AC COMPONENTS
    def get_ac_v_source(stroke_width=3,color=WHITE,stroke_opacity=1):
        trace_1 = VMobject(color=color,stroke_width=stroke_width).set_points_as_corners([ORIGIN,np.array([0.35,0,0])])
        trace_2 = Circle(radius=0.65,stroke_color=color,stroke_width=stroke_width).move_to(RIGHT)
        trace_3 = FunctionGraph(lambda x : 2*np.sin(x),x_range=[0,2*PI],stroke_color=color,stroke_width=stroke_width).rotate(PI/2).scale(0.1).move_to(RIGHT)
        trace_4 = VMobject(color=color,stroke_width=stroke_width).set_points_as_corners(np.array(([1.65,0,0],[2,0,0])))
        trace = VGroup(trace_1,trace_2,trace_3,trace_4)
        return trace

    def get_capacitor(stroke_width=3,color=WHITE,stroke_opacity=1):
        trace_1 = VMobject(color=color,stroke_width=stroke_width).set_points_as_corners(np.array(([0,0,0],[0.9,0,0])))
        trace_2 = VMobject(color=color,stroke_width=stroke_width*1.5).set_points_as_corners(np.array(([0.9,0.6,0],[0.9,-0.6,0])))
        trace_3 = VMobject(color=color,stroke_width=stroke_width*1.5).set_points_as_corners(np.array(([1.1,0.6,0],[1.1,-0.6,0])))
        trace_4 = VMobject(color=color,stroke_width=stroke_width).set_points_as_corners(np.array(([1.1,0,0],[2,0,0])))
        trace=VGroup(trace_1,trace_2,trace_3,trace_4).scale(0.5).move_to(ORIGIN)
        return trace

    def get_inductor(stroke_width=3,color=WHITE,stroke_opacity=1):
        trace_1=VMobject(color=color,stroke_width=stroke_width).set_points_as_corners(np.array(([0,0,0],[0.25,0,0])))
        curve_points = [ np.array([0.25+0.375*x,0,0]) for x in range(0,5)]
        for x in range(0,4):
            trace_1.append_points(ArcBetweenPoints(curve_points[x],curve_points[x+1],angle=-PI).points)
        trace_2=VMobject(color=color,stroke_width=stroke_width).set_points_as_corners([curve_points[4],np.array([2,0,0])])
        trace = trace_1.append_points(trace_2.points).scale(0.5).move_to(ORIGIN)
        return trace

    #MEASURING DEVICES
    def get_ammeter(stroke_width=3,color=WHITE,stroke_opacity=1):
        trace_1 = VMobject(color=color, stroke_width=stroke_width).set_points_as_corners([ORIGIN, np.array([0.35, 0, 0])])
        trace_2 = Circle(radius=0.65, stroke_color=color, stroke_width=stroke_width).move_to(RIGHT)
        trace_3 = Tex("A",color=color).move_to(trace_2.get_center()).scale(1.5)
        trace_4 = VMobject(color=color, stroke_width=stroke_width).set_points_as_corners(np.array(([1.65, 0, 0], [2, 0, 0])))
        trace = VGroup(trace_1, trace_2, trace_3, trace_4).scale(0.5).move_to(ORIGIN)
        return trace

    def get_voltmeter(stroke_width=3,color=WHITE,stroke_opacity=1):
        trace_1 = VMobject(color=color, stroke_width=stroke_width).set_points_as_corners([ORIGIN, np.array([0.35, 0, 0])])
        trace_2 = Circle(radius=0.65, stroke_color=color, stroke_width=stroke_width).move_to(RIGHT)
        trace_3 = Tex("V",color=color).move_to(trace_2.get_center()).scale(1.5)
        trace_4 = VMobject(color=color, stroke_width=stroke_width).set_points_as_corners(np.array(([1.65, 0, 0], [2, 0, 0])))
        trace = VGroup(trace_1, trace_2, trace_3, trace_4).scale(0.5).move_to(ORIGIN)
        return trace

    def get_bulb(stroke_width=3,color=WHITE,stroke_opacity=1):
        trace_1 = VMobject(color=color, stroke_width=stroke_width).set_points_as_corners([ORIGIN, np.array([0.35, 0, 0])])
        trace_2 = Circle(radius=0.65, stroke_color=color, stroke_width=stroke_width).move_to(RIGHT)
        trace_3 = VMobject(color=color,stroke_width=stroke_width*0.8).set_points_as_corners(np.array((trace_2.get_top(),trace_2.get_bottom()))).append_points(
            VMobject(color=color,stroke_width=stroke_width*0.8).set_points_as_corners(np.array((trace_2.get_left(),trace_2.get_right()))).points
        ).rotate(PI/4)
        trace_4 = VMobject(color=color, stroke_width=stroke_width).set_points_as_corners(np.array(([1.65, 0, 0], [2, 0, 0])))
        trace = VGroup(trace_1, trace_2, trace_3, trace_4).scale(0.5).move_to(ORIGIN)
        return trace

#UTILITIES
    def connect_series(elements:list,color=WHITE,stroke_width=3):
        path = VMobject(color=color,stroke_width=stroke_width)
        for i in range(0,len(elements)):
            A = elements[i][0].get_critical_point(elements[i][1])
            B = elements[i][2].get_critical_point(elements[i][3])
            M1 = [A[0],B[1],0]
            M2 = [B[0],A[1],0]

            if i < len(elements)-1:
                C = elements[i+1][2].get_critical_point(elements[i+1][3])
            else:
                C = elements[0][2].get_critical_point(elements[0][3])
            if A[0] <= B[0]:
                if B[0] <= C[0]:
                    M = M1
                else: M = M2
            else:
                if B[0] <= C[0]:
                    M = M2
                else: M = M1
            #self.add(*[Dot(x) for x in [A,B,C,M1,M2]])
            path = path.append_points(VMobject().set_points_as_corners([A,M,B]).points)
        #self.add(*[Dot(path.get_critical_point(x),color = PINK) for x in [UP,UR,RIGHT,DR,DOWN,DL,LEFT,UL]])
        return path

    def connect_parallel(elements:list,color=WHITE,stroke_width=3):
        path =VMobject()
        for i in range(0, len(elements)):
            A = elements[i][0].get_critical_point(elements[i][1])
            B = elements[i][2].get_critical_point(elements[i][3])
            M1 = [A[0], B[1], 0]
            M2 = [B[0], A[1], 0]
            #print(A,B,M1,M2)
            
            if not (A==M1).all():
                VA = np.subtract(elements[i][0].get_center(),A)
                V1A = np.subtract(M1,A)
                V2A = np.subtract(M2,A)
                #print(VA,V1A,V2A)
                VB = np.subtract(elements[i][2].get_center(),B)
                V1B = np.subtract(M1,B)
                V2B = np.subtract(M2,B)
                #print(VB,V1B,V2B)
                M = M1
                if CircuitElements.get_angle(VA,V1A)==0:
                    M = M2
                elif CircuitElements.get_angle(VA,V1A)!=0 and CircuitElements.get_angle(VA,V2A)!=0:
                    if CircuitElements.get_angle(VB,V1B) ==0:
                        M=M2
            else: M=M1
            path = path.append_points(VMobject().set_points_as_corners([A, M, B]).points)
        return path


    def get_angle(V1:np.array,V2:np.array):
        return round(
            np.degrees(np.arccos(np.dot(V1,V2)/(np.linalg.norm(V1)*np.linalg.norm(V2)))))

