from modules.base_module import BaseClass


class ClassTwo(BaseClass):
    def say_fuck_you(self, s: str) -> str:
        return f'fuck you {s} - module_two.py'


def say_fuck_you_one(s: str) -> str:
    return f'fuck you {s} - module_two.py'
