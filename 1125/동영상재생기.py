def solution(video_len, pos, op_start, op_end, commands):
    def 시간변환(d):
        분,초 = map(int, d.split(":"))
        return 60*분+초
    
    video_len = 시간변환(video_len)
    start = 시간변환(pos)
    op_start = 시간변환(op_start)
    op_end = 시간변환(op_end)
    
    if op_start <= start <= op_end:
        start = op_end

    for i in commands:
        if i == "next":
            start = min(start+10, video_len)
        elif i == "prev":
            start = max(start - 10, 0)

        if op_start <= start <= op_end:
            start = op_end
            
    분 = start//60
    초 = start%60
    answer = f"{분:02d}:{초:02d}"
    return answer
        
print(solution(
    "07:22", "04:05", "00:15", "04:07",
    ["next"]
))