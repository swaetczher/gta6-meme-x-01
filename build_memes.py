#!/usr/bin/env python3
"""Build 3 meme candidates for gta6-meme-x-01 ronde 2 (1200x1200, PIL flat vector).
Ghost = official make.fun press-kit mark (mark-1024.png), pasted as a CHARACTER
in each scene, never as a corner banner. Text is real PIL type, big + few lines.
v2: fixes from visual review (no text-on-object overlaps, dog/ghost sit on the
jet ski, dog at the FRONT, note fits its box, labels inside the canvas).
"""
import math
from PIL import Image, ImageDraw, ImageFont

W = H = 1200
OUT = "/home/hatch/workspace/makefun/gta6-meme-x-01-r2-build"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
GHOST = f"{OUT}/mark-1024.png"

WHITE = (255, 255, 255)
BLACK = (20, 16, 28)
YELLOW = (255, 214, 64)
MAGENTA = (233, 30, 140)
BLUE = (96, 196, 255)
NAVY = (26, 22, 48)


def font(sz):
    return ImageFont.truetype(FONT_B, sz)


def text_center(d, y, s, f, fill, stroke=8, stroke_fill=BLACK):
    """Centred text with outline; returns bottom y."""
    bbox = d.textbbox((0, 0), s, font=f, stroke_width=stroke)
    w = bbox[2] - bbox[0]
    d.text(((W - w) / 2 - bbox[0], y), s, font=f, fill=fill,
           stroke_width=stroke, stroke_fill=stroke_fill)
    return y + (bbox[3] - bbox[1])


def text_right(d, x_right, y, s, f, fill):
    bbox = d.textbbox((0, 0), s, font=f)
    d.text((x_right - (bbox[2] - bbox[0]), y), s, font=f, fill=fill)


def gradient(img, top, bottom):
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)


def ghost(img, x, y, size):
    """Paste official ghost, cropped to its alpha bbox, at (x, y) size px."""
    g = Image.open(GHOST).convert("RGBA")
    g = g.crop(g.getchannel("A").getbbox())
    g = g.resize((size, size), Image.LANCZOS)
    img.paste(g, (x, y), g)
    return x, y, size


def hard_hat(d, gx, gy, gs):
    """Yellow construction helmet on top of a ghost placed at (gx, gy, gs)."""
    cx = gx + gs // 2
    top = gy + int(gs * 0.02)
    d.pieslice([cx - int(gs * 0.34), top, cx + int(gs * 0.34),
                top + int(gs * 0.42)], 180, 360, fill=YELLOW,
               outline=BLACK, width=6)
    d.rectangle([cx - int(gs * 0.42), top + int(gs * 0.20),
                 cx + int(gs * 0.42), top + int(gs * 0.27)],
                fill=YELLOW, outline=BLACK, width=5)
    d.rectangle([cx - int(gs * 0.10), top - int(gs * 0.06),
                 cx + int(gs * 0.10), top + int(gs * 0.10)],
                fill=YELLOW, outline=BLACK, width=4)


def brick_wall(d, x0, y0, x1, y1, bw=120, bh=52):
    """Half-built brick wall with a missing chunk (unfinished top-right)."""
    brick = (196, 84, 60)
    mortar = (240, 214, 190)
    d.rectangle([x0, y0, x1, y1], fill=mortar)
    row = 0
    y = y0
    while y < y1:
        off = (bw // 2) if row % 2 else 0
        x = x0 - off
        while x < x1:
            # top two rows: leave a gap on the right (wall unfinished)
            if y < y0 + 2 * bh and x > x0 + (x1 - x0) * 0.55:
                x += bw
                continue
            d.rectangle([x + 3, y + 3, min(x + bw - 3, x1), min(y + bh - 3, y1)],
                        fill=brick, outline=(120, 45, 30), width=2)
            x += bw
        y += bh
        row += 1


def palm(d, x, y, s, lean=0):
    """Simple palm silhouette (drawn AFTER the wall so it stays visible)."""
    trunk = (60, 40, 30)
    leaf = (25, 110, 55)
    d.line([(x, y), (x + lean, y - s)], fill=trunk, width=14)
    for ang in (-70, -35, 0, 35, 70):
        a = math.radians(ang - 90)
        ex = x + lean + int(math.cos(a) * s * 0.55)
        ey = y - s + int(math.sin(a) * s * 0.28) + 10
        d.line([(x + lean, y - s), (ex, ey)], fill=leaf, width=10)


# ---------------------------------------------------------------- A: bolos kerja
def meme_a():
    img = Image.new("RGB", (W, H), (52, 58, 86))
    d = ImageDraw.Draw(img)
    # --- top half: empty office, cold grey-blue
    d.rectangle([0, 0, W, 600], fill=(58, 66, 96))
    d.rectangle([0, 520, W, 600], fill=(40, 44, 66))  # floor
    # headline first, clear of everything
    text_center(d, 18, "SKIP WORK", font(96), WHITE)
    text_center(d, 118, "TO PLAY GTA 6", font(96), YELLOW)
    # window BELOW the headline, left side, city lights
    d.rectangle([80, 260, 460, 500], fill=(18, 20, 44), outline=BLACK, width=6)
    for wx in range(110, 440, 60):
        for wy in (300, 370, 440):
            d.rectangle([wx, wy, wx + 22, wy + 30], fill=YELLOW)
    # wall clock, top right, clear of headline
    d.ellipse([1030, 90, 1130, 190], fill=WHITE, outline=BLACK, width=5)
    d.line([(1080, 140), (1080, 105)], fill=BLACK, width=5)
    d.line([(1080, 140), (1105, 150)], fill=BLACK, width=5)
    # empty desk + chair, right side
    d.rectangle([640, 380, 1140, 410], fill=(120, 90, 60), outline=BLACK, width=5)
    d.rectangle([660, 410, 690, 520], fill=(90, 66, 44))
    d.rectangle([1090, 410, 1120, 520], fill=(90, 66, 44))
    # chair: backrest + seat + leg (pushed away from the desk)
    d.rectangle([830, 430, 860, 510], fill=(150, 40, 50), outline=BLACK, width=5)
    d.rectangle([830, 470, 980, 500], fill=(150, 40, 50), outline=BLACK, width=5)
    d.rectangle([895, 500, 915, 560], fill=BLACK)
    # sick-leave note sitting ON the desk (box sized to fit its text)
    d.rectangle([680, 320, 920, 395], fill=WHITE, outline=BLACK, width=5)
    d.text((700, 330), "CUTI SAKIT", font=font(30), fill=(200, 30, 40))
    d.text((722, 366), "— GTA 6 —", font=font(24), fill=BLACK)
    # --- divider
    d.rectangle([0, 596, W, 610], fill=YELLOW)
    # --- bottom half: Vice City construction site at sunset
    grad = Image.new("RGB", (W, 590), (0, 0, 0))
    gradient(grad, (255, 140, 90), (140, 40, 120))
    img.paste(grad, (0, 610))
    d = ImageDraw.Draw(img)
    # brick wall, half-built
    brick_wall(d, 90, 900, 700, 1180)
    # one palm at the far left edge, drawn after the wall
    palm(d, 45, 1180, 190, lean=25)
    # ghost foreman with hard hat (no trowel prop — helmet + site board sell it)
    # gy 860: helmet dome starts below the "STILL WORKING" baseline
    gx, gy, gs = 760, 860, 330
    ghost(img, gx, gy, gs)
    d = ImageDraw.Draw(img)
    hard_hat(d, gx, gy, gs)
    # site board
    d.rectangle([90, 640, 620, 700], fill=NAVY, outline=YELLOW, width=5)
    d.text((115, 652), "SITE: VICE CITY", font=font(34), fill=WHITE)
    d.text((430, 652), "make.fun", font=font(34), fill=BLUE)
    text_center(d, 700, "10 HOURS LATER:", font(72), WHITE)
    text_center(d, 782, "STILL WORKING", font(84), YELLOW)
    img.save(f"{OUT}/meme-a.png")


# ---------------------------------------------------------------- B: 212 GB
def meme_b():
    img = Image.new("RGB", (W, H), (16, 18, 40))
    d = ImageDraw.Draw(img)
    text_center(d, 40, "DELETED 10 GAMES", font(88), WHITE)
    text_center(d, 140, "FOR 1 GAME", font(88), YELLOW)
    # storage bar
    d.rectangle([70, 300, 1130, 430], fill=(40, 44, 70), outline=WHITE, width=6)
    d.rectangle([76, 306, 1010, 424], fill=MAGENTA)
    d.text((110, 335), "GTA 6 — 212 GB", font=font(64), fill=WHITE)
    d.text((1020, 350), "90%", font=font(44), fill=WHITE)
    # free-space label, right-aligned INSIDE the canvas
    text_right(d, 1125, 445, "free: 3 GB", font(30), (180, 180, 200))
    # deleted game boxes, crossed out, in a row
    for i, name in enumerate(["GAME 1", "GAME 2", "GAME 3"]):
        x = 110 + i * 240
        d.rectangle([x, 520, x + 190, 660], fill=(70, 76, 110),
                    outline=WHITE, width=4)
        d.text((x + 28, 565), name, font=font(30), fill=WHITE)
        d.line([(x + 15, 535), (x + 175, 645)], fill=(255, 60, 60), width=10)
        d.line([(x + 175, 535), (x + 15, 645)], fill=(255, 60, 60), width=10)
    # ghost mover carrying a cardboard box labelled make.fun
    gx, gy, gs = 820, 560, 330
    ghost(img, gx, gy, gs)
    d = ImageDraw.Draw(img)
    # mover cap
    d.pieslice([gx + gs // 2 - 90, gy + 5, gx + gs // 2 + 90, gy + 95],
               180, 360, fill=BLUE, outline=BLACK, width=5)
    d.rectangle([gx + gs // 2 - 105, gy + 55, gx + gs // 2 + 105, gy + 75],
                fill=BLUE, outline=BLACK, width=4)
    # cardboard box in front, text sized to fit inside it
    d.rectangle([gx + 140, gy + 190, gx + 345, gy + 340], fill=(205, 160, 100),
                outline=BLACK, width=5)
    d.line([(gx + 140, gy + 265), (gx + 345, gy + 265)], fill=BLACK, width=4)
    d.text((gx + 156, gy + 288), "make.fun", font=font(28), fill=BLACK)
    # floor line + bottom punchline
    d.rectangle([0, 940, W, 950], fill=(60, 64, 100))
    text_center(d, 990, "212 GB.", font(96), WHITE)
    text_center(d, 1090, "WORTH IT.", font(96), YELLOW)
    img.save(f"{OUT}/meme-b.png")


# ---------------------------------------------------------------- C: anjing jet ski
def meme_c():
    img = Image.new("RGB", (W, H), (0, 0, 0))
    grad = Image.new("RGB", (W, H), (0, 0, 0))
    gradient(grad, (255, 170, 100), (20, 90, 140))
    img.paste(grad, (0, 0))
    d = ImageDraw.Draw(img)
    # sun top-right, clear of the headline; one cloud far left only
    d.ellipse([920, 150, 1140, 370], fill=(255, 225, 140), outline=BLACK, width=5)
    d.ellipse([150, 170, 330, 230], fill=(255, 235, 220))
    # sea
    d.rectangle([0, 620, W, H], fill=(16, 110, 150))
    for y in (700, 800, 900, 1010, 1120):
        for x in range(0, W, 120):
            d.arc([x, y, x + 90, y + 34], 0, 180, fill=(120, 210, 235), width=6)
    # jet ski: hull (nose right) + deck + seat
    d.polygon([(250, 880), (950, 880), (1020, 940), (900, 990), (300, 990),
               (220, 930)], fill=(255, 90, 90), outline=BLACK, width=6)
    d.polygon([(250, 880), (950, 880), (930, 840), (280, 840)],
              fill=(200, 40, 40), outline=BLACK, width=5)
    d.rectangle([560, 800, 820, 845], fill=(30, 30, 40), outline=BLACK, width=4)
    # spray behind the ski (small scattered drops, rear-left)
    for i, (sx, sy, r) in enumerate([(150, 900, 9), (185, 925, 7), (220, 895, 8),
                                     (130, 940, 7), (170, 960, 8), (205, 945, 6),
                                     (250, 920, 7), (110, 915, 6)]):
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=WHITE)
    # ghost riding BEHIND (left), sitting on the seat, coin in hand
    gx, gy, gs = 430, 520, 300
    ghost(img, gx, gy, gs)
    d = ImageDraw.Draw(img)
    # dog at the FRONT (right), clean side profile facing right:
    # horizontal body, head above the front, floppy ear, snout + nose,
    # tail flicking up at the rear, front leg reaching the handlebar
    # tail: thick line up-left from the rear of the body + round tip
    d.line([(772, 712), (738, 642)], fill=(150, 95, 50), width=16)
    d.ellipse([722, 626, 754, 658], fill=(150, 95, 50), outline=BLACK, width=3)
    # body + haunch
    d.ellipse([760, 680, 980, 850], fill=(150, 95, 50), outline=BLACK, width=5)
    d.ellipse([775, 780, 865, 862], fill=(150, 95, 50), outline=BLACK, width=4)
    # head, floppy ear hanging down the rear of the head, snout, nose, eye
    d.ellipse([880, 570, 1000, 690], fill=(150, 95, 50), outline=BLACK, width=5)
    d.ellipse([885, 585, 932, 692], fill=(110, 65, 30), outline=BLACK, width=4)
    d.ellipse([960, 620, 1032, 678], fill=(150, 95, 50), outline=BLACK, width=4)
    d.ellipse([1012, 636, 1032, 662], fill=BLACK)  # nose
    d.ellipse([922, 612, 944, 634], fill=BLACK)  # eye
    # front leg stretched to the handlebar
    d.line([(950, 820), (1002, 852)], fill=(150, 95, 50), width=20)
    # handlebar in FRONT of the dog, drawn last so it reads as held
    d.line([(1005, 852), (1010, 755)], fill=BLACK, width=12)
    d.line([(1010, 755), (1055, 755)], fill=BLACK, width=12)
    # headline + punchline
    text_center(d, 30, "WAITED 13 YEARS", font(84), WHITE)
    text_center(d, 122, "FOR GTA 6", font(84), YELLOW)
    text_center(d, 1040, "10 HOURS IN. MISSIONS: 0.", font(64), WHITE)
    img.save(f"{OUT}/meme-c.png")


if __name__ == "__main__":
    meme_a()
    meme_b()
    meme_c()
    print("done: meme-a.png, meme-b.png, meme-c.png")
