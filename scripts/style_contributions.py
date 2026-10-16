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
        ("#25263e", "#191b2d", "#121421") if dark else ("#eeedf8", "#d8d7e8", "#c1c1d8"),
        ("#6f7bf2", "#424db2", "#282f73"),
        ("#9a86fb", "#6750c4", "#3d2d83"),
        ("#c5a4ff", "#8b62cf", "#55388d"),
        ("#b3f8e1", "#59bca2", "#2a786e"),
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
    defs = ET.SubElement(root, tag("defs"))
    cast_filter = ET.SubElement(defs, tag("filter"), {"id":"cast-shadow","x":"-50%","y":"-100%","width":"250%","height":"300%","color-interpolation-filters":"sRGB"})
    ET.SubElement(cast_filter, tag("feGaussianBlur"), {"stdDeviation":"2"})
    platform_filter = ET.SubElement(defs, tag("filter"), {"id":"platform-shadow","x":"-10%","y":"-50%","width":"125%","height":"220%","color-interpolation-filters":"sRGB"})
    ET.SubElement(platform_filter, tag("feDropShadow"), {"dx":"7","dy":"14","stdDeviation":"10","flood-color":"#050511","flood-opacity":".55" if dark else ".22"})
    for i, palette in enumerate(colors):
        for face, color in zip(("left","right"), palette[1:]):
            gradient = ET.SubElement(defs, tag("linearGradient"), {"id":f"{face}-{i}","x1":"0","y1":"0","x2":"0.2","y2":"1"})
            ET.SubElement(gradient, tag("stop"), {"offset":"0","stop-color":color})
            ET.SubElement(gradient, tag("stop"), {"offset":"1","stop-color":color,"stop-opacity":".68"})
    projection = "translate(14 76) matrix(1 -0.57735 0 1 0 0)"
    ground = ET.SubElement(root, tag("g"), {"transform":projection,"filter":"url(#platform-shadow)"})
    zero = next(cell for cell in calendar if any(e.get("class") == "cont-top-0" for e in cell))
    active = []
    for cell in calendar:
        x, y = map(float, re.search(r"translate\(([-\d.]+) ([-\d.]+)\)", cell.get("transform")).groups())
        side = next(e for e in cell if e.get("class", "").startswith("cont-left-"))
        height = float(side.get("height")) * 1.15
        base = ET.fromstring(ET.tostring(zero))
        base.set("transform", f"translate({x} {y + height - 2.99})")
        ground.append(base)
        if any(e.get("class") == "cont-top-0" for e in cell):
            continue
        active.append((cell, x, y, height))
    shadows = ET.SubElement(root, tag("g"), {"fill":"#030411","opacity":".72" if dark else ".32","filter":"url(#cast-shadow)"})
    for cell, x, y, height in active:
        px, py = x + 14, y - .57735*x + 76 + height
        length = max(9, height * .9)
        points = [(px,py),(px+18,py-20.8),(px+36+length,py-20.8+length*.2),(px+18+length,py+length*.2)]
        ET.SubElement(shadows, tag("polygon"), {"points":" ".join(f"{a:.2f},{b:.2f}" for a,b in points)})
    group = ET.SubElement(root, tag("g"), {"transform":projection})
    for cell, x, y, height in active:
        block = ET.fromstring(ET.tostring(cell))
        for face in block:
            cls = face.get("class", "")
            if cls.startswith("cont-top-"):
                face.set("stroke", "#ffffff")
                face.set("stroke-opacity", ".24")
                face.set("stroke-width", ".65")
            elif cls.startswith(("cont-left-", "cont-right-")):
                name, level = cls.removeprefix("cont-").rsplit("-", 1)
                face.set("style", f"fill:url(#{name}-{level})")
        group.append(block)
    ET.SubElement(root, tag("text"), {"x":"28","y":"354","fill":muted,"font-size":"19"}).text = "Earlier"
    ET.SubElement(root, tag("text"), {"x":"1252","y":"354","fill":muted,"font-size":"19","text-anchor":"end"}).text = "Recent"
    Path("assets").mkdir(exist_ok=True)
    ET.ElementTree(root).write(f"assets/contributions-{theme}.svg", encoding="unicode")
