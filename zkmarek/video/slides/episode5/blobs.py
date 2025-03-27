from manim import FadeOut, Text, RIGHT, DOWN, UP, Create, MathTex, ImageMobject, Indicate, Brace, Write, MoveToTarget, TransformMatchingShapes, FadeIn, TEAL_C, LEFT
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT
from zkmarek.video.slides.common.slide_base import SlideBase

class Blobs(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="Blobs")
        
    def construct(self):
        self.title_text = Text("Blobs", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        self.blob_container = ImageMobject("data/images/blob.png").scale(0.7)
        self.number_sequence = MathTex(r"{{\left[}} {{y_0}}, {{y_1}}, {{y_2}}, {{\cdots}}, {{y_{4095}}}  {{\right]}}", color = SECONDARY_COLOR).next_to(self.blob_container, UP)
        
        self.brace_blob = Brace(self.number_sequence, DOWN).set_color_by_gradient([PRIMARY_COLOR, TEAL_C, HIGHLIGHT_COLOR])
        self.brace_blob.put_at_tip(self.blob_container)
        
        self.less_than_p = MathTex(r"{{\forall}} {{y_k}} \in F_r, \; {{y_k}} < {{r}}", color = PRIMARY_COLOR).next_to(self.brace_blob, RIGHT).shift(DOWN*0.2)
        self.order_p = MathTex(r"r \approx 2^{256} =32 \ \mathrm{B}", color = SECONDARY_COLOR, font_size = 40).next_to(self.less_than_p, DOWN)
        self.bytes_of_ec = Text("32 B", font=PRIMARY_FONT, font_size = 24).set_color(HIGHLIGHT_COLOR)
        
        self.kilo_bytes_of_ec_eqn = Text(" 32 B x 4096", font_size = 24, font = PRIMARY_FONT).set_color_by_gradient([TEAL_C, HIGHLIGHT_COLOR])
        self.kilo_bytes_of_ec_eqn.shift(UP*0.85)
        self.approx = MathTex(r"\approx", font_size=34).set_color_by_gradient([TEAL_C, HIGHLIGHT_COLOR]).next_to(self.kilo_bytes_of_ec_eqn, LEFT, buff = 0.1)
        self.kilo_bytes_of_ec = Text("128 kB", font_size = 28, font = PRIMARY_FONT).set_color_by_gradient([TEAL_C, HIGHLIGHT_COLOR]).next_to(self.kilo_bytes_of_ec_eqn, DOWN, buff = 0.5).shift(UP*0.3)
        self.approx_128 = MathTex(r"\approx", font_size=34).set_color_by_gradient([TEAL_C, HIGHLIGHT_COLOR]).next_to(self.kilo_bytes_of_ec, LEFT, buff = 0.1)
        self.sim_128 = MathTex(r"\sim", font_size=34).set_color_by_gradient([TEAL_C, HIGHLIGHT_COLOR]).next_to(self.kilo_bytes_of_ec, LEFT, buff = 0.1).shift(UP*0.3)
        self.brace_blob.put_at_tip(self.bytes_of_ec)
        
        
    def animate_in(self, scene):
        self.new_subsection(scene, "what is blob?", "data/sound/e5/slide2-1.mp3")
        scene.play(Write(self.title_text))
        scene.play(FadeIn(self.blob_container))
        scene.play(Create(self.number_sequence), Create(self.brace_blob))
        for i in range(5):
            scene.play(Indicate(self.number_sequence[2*i+2], color = HIGHLIGHT_COLOR), run_time=0.3)
        
        self.new_subsection(scene, "field elements", "data/sound/e5/slide2-2.mp3")
        scene.wait(4)
        for i in range(5):
            scene.play(Indicate(self.number_sequence[2*i+2], color = PRIMARY_COLOR), run_time=0.2)
        scene.play(Create(self.less_than_p))
        
        scene.wait(0.5)
             
        self.new_subsection(scene, "32 bytes", "data/sound/e5/slide2-3.mp3")
        scene.wait(1)
        scene.play(Write(self.order_p))   
        scene.wait(2)
        self.number_sequence[4].set_color(HIGHLIGHT_COLOR)
        self.bytes_of_ec.next_to(self.number_sequence[4], UP)
        self.sim_32 = MathTex(r"\sim", color = HIGHLIGHT_COLOR, font_size = 30).next_to(self.bytes_of_ec, LEFT, buff = 0.1)
        scene.wait(1)
        scene.play(Create(self.bytes_of_ec), Create(self.sim_32))
        scene.play(FadeOut(self.less_than_p, self.order_p), run_time=0.5)
        
        self.new_subsection(scene, "128 k bytes", "data/sound/e5/slide2-4.mp3")
        self.blob_container.generate_target()
        self.blob_container.target.to_edge(DOWN).shift(UP)
        scene.play(MoveToTarget(self.blob_container))
        scene.wait(2)
        scene.play(Create(self.kilo_bytes_of_ec), Create(self.approx_128), Create(self.kilo_bytes_of_ec_eqn), Create(self.approx))
        scene.wait(2)
        
        self.new_subsection(scene, "temporary space", "data/sound/e5/slide2-5.mp3")
        scene.play(FadeOut(self.kilo_bytes_of_ec_eqn, self.approx))
        self.kilo_bytes_of_ec.generate_target()
        self.kilo_bytes_of_ec.target.shift(UP*0.3)
        scene.wait(0.5)
        scene.play(TransformMatchingShapes(self.approx_128, self.sim_128), MoveToTarget(self.kilo_bytes_of_ec))
        scene.wait(3.5)
        
        self.new_subsection(scene, "make it accessable", "data/sound/e5/slide2-5a.mp3")
        scene.wait(5)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.brace_blob, self.blob_container, self.number_sequence, self.kilo_bytes_of_ec, self.sim_32, self.sim_128, self.bytes_of_ec, self.title_text))
        