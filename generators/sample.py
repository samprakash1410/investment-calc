def odd_numbers(start, end):
    results = []
    for number in range(start, end+1):
        if number%2 != 0:
            results.append(number)
    return results