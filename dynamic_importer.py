from abc import ABC, abstractmethod
from enum import Enum
from os import listdir
from os.path import isdir
from typing import Callable, Any
from dataclasses import dataclass
from importlib.machinery import SourceFileLoader
from importlib.util import spec_from_loader, module_from_spec
from inspect import getmembers, isclass, isfunction, isabstract


NAME = 0
CLASSIFICATION = 1


class ComponentType(Enum):
    CLASS = 'class'
    FUNCTION = 'function'


@dataclass
class ModuleComponent:
    module_name: str
    module_path: str
    component: Callable
    component_type: ComponentType


def mount_module_path(path: str, module_name: str) -> str:
    return f'{path}/{module_name}'


def import_and_load_module(module_path: str, module_name: str):
    """
    Follows the steps to load a python file as a module.
    Currently these are:
        1. Creates a Loader for the python file
        2. Create a Spec from that loader
        3. Create a module from that spec
        4. Loads that module using the Loader
    This way the loaded modules allow for extraction of their components,
    such as classes and functions, and calling of those as well.

    Args:
        module_path : the path to that module
        module_name : name of the module

    Returns:
        the loaded module
    """
    loader = SourceFileLoader(fullname=module_name, path=module_path)
    spec = spec_from_loader(name=module_name, loader=loader)
    module = module_from_spec(spec=spec)
    loader.exec_module(module=module)
    return module


def list_classes_and_functions(module) -> tuple[list[Any], list[Any]]:
    """
    Filters modules components based on their desired types.

    Args:
        module : already loaded module

    Returns:
        a list of each component type.
    """    
    return (
        [
            item for item in getmembers(module)
            if isclass(item[CLASSIFICATION])
        ],
        [
            item for item in getmembers(module)
            if isfunction(item[CLASSIFICATION])
        ]
    )


def extract_functions_from_module(
    module: Any,
    functions: list[Any],
    module_path: str,
    module_name: str
):
    valid_functions = []

    for func_tuple in functions:
        func = getattr(module, func_tuple[NAME])
        if func is abstractmethod:
            continue

        valid_functions.append(
            ModuleComponent(
                module_name=module_name,
                module_path=module_path,
                component=func,
                component_type=ComponentType.FUNCTION,
            )
        )

    return valid_functions


def extract_classes_from_module(
    module: Any,
    classes: list[Any],
    module_path: str,
    module_name: str
) -> list[Any]:
    concrete_classes = []
    for cls_tuple in classes:
        cls = getattr(module, cls_tuple[NAME])
        if isabstract(cls) or cls is ABC:
            continue

        concrete_classes.append(
            ModuleComponent(
                module_name=module_name,
                module_path=module_path,
                component=cls,
                component_type=ComponentType.CLASS,
            )
        )

    return concrete_classes


def run_importer(path: str = './modules') -> list[ModuleComponent]:
    modules_components = []
    modules_names = [item for item in listdir(path=path) if not isdir(item)]

    for module_name in modules_names:
        module_path = mount_module_path(path=path, module_name=module_name)
        module = import_and_load_module(
            module_path=module_path,
            module_name=module_name
        )
        classes, functions = list_classes_and_functions(module=module)
        modules_components.extend(
            [
                *extract_classes_from_module(
                    module=module,
                    classes=classes,
                    module_path=module_path,
                    module_name=module_name
                ),
                *extract_functions_from_module(
                    module=module,
                    functions=functions,
                    module_path=module_path,
                    module_name=module_name
                )
            ]
        )

    return modules_components


if __name__ == "__main__":
    run_importer()
