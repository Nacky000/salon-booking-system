def generate_times(start="09:00", end="18:00", step=30):
    """予約可能な時間リストを生成する(30分刻み)"""

    def to_minutes(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    def to_time(mins):
        h = mins // 60
        m = mins % 60
        return f"{h:02d}:{m:02d}"

    start_min = to_minutes(start)
    end_min = to_minutes(end)

    times = []

    current = start_min
    while current < end_min: # 18:00は開始できない
        times.append(to_time(current))
        current += step

    return times