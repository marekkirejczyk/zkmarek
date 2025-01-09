from manim import VGroup, Text, RIGHT, DOWN
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT

class BulletList(VGroup):
    def __init__(self, items, bullet_styles=None, bullet_offset=0.5, line_spacing=0.7, **kwargs):
        """
        A bullet list with custom styles and positioning.

        Parameters:
        - items: List of strings for the text content of each list item.
        - bullet_styles: List of strings for bullet styles. Defaults to "(i)", "(ii)", etc.
        - bullet_offset: Horizontal spacing between bullets and text.
        - line_spacing: Vertical spacing between list items.
        - kwargs: Additional arguments passed to VGroup.
        """
        super().__init__(**kwargs)
        
        if not all(isinstance(item, str) for item in items):
            raise ValueError("All items in the list must be strings.")
        
        if bullet_styles is None:
            bullet_styles = ["(i)", "(ii)", "(iii)", "(iv)", "(v)", "(vi)", "(vii)", "(viii)", "(ix)", "(x)"]

        if len(bullet_styles) < len(items):
            raise ValueError("Insufficient bullet styles for the number of items.")

        self.bullets = []
        self.items = []

        previous_item = None
        for i in range(len(items)):
            bullet = Text(bullet_styles[i], color=PRIMARY_COLOR, font=PRIMARY_FONT)
            item = Text(items[i], color=PRIMARY_COLOR, font=PRIMARY_FONT)
            
            item.next_to(bullet, RIGHT, buff=bullet_offset)

            if previous_item:
                bullet.next_to(previous_item, DOWN, buff=line_spacing)

            self.add(bullet, item)
            self.bullets.append(bullet)
            self.items.append(item)
            previous_item = bullet
