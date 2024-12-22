
def possible_list(number: int, data: list[int]) -> float:
    return f'chance: {data.count(number) / len(data) * 100:.1f} %'
