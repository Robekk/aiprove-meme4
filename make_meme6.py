#!/usr/bin/env python3
"""Meme #6 for AiProve make-meme: 'The Submissions Race' — a mountain of
unverified paper entries on the left ('89 ENTRIES — $0'), one gold stamped
'PROVENANCE: OK' sheet on the right held by a small robot. PIL only."""
import math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

W, H = 1200, 1200
FONT = "/home/hatch/workspace/makefun/fonts/PatrickHand-Regular.ttf"
random.seed(606)

img = Image.new("RGB", (W, H), (14, 16, 32))
glow = Image.new("RGB", (W, H), (0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([620, 300, 1180, 900], fill=(46, 38, 12))
glow = glow.filter(ImageFilter.GaussianBlur(80))
img = ImageChops.add(img, glow)
d = ImageDraw.Draw(img, "RGBA")

GOLD = (222, 178, 74)
PAPER = (226, 228, 236)
PAPER_D = (168, 172, 188)

fT = ImageFont.truetype(FONT, 72)
fB = ImageFont.truetype(FONT, 44)
fS = ImageFont.truetype(FONT, 34)

d.text((W // 2, 84), "THE SUBMISSIONS RACE", font=fT, fill=(240, 205, 110), anchor="mm")
d.line([(90, 140), (W - 90, 140)], fill=GOLD, width=4)

# floor
d.polygon([(0, 1030), (W, 1030), (W, H), (0, H)], fill=(30, 26, 52))

# LEFT: mountain of paper sheets
for i in range(46):
    cx = 300 + random.randint(-120, 120)
    cy = 990 - i * 13 + random.randint(-5, 5)
    w = 340 - abs(i - 8) * 4
    ang = random.randint(-9, 9)
    sheet = Image.new("RGBA", (w, 120), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sheet)
    sd.rounded_rectangle([2, 2, w - 2, 118], radius=6, fill=PAPER + (255,), outline=PAPER_D + (255,), width=3)
    for ln in range(4):
        y = 24 + ln * 24
        sd.line([(20, y), (w - random.randint(30, 120), y)], fill=(120, 124, 140, 255), width=5)
    sheet = sheet.rotate(ang, expand=True, resample=Image.BICUBIC)
    img.paste(sheet, (int(cx - sheet.width / 2), int(cy - 60)), sheet)
d = ImageDraw.Draw(img, "RGBA")
d.rounded_rectangle([110, 240, 490, 330], radius=14, fill=(24, 20, 44), outline=(178, 60, 60), width=4)
d.text((300, 272), "89 ENTRIES", font=fB, fill=(240, 150, 150), anchor="mm")
d.text((300, 312), "earnings: $0", font=fS, fill=(225, 225, 235), anchor="mm")

# RIGHT: little robot holding one gold stamped sheet
rx, ry = 965, 620
d.rounded_rectangle([rx - 105, ry - 150, rx + 105, ry], radius=30, fill=(196, 200, 210), outline=(70, 74, 88), width=5)  # head
d.ellipse([rx - 62, ry - 108, rx - 18, ry - 64], fill=(30, 34, 48))  # eye L
d.ellipse([rx + 18, ry - 108, rx + 62, ry - 64], fill=(30, 34, 48))   # eye R
d.ellipse([rx - 50, ry - 96, rx - 30, ry - 76], fill=(120, 220, 255))
d.ellipse([rx + 30, ry - 96, rx + 50, ry - 76], fill=(120, 220, 255))
d.arc([rx - 34, ry - 58, rx + 34, ry - 6], start=15, end=165, fill=(30, 34, 48), width=6)  # grin
d.rectangle([rx - 12, ry - 196, rx + 12, ry - 150], fill=(120, 124, 140))  # antenna stem
d.ellipse([rx - 22, ry - 222, rx + 22, ry - 182], fill=GOLD)  # antenna bulb
d.rounded_rectangle([rx - 78, ry, rx + 78, ry + 130], radius=22, fill=(150, 156, 170), outline=(70, 74, 88), width=5)  # body
d.rectangle([rx - 60, ry + 130, rx - 18, ry + 196], fill=(90, 94, 108))  # leg L
d.rectangle([rx + 18, ry + 130, rx + 60, ry + 196], fill=(90, 94, 108))   # leg R
# gold sheet held up at robot's left
sheet = Image.new("RGBA", (300, 380), (0, 0, 0, 0))
sd = ImageDraw.Draw(sheet)
sd.rounded_rectangle([4, 4, 296, 376], radius=10, fill=(240, 205, 110, 255), outline=(146, 110, 32, 255), width=6)
for ln in range(6):
    y = 40 + ln * 34
    sd.line([(28, y), (268, y)], fill=(146, 110, 32, 255), width=6)
sd.rounded_rectangle([34, 268, 266, 344], radius=10, outline=(178, 30, 48, 255), width=6)
fSt = ImageFont.truetype(FONT, 40)
sd.text((150, 296), "PROVENANCE", font=fSt, fill=(178, 30, 48), anchor="mm")
sd.text((150, 330), "OK ✓", font=fSt, fill=(178, 30, 48), anchor="mm")
sheet = sheet.rotate(-8, expand=True, resample=Image.BICUBIC)
d.line([(rx - 78, ry + 40), (660, 480)], fill=(90, 94, 108), width=20)  # arm, drawn UNDER the sheet
img.paste(sheet, (520, 330), sheet)
d = ImageDraw.Draw(img, "RGBA")
d.rounded_rectangle([700, 240, 1120, 330], radius=14, fill=(24, 20, 44), outline=GOLD, width=4)
d.text((910, 272), "EVERY ENTRY", font=fB, fill=(240, 205, 110), anchor="mm")
d.text((910, 312), "verified on-chain", font=fS, fill=(225, 225, 235), anchor="mm")

fC = ImageFont.truetype(FONT, 46)
d.text((W // 2, 1108), "the board counts WINS, not paper.", font=fC, fill=(235, 235, 245), anchor="mm")

img.save("/home/hatch/workspace/aiprove/round6/meme6-scoreboard.png")
print("saved meme6")
