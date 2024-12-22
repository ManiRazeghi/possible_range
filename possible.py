
class Possible:

    def possible_int_str(self, target: int|str, data: list[int]|str) -> float:
        return f'chance: {data.count(target) / len(data) * 100:.1f} %'




