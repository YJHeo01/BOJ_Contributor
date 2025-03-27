import svgwrite

def create_svg():
    dwg = svgwrite.Drawing(size=("300px", "100px"))
    dwg.add(dwg.text("sk14cj", insert=(10, 20), fill="black", font_size="16px"))
    dwg.add(dwg.text("문제 제작: 3", insert=(10, 50), fill="black", font_size="14px"))
    dwg.add(dwg.text("문제 검수: 5", insert=(150, 50), fill="black", font_size="14px"))
    dwg.add(dwg.text("오류 제보: 0", insert=(10, 75), fill="black", font_size="14px"))
    dwg.add(dwg.text("난이도 기여: 133", insert=(150, 75), fill="black", font_size="14px"))
    return dwg.tostring()
