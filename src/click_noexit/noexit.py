import click
import click.exceptions

import functools

from typing import Any
from typing import Union
from typing import Optional
from typing import Callable


# type alias for any command result in Click
CommandResult = Optional[Union[int, Any]]

# type alias for any command function in Click
CommandFunction = Callable[..., CommandResult]


def noexit(*args, **kwargs) -> Callable[[CommandFunction], CommandFunction]:
    """
    A decorator to wrap Click commands and prevent them from exiting the application directly.

    Click commands, by default, exit the application after completion or when an error occurs.
    This decorator ensures that the command does not exit the application, but instead,
    returns the exit code. This is particularly useful when integrating Click commands into
    larger applications, where you want to handle exits and exceptions more gracefully.

    :param args: Arguments to pass to the command.
    :param kwargs: Keyword arguments to pass to the command.
    :return: A decorated command function.
    """

    def decorator(command: CommandFunction) -> CommandFunction:
        """
        The actual decorator that modifies the Click command.

        :param command: The Click command to decorate.
        :return: The wrapped command with modified behavior.
        """

        @functools.wraps(command)
        def wrapper(*args, **kwargs) -> CommandResult:
            """
            The wrapper function that is applied to the Click command. It executes the command
            and catches the `click.exceptions.Exit` exception to prevent the application from exiting.
            Instead, it returns the exit code.

            :param args: Arguments to pass to the command.
            :param kwargs: Keyword arguments to pass to the command.
            :return: The exit code of the command if an exit was requested, otherwise None.
            """

            try:
                # Execute the command with standalone_mode set to False.
                # This prevents Click from automatically handling exceptions and exiting the application.
                return command(standalone_mode=False, *args, **kwargs)
            except click.exceptions.Exit as e:
                # If the command requests an exit (like with ctx.exit()),
                # catch it and return the exit code instead of exiting the program.
                return e.exit_code
            except click.exceptions.ClickException as e:
                # Handle Click-specific exceptions. This captures exceptions that are internal to Click,
                # allowing the application to handle these exceptions and return the associated exit code
                # instead of terminating abruptly.
                return e.exit_code

        return wrapper
    return decorator
