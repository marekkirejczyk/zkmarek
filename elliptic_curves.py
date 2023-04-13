from src.cpoint import CPoint
from src.sidebar import Sidebar
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
        self.operations(group)
        self.next_section("Negation", type=PresentationSectionType.NORMAL)
        self.negation(ax)
        # self.next_section("Addition", type=PresentationSectionType.NORMAL)
        # self.addition(ax)

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


    def draw_point(self, ax, label, p, color=GREEN):
        point = Dot(ax.coords_to_point(p.x, p.y), color=GREEN)
        lines = ax.get_lines_to_point(ax.c2p(p.x, p.y))
        text = r"{}({:.4f}, {:.4f})".format(label, p.x, p.y)
        label = MathTex(text, font_size=30).next_to(point, RIGHT)

        self.play(Write(lines), Wait())
        self.play(Create(point), Wait())
        self.play(Create(label), Wait())

        return [point, lines, label]


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

    def operations(self, group):
        self.play(group.animate.shift(LEFT * 3.2), Wait())
        sidebar = Sidebar(group, "Operations", tex_filename="data/operations.tex")
        self.play(Write(sidebar), Wait())
        self.play(FadeOut(sidebar), Wait())



    def negation(self, ax):
        sidebar = Sidebar(ax, "Negation", code_filename="data/neg.py")
        self.play(Write(sidebar), Wait())

        p = CPoint.from_compressed(2)
        self.draw_point(ax, "A", p)
        self.draw_point(ax, "-A", p.neg())

        self.play(FadeOut(sidebar), Wait())

    def addition(self, ax):
        p1 = CPoint.from_compressed(2)
        p2 = CPoint.from_compressed(3)
        p3 = p1 + p2
        self.draw_point(ax, "A", p1)
        self.draw_point(ax, "B", p2)
        self.draw_point(ax, "A + B", p3)

        line = DashedLine(start=p1.to_coord(ax), end=p2.to_coord(ax), dashed_ratio=0.6).scale(10)
        print(line.start)
        self.play(Write(line), Wait(2))


