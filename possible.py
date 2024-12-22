
def possible_list(number: int, data: list[int]) -> float:
    return f'chance: {data.count(number) / len(data) * 100:.1f} %'


def possible_string_self(letter: str, word: str) -> float:
    return f'chance: {word.count(letter) / len(word) * 100:.1f} %'

