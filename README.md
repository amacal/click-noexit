# click-noexit

A utility for the Click command-line interface library that prevents commands from exiting the application directly. Instead, it allows commands to return exit codes for improved control and handling in larger applications.

## Introduction

`click-noexit` is a decorator for Click commands designed to suppress the default behavior of exiting the application upon command completion or when an error occurs. This is particularly useful when integrating Click commands into larger applications, where you want to handle exits and exceptions more gracefully.

## Installation

Install `click-noexit` using pip:

```bash
pip install click-noexit
```

Or, if you are using Poetry:

```bash
poetry add click-noexit
```

Ensure that you have Click version 8.0.0 or newer.

## Installation

Import and use the `noexit` decorator to wrap your Click commands:

```python
import click
import click_noexit

@click_noexit.noexit()
@click.command()
def my_command():
    # Command logic here
    pass
```

The noexit decorator can be used without any additional arguments. It modifies the behavior of the Click command to prevent the application from exiting and allows the command to return exit codes instead.

## Examples
### Basic Command

```python
@click_noexit.noexit()
@click.command()
def hello() -> None:
    click.echo("Hello, World!")
```

### Command with Exit Code
```python
@noexit()
@click.command()
def goodbye():
    click.echo("Goodbye!")
    return 42
```

## Contributing

Contributions are welcome! If you have a feature request, bug report, or a pull request, please feel free to open an issue or a pull request on the project repository.

## License

click-noexit is released under the MIT License. See the LICENSE file for more details.