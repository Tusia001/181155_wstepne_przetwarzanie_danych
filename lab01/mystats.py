def median(data):
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


def trimmed_mean(data, p):
    if not 0 <= p < 0.5:
        raise ValueError("Parametr p musi być między 0 a 0.5")
    n = len(data)
    sorted_data = sorted(data)
    k = int(n * p)
    trimmed_data = sorted_data[k: n - k]
    return sum(trimmed_data) / len(trimmed_data)