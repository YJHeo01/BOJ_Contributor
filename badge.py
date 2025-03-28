import svgwrite

def create_svg(data):
    # 뱃지 전체 크기 설정
    width = 400
    height = 280
    dwg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
    
    # 배경: 다크 모던 느낌의 어두운 그레이 색상과 둥근 모서리
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), rx=20, ry=20, fill='#2C2F33'))
    
    # 타이틀 텍스트 (중앙 정렬)
    title = "BOJ Contribute Stat"
    dwg.add(dwg.text(
        title,
        insert=(width / 2, 40),
        text_anchor="middle",
        fill="white",
        font_size="24px",
        font_family="Arial, sans-serif",
        font_weight="bold"
    ))
    
    # 통계 항목들을 위한 시작 위치와 줄 간격 설정
    start_y = 80
    line_height = 35
    
    stats = [
        ("BOJ Handle", data[0]),
        ("만든 문제", str(data[1])),
        ("검수한 문제", str(data[2])),
        ("공헌한 문제", str(data[3])),
        ("난이도 기여", str(data[4]))
    ]
    
    # 좌측과 우측 영역을 나누는 기준 x좌표 (라인 추가)
    split_x = width * 0.5
    # 수직 구분선 (액센트 컬러)
    dwg.add(dwg.line(start=(split_x, start_y - 20), 
                     end=(split_x, start_y + len(stats) * line_height - 10),
                     stroke="#7289DA", stroke_width=2))
    
    # 각 통계 항목을 텍스트로 추가 (왼쪽: 라벨, 오른쪽: 값)
    for i, (label, value) in enumerate(stats):
        y = start_y + i * line_height
        # 라벨 텍스트
        dwg.add(dwg.text(
            f"{label}:",
            insert=(20, y),
            fill="white",
            font_size="18px",
            font_family="Arial, sans-serif"
        ))
        # 값 텍스트 (오른쪽 정렬)
        dwg.add(dwg.text(
            value,
            insert=(width - 20, y),
            text_anchor="end",
            fill="white",
            font_size="18px",
            font_family="Arial, sans-serif"
        ))
    
    return dwg.tostring()
