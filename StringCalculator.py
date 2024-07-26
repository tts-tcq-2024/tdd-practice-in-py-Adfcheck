def add(numbers):
    if not numbers:
        return 0

    if numbers.startswith('//'):
        delimiter_end = numbers.find('\n')
        delimiter = numbers[2:delimiter_end]
        numbers = numbers[delimiter_end + 1:]
    else:
        delimiter = ',|\n'

    import re
    numbers = re.sub(f"[{re.escape(delimiter)}]", ',', numbers)

    number_list = list(map(int, numbers.split(',')))

    negatives = [num for num in number_list if num < 0]
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

    number_list = [num for num in number_list if num <= 1000]

    return sum(number_list)

