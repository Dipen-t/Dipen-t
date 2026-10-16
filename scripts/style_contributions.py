"""Restyle generated contribution data as a focused, horizontal 3D calendar."""
import re
from pathlib import Path
import xml.etree.ElementTree as ET

NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
def tag(name):
    return f"{{{NS}}}{name}"

source = ET.parse("profile-3d-contrib/profile-night-view.svg").getroot()
calendar = next(e for e in source if e.tag == tag("g") and len(e) > 300)
assert 350 <= len(calendar) <= 371, "Unexpected calendar format; keep existing artwork"
summary = " ".join(source.itertext())
match = re.search(r"(\d+) contributions", summary)
assert match, "Contribution count missing"
total = match.group(1)
dates = re.search(r"(\d{4}-\d{2}-\d{2}) / (\d{4}-\d{2}-\d{2})", summary)
assert dates, "Calendar period missing"
for parent in calendar.iter():
    for child in list(parent):
        if child.tag in (tag("animate"), tag("animateTransform")):
            parent.remove(child)

for theme in ("dark", "light"):
    dark = theme == "dark"
    bg, fg, muted = ("#0d1117", "#dce8f8", "#8b9db5") if dark else ("#ffffff", "#182d48", "#60758f")
    colors = [
        ("#1d2a3b", "#172232", "#131d2c") if dark else ("#e7edf5", "#d7e1ee", "#c8d5e6"),
        ("#4475a9", "#345b85", "#284666"),
        ("#568fd0", "#3f6fa4", "#30567f"),
        ("#72b6ea", "#528fbc", "#3c7199"),
        ("#97d9ef", "#6eb0c8", "#508aab"),
    ]
    root = ET.Element(tag("svg"), {"width":"1280","height":"380","viewBox":"0 0 1280 380","role":"img","aria-labelledby":"title desc"})
    ET.SubElement(root, tag("title"), {"id":"title"}).text = "A year of GitHub contributions"
    ET.SubElement(root, tag("desc"), {"id":"desc"}).text = f"{total} contributions from {dates[1]} to {dates[2]}. Each block represents a day; height and color reflect activity."
    css = "*{font-family:Segoe UI,Arial,sans-serif}.fill-strong{fill:#97d9ef}"
    for i, palette in enumerate(colors):
        for face, color in zip(("top","left","right"), palette):
            css += f".cont-{face}-{i}{{fill:{color}}}"
    ET.SubElement(root, tag("style")).text = css
    ET.SubElement(root, tag("rect"), {"width":"1280","height":"380","fill":bg})
    ET.SubElement(root, tag("text"), {"x":"28","y":"40","fill":fg,"font-size":"27","font-weight":"600"}).text = f"{int(total):,} contributions"
    ET.SubElement(root, tag("text"), {"x":"1252","y":"40","fill":muted,"font-size":"19","text-anchor":"end"}).text = f"{dates[1]} — {dates[2]}"
    group = ET.SubElement(root, tag("g"), {"transform":"translate(14 76) matrix(1 -0.57735 0 1 0 0)"})
    # Serialize/parse to copy the source calendar without altering its measured heights.
    group.append(ET.fromstring(ET.tostring(calendar)))
    ET.SubElement(root, tag("text"), {"x":"28","y":"354","fill":muted,"font-size":"19"}).text = "Earlier"
    ET.SubElement(root, tag("text"), {"x":"1252","y":"354","fill":muted,"font-size":"19","text-anchor":"end"}).text = "Recent"
    Path("assets").mkdir(exist_ok=True)
    ET.ElementTree(root).write(f"assets/contributions-{theme}.svg", encoding="unicode")
