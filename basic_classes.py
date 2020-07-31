from manimlib.imports import *

class Equations(Scene):
    #always define on a 'construct' method and type in there
    def construct(self):
        question = TextMobject('Question', color=BLUE)
        first_line = TextMobject('Find all functions $f:Q^{+}\\rightarrow Q^{+}$ that satisfy')
        #LaTeX commands start with \\ here
        second_line = TextMobject('$$\\textcircled{1}\\hspace{3mm} f(x+1)=f(x)+1,\, \\forall x \in Q^{+}$$', color=PURPLE)
        third_line = TextMobject('$$\\textcircled{1}\\hspace{3mm} f(x^{2})=[f(x)]^{2},\, \\forall x \in Q^{+}$$', color=BLUE)


        #change position, the defauelt position is at the center of the window
        first_line.shift(2*UP)
        #changes the third_line position to under the second_line
        third_line.next_to(second_line, DOWN)

        solution = TextMobject('Solution',color=PURPLE)

        #change color
        first_line.set_color_by_gradient(BLUE,PURPLE)

        #animate equations
        #ApplyMethod makes the animation of the command set next to the var name
        self.play(ApplyMethod(question.scale,2))
        self.play(FadeOut(question))
        self.play(Write(first_line))
        self.play(Write(second_line))
        self.wait(4)
        self.play(Write(third_line))
        self.wait(4)
        #ReplacementTransform keeps the initial variable (Transform does not)
        self.play(FadeOut(first_line),FadeOut(third_line),ReplacementTransform(second_line, solution))
        #ApplyMethod animates the transition
        self.play(ApplyMethod(solution.scale,2))
        self.play(FadeOut(solution))

        #Solution
        line1 = TextMobject('Take $\\textcircled{2}$ and let $x=1$')
        line2 = TextMobject('$$f(1)=[f(1)]^{2}\\Rightarrow f(1)=1$$')
        line3 = TextMobject('Now, by $\\textcircled{1}$ it is easy to prove by induction that')
        line4 = TextMobject('$$f(n)=n,\, \\forall n \in N$$')
        claim = TextMobject('\\underline{CLAIM}')
        claim1 = TextMobject('$$f(x)=x,\, \\forall x \in Q^{+}$$')
        line1.shift(2**UP+LEFT)
        line3.shift(2**UP+LEFT)
        claim.shift(2**UP+LEFT)

        #animate Solution
        self.play(Write(line1))
        self.wait(2)
        self.play(Write(line2))
        self.wait(4)
        self.play(FadeOut(line2), ReplacementTransform(line1,line3))
        self.wait(2)
        self.play(Write(line4))
        self.wait(4)
        self.play(FadeOut(line4), ReplacementTransform(line3,claim))
        self.wait(1)
        self.play(Write(claim1))
        self.wait(3)
        self.play(FadeOut(claim1))

        #Proof
        proof = TextMobject('Proof:')
        proof1 = TextMobject('It is trivial to see that $f(x+n)=f(x)+n$ for $n$ natural')
        proof2 = TextMobject('Take $\\textcircled{2}$ and substitute $x\\rightarrow x+n$')
        proof.shift(2*UP)

        self.play(ReplacementTransform(claim,proof))
        self.play(Write(proof1))
        self.wait(3)
        self.play(ReplacementTransform(proof1,proof2))
        self.wait(2)

        proof3 = TextMobject('$$f(x^{2}+2nx+n^2)=[f(x)+n]^{2}$$')
        proof4 = TextMobject('$$\\iff f(x^{2}+2nx)+n^{2}=f(x^2)+2nf(x)+n^{2}$$')
        proof4_2 = TextMobject('$$\\iff f(x^{2}+2nx)=f(x^2)+2nf(x)$$')
        proof3.next_to(proof2, DOWN)
        proof4.next_to(proof2, DOWN)
        proof4_2.next_to(proof2, DOWN)

        self.play(Write(proof3))
        self.wait(3)
        self.play(FadeOut(proof2), ReplacementTransform(proof3,proof4))
        self.wait(3)
        self.play(ReplacementTransform(proof4, proof4_2))
        self.wait(2)

        proof5 = TextMobject('Let $x=\\frac{1}{n}$')
        proof6 = TextMobject('$$f\\left(\\frac{1}{n^{2}}+2\\right)=f\\left(\\frac{1}{n^{2}}\\right)+2nf\\left(\\frac{1}{n}\\right)$$')
        proof7 = TextMobject('$$f\\left(\\frac{1}{n^{2}}\\right)+2=f\\left(\\frac{1}{n^{2}}\\right)+2nf\\left(\\frac{1}{n}\\right)$$')
        proof8 = TextMobject('$$\\Rightarrow f\\left(\\frac{1}{n}\\right)=\\frac{1}{n}$$')
        proof6.next_to(proof5, DOWN)
        proof7.next_to(proof5, DOWN)
        proof8.next_to(proof5, DOWN)

        self.play(FadeOut(proof4_2))
        self.play(Write(proof5))
        self.play(Write(proof6))
        self.wait(2)
        self.play(ReplacementTransform(proof6, proof7))
        self.wait(1)
        self.play(ReplacementTransform(proof7,proof8))
        self.wait(2)
        self.play(FadeOut(proof8), FadeOut(proof), FadeOut(proof5))


        #final part
        proof9 = TextMobject('Now, by $\\textcircled{1}$ we can extend this easily to have')
        proof10 = TextMobject('$$f(x)=x,\, \\forall x \in Q^{+}$$')
        square = Square()
        square.scale(0.2)
        proof9.shift(2*UP)
        square.next_to(proof10, DOWN)

        self.play(Write(proof9))
        self.wait(1)
        self.play(Write(proof10))
        self.play(GrowFromCenter(square))
        self.wait()


class CreateGraph(GraphScene, Scene):
    #dictionary that allow to change this properties
    CONFIG = {
        'x_min': -1,
        'x_max': 9,
        'y_min': -1,
        'y_max': 9,
        'graph_origin': ORIGIN,
        'axes_color': BLUE,
        "graph_origin": 3 * DOWN + 5.5 * LEFT,
        #range(n, m, s) creates a list from n to m not inclusive with steps of size s
        'x_labeled_nums': range(0,9,2),
        'y_labeled_nums': range(0,9,2)
    }

    def construct(self):
        #Create Graph
        self.setup_axes(animate=True)
        #you can also add the function and its color to the CONFIG dict
        #and set the parameters of get_graph  beginning with <self.> followed by the name of the variable
        graph = self.get_graph(lambda x: x, WHITE)
        graph_label = self.get_graph_label(graph, label='y = x')

        graph2 = self.get_graph(lambda x: x**2, WHITE)
        graph_label2 = self.get_graph_label(graph2, label='y = x^{2}')

        #Display graph
        self.play(ShowCreation(graph), Write(graph_label))
        self.wait(2)
        self.play(Transform(graph, graph2), Transform(graph_label, graph_label2))
        self.wait(2)
        #if you do this graph2 won't dissapear as it moves its info to graph (Transform)
        #self.play(FadeOut(graph2))



#https://talkingphysics.wordpress.com/2019/01/08/getting-started-animating-with-manim-and-python-3-7/

class ExampleApproximation(GraphScene):
    CONFIG = {
        "function" : lambda x : np.cos(x),
        "function_color" : BLUE,
        "taylor" : [lambda x: 1, lambda x: 1-x**2/2, lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4), lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6),
        lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8), lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8) - x**10/math.factorial(10)],
        "center_point" : 0,
        "approximation_color" : GREEN,
        "x_min" : -10,
        "x_max" : 10,
        "y_min" : -1,
        "y_max" : 1,
        "graph_origin" : ORIGIN ,
        "x_labeled_nums" :range(-10,12,2),

    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(
            self.function,
            self.function_color,
        )
        approx_graphs = [
            self.get_graph(
                f,
                self.approximation_color
            )
            for f in self.taylor
        ]

        term_num = [
            TexMobject("n = " + str(n),aligned_edge=TOP)
            for n in range(0,8)]
        #[t.to_edge(BOTTOM,buff=SMALL_BUFF) for t in term_num]


        #term = TexMobject("")
        #term.to_edge(BOTTOM,buff=SMALL_BUFF)
        term = VectorizedPoint(3*DOWN)

        approx_graph = VectorizedPoint(
            self.input_to_graph_point(self.center_point, func_graph)
        )

        self.play(
            ShowCreation(func_graph),
        )
        for n,graph in enumerate(approx_graphs):
            self.play(
                Transform(approx_graph, graph, run_time = 2),
                Transform(term,term_num[n])
            )
            self.wait()
