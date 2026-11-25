"""Draws public/assets/og.png (1200x630), the share preview until screenshot frame 1 exists."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H = 1200, 630
BG, TEXT, SUB, ACCENT, ON_ACCENT = "#16191E", "#EEF0F3", "#A3AAB5", "#2FD3A8", "#16191E"


def font(size, weight):
    f = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", size)
    f.set_variation_by_name(weight)
    return f


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# The tally mark from EveryRepLogo.swift, on its 32-point grid.
s, ox, oy = 4.0, 96, 96
d.rounded_rectangle([ox, oy, ox + 32 * s, oy + 32 * s], radius=9 * s, fill=ACCENT)
for x in (10, 14, 18, 22):
    d.line([ox + x * s, oy + 9 * s, ox + x * s, oy + 23 * s], fill=ON_ACCENT, width=round(2.4 * s))
d.line([ox + 7 * s, oy + 20.5 * s, ox + 25 * s, oy + 11.5 * s], fill=ON_ACCENT, width=round(2.8 * s))
d.text((ox + 32 * s + 28, oy + 16 * s), "EveryRep", font=font(56, "Bold"), fill=TEXT, anchor="lm")

d.text((96, 330), "Lock Apps Until", font=font(84, "Bold"), fill=TEXT)
d.text((96, 425), "You Work Out", font=font(84, "Bold"), fill=ACCENT)
d.text((96, 545), "A real training program, and a lock that waits for it.", font=font(32, "Regular"), fill=SUB)

img.save(ROOT / "public/assets/og.png", optimize=True)
