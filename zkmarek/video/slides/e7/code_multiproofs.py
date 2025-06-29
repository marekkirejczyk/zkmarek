from manim import FadeIn, Text, UP, Write, Indicate, Code, Scene, FadeOut, DOWN
from zkmarek.video.constant import PRIMARY_FONT, PRIMARY_COLOR, SECONDARY_COLOR
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.utils import find_in_code

class Multiproofs(CodeSlide):
    def __init__(self) -> None:
        super().__init__("Multiproofs", "data/snippets/make_multiproof.py")

    def construct(self):
        self.title_label = (
            Text(
                "Multiproofs",
                font=PRIMARY_FONT,
                color=PRIMARY_COLOR,
                font_size=40,
            )
            .to_edge(UP)
        )
        self.code = Code("data/snippets/make_multiproof.py", 
                         background="rectangle", 
            language="python",).scale(0.55).shift(DOWN * 0.5)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "prover quoery", "data/sound/e7/slide7-1.mp3")
        scene.play(Write(self.title_label))
        scene.play(FadeIn(self.code))
        scene.wait(1.5)
        self.indicate_code(scene, self.code, "def generateMultiProof", run_time=1)
        scene.wait(5)
        self.indicate_code(scene, self.code, "x_i", run_time=1)
        scene.wait(2)
        self.indicate_code(scene, self.code, "a_i", run_time=1)
        scene.wait(2)
        self.indicate_code(scene, self.code, "VerklePath", run_time=1)
        scene.wait(1)
        self.indicate_code(scene, self.code, "c0, c1 = VerklePath", run_time=1)
        scene.wait(2.7)
        
        self.new_subsection(scene, "+ list of polynomials", "data/sound/e7/slide7-2.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, "polynomials", run_time=1)
        
        self.new_subsection(scene, "challenge scalar r", "data/sound/e7/slide7-3.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, "r = hash(c2, c1, c0, a_i, hash(c0), hash(c1))", run_time=1)
        scene.wait(2.4)
        challenges = ["c2", "c1", "c0", "a_i", "hash(c0)", "hash(c1)"]
        indices = [1, 1, 1, 1, 0, 0]
        for i, challenge in enumerate(challenges):
            self.indicate_code(scene, self.code, challenge, index=indices[i], run_time=0.4)
        
        self.new_subsection(scene, "set up openings", "data/sound/e7/slide7-4.mp3")
        scene.wait(0.5)
        self.indicate_code(scene, self.code, "opening_indices", run_time=1)
        self.indicate_code(scene, self.code, "opening_values", run_time=1)
        scene.wait(1)
        self.indicate_code(scene, self.code, "a_i", index = 2, run_time=1)
        scene.wait(2)
        self.indicate_code(scene, self.code, "hash(c0)", index = 1, run_time=1)
        self.indicate_code(scene, self.code, "hash(c1)", index = 1, run_time=1)
        
        self.new_subsection(scene, "g - random linear combination", "data/sound/e7/slide7-5.mp3")
        scene.wait(3)
        self.indicate_code(scene, self.code, "g = polynomial.zero()", run_time=1)
        scene.wait(3.5)
        self.indicate_code(scene, self.code, "(p_i(x) - vi) / (x - xi)", run_time=1)
        scene.wait(1)
        
        self.new_subsection(scene, "for each opening - quotient", "data/sound/e7/slide7-6.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, "xi = opening_indices[i]", run_time=1)
        self.indicate_code(scene, self.code, "vi = opening_values[i]", run_time=1)
        scene.wait(1)
        self.indicate_code(scene, self.code, "p_i = polynomials[i]", run_time=1)
        scene.wait(2)
        self.indicate_code(scene, self.code, "(p_i(x) - vi) / (x - xi)", run_time=1)
        scene.wait(2)
        self.indicate_code(scene, self.code, "(p_i(x) - vi)", run_time=1)
        self.indicate_code(scene, self.code, "(x - xi)", run_time=1)
        self.new_subsection(scene, "quotient verifies opening", "data/sound/e7/slide7-7.mp3")
        scene.wait(4.5)
        self.indicate_code(scene, self.code, "xi = opening_indices[i]", run_time=1)
        self.indicate_code(scene, self.code, "vi = opening_values[i]", run_time=1)
        scene.wait(3)
        self.indicate_code(scene, self.code, "r ** i", run_time=1)
        
        self.new_subsection(scene, "commit to g", "data/sound/e7/slide7-8.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, "D = commit(g)", run_time=1)
        
        self.new_subsection(scene, "random s -> g(s)", "data/sound/e7/slide7-9.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, "s = hash(D, c0, c1, c2, a_i, hash(c0), hash(c1))", run_time=1)
        
        self.new_subsection(scene, "generate proof", "data/sound/e7/slide7-10.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, "pi = generate_proof(D, s, value)", run_time=1)
        
        self.new_subsection(scene, "pi - multiproof", "data/sound/e7/slide7-11.mp3")
        scene.wait(3)
        self.indicate_code(scene, self.code, "return (pi, c0, c1)", run_time=1)
        scene.wait(5)

        
    def animate_out(self, scene):
        scene.play(FadeOut(self.code))
        scene.play(FadeOut(self.title_label))
        
        
    def indicate_code(self, scene: Scene, code, fragment: str, index=0, run_time=1):
        chars = find_in_code(code, fragment)
        scene.play(Indicate(chars[index]), color=SECONDARY_COLOR, run_time=run_time)

    @staticmethod
    def _get_code(path: str):
        return Code(
            path,
            background="rectangle",
        )
