import svgwrite

def create_svg(data):
    """
    data: 리스트 형식의 정보
      data[0]: 뱃지 타이틀 (예: "BOJ Contributor")
      data[1]: "문제 제작" 횟수 또는 관련 정보
      data[2]: "문제 검수" 횟수 또는 관련 정보
      data[4]: "난이도 기여" 횟수 또는 관련 정보
    """
    # 뱃지 크기 설정 (GitHub 뱃지 스타일)
    width, height = 350, 170
    dwg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
    
    # 배경 그라데이션 정의 (위에서 아래로)
    gradient = dwg.linearGradient(start=(0, 0), end=(0, 1), id="grad")
    gradient.add_stop_color(0, "#99ccff")  # 연한 블루
    gradient.add_stop_color(1, "#3399ff")  # 진한 블루
    dwg.defs.add(gradient)
    
    # 드롭 섀도우 필터 정의 (그림자 효과)
    shadow = dwg.defs.add(dwg.filter(id="shadow", filterUnits="userSpaceOnUse"))
    shadow.feOffset(in_="SourceAlpha", dx=2, dy=2, result="offOut")
    shadow.feGaussianBlur(in_="offOut", stdDeviation=2, result="blurOut")
    shadow.feBlend(in_="SourceGraphic", in2="blurOut", mode="normal")
    
    # 라운드된 사각형 배경 추가 (드롭 섀도우 적용)
    rect = dwg.rect(insert=(0, 0), size=(width, height), rx=10, ry=10, fill=f"url(#{gradient.get_id()})")
    rect.update({'filter': 'url(#shadow)'})
    dwg.add(rect)
    
    # 텍스트 스타일 설정 (폰트 및 색상)
    dwg.defs.add(dwg.style("text { font-family: 'Noto Sans KR', 'Arial', sans-serif; fill: white; }"))
    
    # 뱃지 타이틀 (중앙 정렬)
    dwg.add(dwg.text(data[0], insert=(width / 2, 30), text_anchor="middle", font_size="20px", font_weight="bold"))
    
    # 두 개의 정보를 좌/우 열에 배치
    dwg.add(dwg.text("문제 제작: " + str(data[1]), insert=(20, 60), font_size="14px"))
    dwg.add(dwg.text("문제 검수: " + str(data[2]), insert=(width / 2 + 10, 60), font_size="14px"))
    dwg.add(dwg.text("BOJ Contributor", insert=(20, 100), font_size="14px"))
    # 하단 우측에 난이도 기여 정보 배치
    dwg.add(dwg.text("난이도 기여: " + str(data[4]), insert=(width / 2 + 10, 100), font_size="14px"))
    
    return dwg.tostring()
