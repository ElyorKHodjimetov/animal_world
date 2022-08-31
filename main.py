from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.label import CoreLabel


def collides(rect1, rect2):
    r1x = rect1[0][0]
    r1y = rect1[0][1]
    r2x = rect2[0][0]
    r2y = rect2[0][1]
    r1w = rect1[1][0]
    r1h = rect1[1][1]
    r2w = rect2[1][0]
    r2h = rect2[1][1]

    if (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y):
        return True
    else:
        return False


class Main_Game(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        self._score_label = CoreLabel(text="text core label")
        self._score_label.refresh()
        self._score = 0

        with self.canvas:
            self.player = Rectangle(source="free-icon-lion-5640477.png", pos=(0, 0), size=(110, 110))
            self.enemy = Rectangle(source="free-icon-lioness-7411990.png", pos=(400, 400), size=(60, 60))

            # self._score_instruction = Rectangle(source=self.label.texture, pos=(400, 400), size=self.label.texture.size)

        self.keyPressed = set()
        self._entities = set()

        Clock.schedule_interval(self.move_step, 0)
        self.sound = SoundLoader.load("Zangalewa_-_Zangalewa_65404542.mp3")
        self.sound.play()
        print(self.size)

        score = 10

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
        self._score_label.text = "Счет:" + str(value)

    def add_enity(self, enity):
        self._entities.add(enity)

    def _on_keyboard_closed(self):
        self._keyboard.ubind(on_key_down=self._on_keyboard_down)
        self._on_keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.keyPressed.add(text)

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.keyPressed:
            self.keyPressed.remove(text)

    def move_step(self, dt):
        current_x = self.player.pos[0]
        current_y = self.player.pos[1]

        step_size = 200 * dt

        if "w" in self.keyPressed:
            current_y += 3
        if "s" in self.keyPressed:
            current_y -= 3
        if "a" in self.keyPressed:
            current_x -= 3
        if "d" in self.keyPressed:
            current_x += 3

        self.player.pos = (current_x, current_y)

        if collides((self.player.pos, self.player.size), (self.enemy.pos, self.enemy.size)):
            print("Контакт")
            with self.canvas:
                self.vvvv = Rectangle(source="free-icon-lioness-7412035.png", pos=(370, 370), size=(40, 40))

        else:
            print("................")


class Myapp(App):
    def build(self):
        return Main_Game()


if __name__ == "__main__":
    app = Myapp()
    app.run()
