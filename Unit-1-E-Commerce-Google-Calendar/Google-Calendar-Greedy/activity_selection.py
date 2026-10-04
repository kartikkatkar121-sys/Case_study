def select_events(events):
    events = sorted(events, key=lambda event: event[2])
    selected = []
    last_finish = -1

    for name, start, finish in events:
        if start >= last_finish:
            selected.append((name, start, finish))
            last_finish = finish
    return selected


if __name__ == "__main__":
    events = [
        ("DSA Lecture", 9, 10),
        ("Team Meeting", 9, 11),
        ("Project Work", 10, 12),
        ("Lunch", 12, 13),
        ("Lab Session", 13, 15),
        ("AIML Class", 14, 16),
        ("Revision", 15, 17),
    ]

    print("Selected Calendar Events:")
    for name, start, finish in select_events(events):
        print(f"{start}:00 - {finish}:00  {name}")
