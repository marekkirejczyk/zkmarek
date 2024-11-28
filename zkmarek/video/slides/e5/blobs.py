from manim import FadeOut, Text, RIGHT, DOWN, UP, Create, MathTex, ApplyWave, VGroup, ImageMobject, WHITE, Indicate, Brace, Write, MoveToTarget, PURPLE_C, FadeIn, TEAL_C
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e4.discreete_polynomial_chart import DiscreetePolynomialChart

def poly(x):
    return x * x * x - x * x * 2 + x * 3 + 7


class Blobs(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="Blobs")
        
    def construct(self):
        self.title_text = Text("Blobs", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        # self.blob_container = Rectangle(width=3, height=2, fill_opacity=0.3).set_color_by_gradient([PRIMARY_COLOR, GREY_A, WHITE])
        self.blob_container = ImageMobject("data/images/blob.png").scale(0.7)
        self.number_sequence = MathTex(r"{{\left[}} {{y_0}}, {{y_1}}, {{y_2}}, {{\cdots}}, {{y_{4095}}}  {{\right]}}", color = SECONDARY_COLOR).next_to(self.blob_container, UP)
        self.chart = DiscreetePolynomialChart(41, poly).scale(0.5).shift(DOWN)
        self.brace_blob = Brace(self.number_sequence, DOWN).set_color_by_gradient([PRIMARY_COLOR, TEAL_C, HIGHLIGHT_COLOR])
        self.brace_blob.put_at_tip(self.blob_container)
        self.less_than_p = MathTex(r"<p", color = PRIMARY_COLOR).next_to(self.brace_blob, RIGHT).shift(DOWN*0.2)
        self.order_p = MathTex(r"p \rightarrow 2^{256}", color = SECONDARY_COLOR, font_size = 40).next_to(self.chart.ax[0], RIGHT+UP).shift(UP)
        self.bytes_of_ec = Text("32 B", font=PRIMARY_FONT, font_size = 24).set_color_by_gradient([TEAL_C, HIGHLIGHT_COLOR])
        self.kilo_bytes_of_ec = MathTex(r"\approx 128 \ \mathrm{kB}", font_size = 35).set_color_by_gradient([TEAL_C, HIGHLIGHT_COLOR])
        self.brace_blob.put_at_tip(self.bytes_of_ec)
        self.kilo_bytes_of_ec.shift(UP*0.55)
        self.kilo_bytes_of_ec_eqn = MathTex(r"= 32 \ \mathrm{B} \times 4096", font_size = 28).set_color_by_gradient([TEAL_C, HIGHLIGHT_COLOR]).next_to(self.kilo_bytes_of_ec, DOWN, buff = 0.5).shift(UP*0.3)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "what is blob?", "data/sound/e5/slide2-1.mp3")
        scene.play(Write(self.title_text))
        scene.play(FadeIn(self.blob_container))
        scene.play(Create(self.number_sequence), Create(self.brace_blob))
        for i in range(5):
            scene.play(Indicate(self.number_sequence[2*i+2], color = [HIGHLIGHT_COLOR, PRIMARY_COLOR]), run_time=0.3)
        
        self.new_subsection(scene, "field elements", "data/sound/e5/slide2-2.mp3")
        scene.play(FadeOut(self.blob_container))
        self.chart.gen_points()
        scene.play(Create(self.chart))
        
        self.dots = VGroup(*self.chart.dots)
        scene.wait(2)
        scene.play(Indicate(self.dots, color = [SECONDARY_COLOR, PURPLE_C, TEAL_C]))
        for i in range(5):
            scene.play(Indicate(self.number_sequence[2*i+2], color = [HIGHLIGHT_COLOR, PRIMARY_COLOR]), run_time=0.2)
        scene.play(Create(self.less_than_p))
        
        scene.wait(0.5)
             
        self.new_subsection(scene, "32 bytes", "data/sound/e5/slide2-3.mp3")
        self.chart.generate_target()
        self.chart.target.shift(DOWN)
        scene.wait(1)
        scene.play(ApplyWave(self.chart.labels), Write(self.order_p))   
        scene.wait(2)
        self.number_sequence[4].set_color_by_gradient([WHITE, HIGHLIGHT_COLOR])
        self.bytes_of_ec.next_to(self.number_sequence[4], UP)
        scene.wait(1)
        scene.play(Create(self.bytes_of_ec))
        scene.play(FadeOut(self.less_than_p, self.order_p), run_time=0.5)
        
        self.new_subsection(scene, "128 k bytes", "data/sound/e5/slide2-4.mp3")
        scene.play(MoveToTarget(self.chart))
        scene.wait(2)
        scene.play(Create(self.kilo_bytes_of_ec), Create(self.kilo_bytes_of_ec_eqn))
        scene.wait(2)
        
        self.new_subsection(scene, "temporary space", "data/sound/e5/slide2-5.mp3")
        scene.play(FadeOut(self.kilo_bytes_of_ec_eqn))
        scene.wait(0.5)
        scene.play(Indicate(self.kilo_bytes_of_ec, color = PURPLE_C))
        scene.wait(9)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.brace_blob, self.chart, self.number_sequence, self.kilo_bytes_of_ec, self.bytes_of_ec, self.title_text))
        