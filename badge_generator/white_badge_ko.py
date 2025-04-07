import svgwrite

def create_svg(data):
    # 뱃지 전체 크기 설정
    stats = [
        ("BOJ Handle", data[0]),
        ("만든 문제", str(data[1])),
        ("검수한 문제", str(data[2])),
        ("공헌한 문제", str(data[3])),
        ("난이도 기여", str(data[4]))
    ]
    width = 467
    height = 195
    dwg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
    
    # 배경: 흰색 배경
    bg_rect = dwg.rect(
        insert=(0, 0),
        size=(width, height),
        rx=10,  # 라운드 모서리
        ry=10,
        fill="#FFFFFF"  # 흰색 배경
    )

    dwg.add(bg_rect)
    
    # 타이틀 텍스트
    title = f"{stats[0][1]}'s LeetCode Stats"
    dwg.add(dwg.text(
        title,
        insert=(20, 30),
        fill="#E84DFF",
        font_size="18px",
        font_weight="bold"
    ))
    
    # 통계 항목들을 위한 시작 위치와 줄 간격 설정
    start_y = 80
    line_height = 35
    
    
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
            fill="black",
            font_size="14px",
            #font_family="Arial, sans-serif"
            font_weight="bold"
        ))
        # 값 텍스트 (오른쪽 정렬)
        dwg.add(dwg.text(
            value,
            insert=(width // 2, y),
            fill="black",
            font_size="14px",
            #font_family="Arial, sans-serif"
            font_weight="bold"
        ))
    return dwg.tostring()
