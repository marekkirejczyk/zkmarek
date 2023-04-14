from src.cpoint import CPoint
from src.mobjects.sidebar import Sidebar
from src.mobjects.line_through_points import LineThroughPoints
from src.mobjects.point_on_curve import PointOnCurve
from manim import *
from manim_editor import PresentationSectionType

config.width = 16
config.height = 9

class EllipticCurves(Scene):
    def construct(self):
        # self.next_section("Title", type=PresentationSectionType.NORMAL)
        # self.title_sequence()

        # self.next_section("Elliptic Curve equation", type=PresentationSectionType.NORMAL)
        # self.equation()

        self.next_section("Chart", type=PresentationSectionType.NORMAL)
        group, ax = self.elliptic_chart()

        self.next_section("Operations", type=PresentationSectionType.NORMAL)
        operations = self.operations(group, ax)

        # self.next_section("Negation", type=PresentationSectionType.NORMAL)
        # self.play(FadeOut(operations), Wait())
        # negation = self.negation(ax)

        self.next_section("Addition", type=PresentationSectionType.NORMAL)
        # self.play(FadeOut(negation), Wait())
        addition = self.addition(ax)

        self.play(FadeOut(addition), Wait())

    def title_sequence(self):
        title = Text("Elliptic Curves")
        self.play(Write(title), Wait(3))
        self.play(FadeOut(title))


    def equation(self):
        # Weierstrass Equation
        weierstrass_form = Text(r"Weierstrass form")
        weierstrass_equation = MathTex(r"y^2 = x^3 + ax + b")
        weierstrass_form.next_to(weierstrass_equation, UP)

        self.play(Write(weierstrass_form), Write(weierstrass_equation), Wait())


        # secp256k1 equation
        secp256k1_label = Text(r"Secp256k1 equation")
        secp256k1_label.next_to(weierstrass_equation, DOWN, buff=1)
        self.play(FadeIn(secp256k1_label))

        secp_equation1 = weierstrass_equation.copy()
        self.add(secp_equation1)
        secp_equation1.generate_target()
        secp_equation1.target.next_to(secp256k1_label, DOWN)
        self.play(MoveToTarget(secp_equation1))
        secp_equation1[0][6:7].set_color(YELLOW)
        secp_equation1[0][9:10].set_color(YELLOW)

        #Substitute a and b
        a = MathTex(r"a = 0", color=YELLOW)
        b = MathTex(r"b = 7", color=YELLOW)
        ab = VGroup(a, b).arrange_submobjects()
        ab.next_to(secp_equation1, DOWN)
        self.play(FadeIn(ab))

        secp_equation2 = MathTex(r"y^2 = x^3 + 0x + 7")
        secp_equation2.move_to(secp_equation1)
        secp_equation3 = MathTex(r"y^2 = x^3 + 7")
        secp_equation3.move_to(secp_equation2)
        self.play(ReplacementTransform(secp_equation1, secp_equation2), FadeOut(ab), Wait())
        self.play(ReplacementTransform(secp_equation2, secp_equation3), Wait())

        # Clean-up
        self.play(FadeOut(weierstrass_form), FadeOut(weierstrass_equation), Wait())
        self.play(FadeOut(secp256k1_label), FadeOut(secp_equation3), Wait())


    def elliptic_chart(self):
        group = Group()
        ax = Axes(
            x_range=[-5, 7, 2],
            y_range=[-8, 8, 2],
            x_length=7,
            axis_config={"include_numbers": True}
        )
        group.add(ax)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amsfonts}")
        labels = ax.get_axis_labels(
            Tex(r"$\mathbb{R}$", tex_template=myTemplate, font_size=26),
            Tex(r"$\mathbb{R}$", tex_template=myTemplate, font_size=26)
        )

        graph = ax.plot_implicit_curve(
            lambda x, y: y**2 - x**3 - 7,
            color=YELLOW
        )
        group = VGroup(ax, labels, graph)
        self.play(Create(ax), Wait())
        self.play(Create(labels), Wait())
        self.play(Create(graph), Wait())
        return [group, ax]

    def operations(self, group, ax):
        a = CPoint.from_compressed(1)
        p1 = PointOnCurve(ax, "A(x, y)", a)
        p2 = PointOnCurve(ax, "A", a, include_coords=True)
        self.play(*p1.animate_appear(), Wait())
        self.play(ReplacementTransform(p1, p2), Wait())
        self.play(FadeOut(p2), Wait())

        self.play(group.animate.shift(LEFT * 3.2), Wait())
        sidebar = Sidebar(group, "Operations", tex_filename="data/operations.tex")
        self.play(Write(sidebar), Wait())
        self.play(FadeOut(sidebar), Wait())

    def negation(self, ax):
        sidebar = Sidebar(ax, "Negation", tex_filename="data/neg.tex", code_filename="data/neg.py")
        a = CPoint.from_compressed(2)
        p1 = PointOnCurve(ax, "A", a, include_lines=True)
        p2 = PointOnCurve(ax, "-A", -a, include_lines=True)
        self.play(*p1.animate_appear(), *p2.animate_appear(), Wait())
        self.play(Write(sidebar), Wait())
        return VGroup(p1, p2, sidebar)

    def addition(self, ax):
        a = CPoint.from_compressed(2)
        b = CPoint.from_compressed(3)
        c = a + b
        p1 = PointOnCurve(ax, "A", a)
        p2 = PointOnCurve(ax, "B", b)
        p3 = PointOnCurve(ax, "A + B", c, label_direction=LEFT)
        p4 = PointOnCurve(ax, "-(A + B)", -c, label_direction=LEFT)
        self.play(*p1.animate_appear(), Wait())
        self.play(*p2.animate_appear(), Wait())
        line1 = LineThroughPoints(p1, p2)
        self.play(Write(line1), Wait(2))
        self.play(*p4.animate_appear(), Wait())
        line2 = LineThroughPoints(p3, p4)
        self.play(Write(line2), Wait(2))
        self.play(*p3.animate_appear(), Wait())
        sidebar = Sidebar(ax, "Addition", tex_filename="data/add.tex", code_filename="data/add.py")
        return VGroup(p1, p2, p3, p4, line1, line2, sidebar)


