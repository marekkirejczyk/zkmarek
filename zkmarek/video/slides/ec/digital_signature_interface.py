from zkmarek.video.slides.common.code_slide import CodeSlide


class DigitalSignatureInterface(CodeSlide):
    def __init__(self):
        super().__init__(
            "Digital Signature Interface",
            "data/ec/signature_interface.py",
            font_size=24,
            background='rectangle',
            insert_line_no=False
        )
