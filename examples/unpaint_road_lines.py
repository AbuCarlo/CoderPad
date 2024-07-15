x = (3, 10, 14, 20, 1, 5)
y = (1, 7, 1, 7, 1, 11, 1, 7, 1, 7)


def coalesce(l):
    if len(l) == 0:
        return []
    intervals = [[l[i * 2], l[i * 2 + 1]] for i in range(len(l) // 2)]
    intervals.sort(key = lambda i: i[0])
    current = intervals[0]
    result = []
    for i in intervals[1:]:
        if i[0] <= current[1]:
            current[1] = max(current[1], i[1])
        else:
            result.append(current)
            current = i
    result.append(current)
    return result

def analyze(l):
    if len(l) == 0:
        return []
    intervals = [[l[i * 2], l[i * 2 + 1]] for i in range(len(l) // 2)]
    events = {}
    for i in intervals:
        events[i[0]] = events.get(i[0], 0) + 1
        events[i[1]] = events.get(i[1], 0) - 1
    times = sorted(events.keys())
    result = []
    start = times[0]
    thickness = events[start]
    for t in times[1:]:
        result.append((thickness, start, t))
        thickness += events[t]
        start = t
    return result

print(coalesce(x))
print(coalesce(y))

print(analyze(y))
