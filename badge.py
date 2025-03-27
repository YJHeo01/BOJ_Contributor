import svgwrite

def create_svg(data):
    dwg = svgwrite.Drawing(size=("350px", "170px"))
    dwg.defs.add(dwg.style("text { font-family: 'Nanum Gothic', 'Arial', sans-serif; }"))
    dwg.add(dwg.text(data[0], insert=(10, 20), fill="black", font_size="16px"))
    dwg.add(dwg.text("문제 제작   :   "+str(data[1]), insert=(10, 50), fill="black", font_size="14px"))
    dwg.add(dwg.text("문제 검수   :   "+str(data[2]), insert=(150, 50), fill="black", font_size="14px"))
    dwg.add(dwg.text("BOJ Contributor", insert=(10, 75), fill="black", font_size="14px"))
    #dwg.add(dwg.text("오류 제보: " +str(data[4]), insert=(10, 75), fill="black", font_size="14px"))
    dwg.add(dwg.text("난이도 기여   :   "+str(data[3]), insert=(150, 75), fill="black", font_size="14px"))
    return dwg.tostring()
