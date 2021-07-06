from pygame.display import set_mode, set_caption, set_icon, flip
from pygame.image import load
from pygame.time import Clock
from pygame import quit, QUIT
from pygame.event import get
from pygame.draw import aaline
from pygame.gfxdraw import arc
from math import cos, sin, radians, degrees
from datetime import datetime


def show_hand(surface, hms):
    h, m, s = datetime.now().strftime("%H %M %S").split()
    set_caption(f"Clock    {h}.{m}.{s}")

    if hms == "h":
        angle = radians((180 + ((int(h) % 12) * (360 / 12))) * -1)  # -> math.radians()
        arc_gap, hand_length, color = 100, 50, (255, 0, 0)
    elif hms == "m":
        angle = radians((180 + (int(m) * (360 / 60))) * -1)         # -> math.radians()
        arc_gap, hand_length, color = 110, 60, (0, 0, 255)
    elif hms == "s":
        angle = radians((180 + (int(s) * (360 / 60))) * -1)         # -> math.radians()
        arc_gap, hand_length, color = 120, 70, (0, 255, 0)
    else:
        return

    sx, sy = surface.get_size()[0] / 2, surface.get_size()[1] / 2
    ex, ey = sx + hand_length * sin(angle), sy + hand_length * cos(angle)               # -> math.sin(), math.cos()
    aaline(surface, color, (sx, sy), (ex, ey))                                          # -> pygame.draw.aaline()
    arc(surface, int(sx), int(sy), arc_gap, -90, int(degrees(angle) - 90) * -1, color)  # -> pygame.gfxdraw.arc(), math.degrees()


def main():
    display = set_mode((300, 300))      # -> pygame.display.set_mode()
    set_caption("Clock")                # -> pygame.display.set_caption()
    set_icon(load("images/clock.png"))  # -> pygame.display.set_icon(), pygame.image.load()

    clock = Clock()  # -> pygame.time.Clock()

    process_interrupted = False

    while not process_interrupted:
        display.fill((50, 50, 50))

        for hand in ["h", "m", "s"]:
            show_hand(display, hand)

        for event in get():
            if event.type == QUIT:  # -> pygame.QUIT
                process_interrupted = True

        clock.tick(60)
        flip()  # -> pygame.display.flip()

    quit()  # -> pygame.quit()


if __name__ == "__main__":
    main()
