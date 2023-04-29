from modules.base_module import BaseClass


class ClassOne(BaseClass):
    def say_fuck_you(self, s: str) -> str:
        return f'fuck you {s} - module_one.py'


def say_fuck_you_two(s: str) -> str:
    return f'fuck you {s} - module_one.py'
