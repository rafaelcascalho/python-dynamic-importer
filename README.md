# Dynamic Importer

This project is a simple reusable dynamic importer of python modules components such as classes and functions.

## Concepts

- Module Component: a callable of a module

## Current supported module components

- Classes
- functions

## Prerequisites

Python 3.10.7+

## Usage

Basic usage

```py
# import the dynamic importer run_importer function
from dynamic_importer import run_importer, ComponentType

# get the result from the method
# use a custom path, or the default will be a 'modules' folder in the root of the project
modules_components = run_importer(path='custom-modules-path')

# run the module components at your own will
for module_component in modules_components:
    if module_component.component_type == ComponentType.FUNCTION:
        func = module_component.component
        func(**kwargs)  # the kwargs here just represent whatever arguments you want to pass with it
    elif module_component.component_type == ComponentType.CLASS:
        cls = module_component.component
        obj = cls(**kwargs)  # the kwargs here just represent whatever arguments you want to pass with it
        obj.method(**kwargs)  # the kwargs here just represent whatever arguments you want to pass with it
```

In the modules folder, there is a `BaseClass` that extends an abstract class, and creates the base of the classes
to be implemented. Just add new methods with `classmethod` decorator to add new methods that will required to be
implemented in this class.

## Tests

To run the existent tests just run the tests file with the command

```sh
$ python dynamic_importer_tests.py
```

## Security

This dynamic import creates a possible security breach of new malicious files been placed in your modules folder.
To try to avoid it, change the folder name - check the usage, and run in an isolated manner inside the machine,
requiring as many authentication steps as possible. That said, use at your own risk :)
