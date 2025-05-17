def gotintothattxt(s, text):
    if not s or not text:
        return 0

    n = len(s)
    total = 0

    for shift in range(n):
        current_shift = s[shift:] + s[:shift]
        pos = 0
        while True:
            pos = text.find(current_shift, pos)
            if pos == -1:
                break
            total += 1
            pos += 1

    return total

test_pattern = "abab"
test_text = "abababababab"
result = gotintothattxt(test_pattern, test_text)
print(f"Найдено совпадений: {result}")