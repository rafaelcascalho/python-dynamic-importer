from dynamic_importer import (
    run_importer,
    ComponentType,
    ModuleComponent
)


def run_tests():
    modules_components = run_importer()

    classes = [
        comp for comp in modules_components
        if comp.component_type == ComponentType.CLASS
    ]
    test_classes_components(classes=classes)

    functions = [
        comp for comp in modules_components
        if comp.component_type == ComponentType.FUNCTION
    ]
    test_functions_components(functions=functions)

    print('TEST_RESULT: All tests passed!')


def test_classes_components(
    classes: list[ModuleComponent]
) -> tuple[int, list[str]]:
    arg_test = 'abc'

    for class_component in classes:
        cls = class_component.component
        expected = f'fuck you {arg_test} - {class_component.module_name}'

        result = cls().say_fuck_you(s=arg_test)

        assert result == expected


def test_functions_components(
    functions: list[ModuleComponent]
) -> tuple[int, list[str]]:
    arg_test = 'abc'

    for function_component in functions:
        function = function_component.component
        expected = f'fuck you {arg_test} - {function_component.module_name}'

        result = function(s=arg_test)

        assert result == expected


run_tests()
