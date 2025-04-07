import svgwrite

def create_svg(data):
    # 뱃지 전체 크기 설정
    stats = {
        "Solved Problem": '0',
        "Created Problem": str(data[1]),
        "Reviewed Problem": str(data[2]),
        "Fixed Problem": str(data[3]),
        "Difficulty Poll": str(data[4])
    }

    width = 467
    height = 195
    dwg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
    
    # 배경
    bg_rect = dwg.rect(
        insert=(0, 0),
        size=(width, height),
        rx=10,  # 라운드 모서리
        ry=10,
        fill="#111111"
    )

    dwg.add(bg_rect)
    
    # 타이틀 텍스트
    title = f"{data[0]}'s Baekjoon Stats"
    dwg.add(dwg.text(
        title,
        insert=(20, 30),
        fill="#E84DFF",
        font_size="18px",
        font_weight="bold"
    ))
    
    # 통계 항목들을 위한 시작 위치와 줄 간격 설정
    start_y = 60
    line_height = 25
    
    # 각 통계 항목을 텍스트로 추가 (왼쪽: 라벨, 오른쪽: 값)
    for i, label in enumerate(stats):
        y = start_y + i * line_height
        # 라벨 텍스트
        dwg.add(dwg.text(
            f"{label}:",
            insert=(20, y),
            fill="white",
            font_size="14px",
            #font_family="Arial, sans-serif"
            font_weight="bold"
        ))
        # 값 텍스트
        dwg.add(dwg.text(
            stats[label],
            insert=(width // 2, y),
            fill="white",
            font_size="14px",
            #font_family="Arial, sans-serif"
            font_weight="bold"
        ))
    return dwg.tostring()
