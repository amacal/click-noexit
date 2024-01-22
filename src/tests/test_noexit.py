import click
import click.testing

import click_noexit


def test_command_execution_success_no_op() -> None:
    # The purpose of this test is to verify that a Click command wrapped with the `noexit` decorator
    # behaves as expected when it executes successfully without any internal logic (a no-op command).
    # It checks if the command returns `None` when there are no errors or exit triggers, 
    # indicating a successful execution without any specific exit code.

    @click_noexit.noexit()
    @click.command()
    def hello() -> None:
        pass

    assert hello() is None


def test_command_execution_success_17() -> None:
    # This test verifies the behavior of a Click command wrapped with the `noexit` decorator
    # when the command successfully completes and explicitly returns an exit code (17 in this case).
    # It's essential to ensure that the `noexit` decorator doesn't interfere with the command's
    # ability to return a normal exit code when not using Click's context management to exit.
    # The test checks if the command properly returns the specific exit code it's supposed to.

    @click_noexit.noexit()
    @click.command()
    def hello() -> int:
        return 17

    assert hello() == 17


def test_command_execution_exit_due_to_missed_argument() -> None:
    # This test checks the behavior of a Click command wrapped with the `noexit` decorator
    # when it's missing a required argument. The test ensures that instead of the program 
    # terminating, the `noexit` decorator catches the exit and returns the appropriate 
    # exit code that Click uses for missing arguments (typically exit code 2).

    @click_noexit.noexit()
    @click.command()
    @click.argument("name")
    def hello(name: str) -> None:
        assert name is not None

    assert hello() == 2


def test_command_execution_context_17() -> None:
    # The purpose of this test is to verify that the `noexit` decorator properly handles 
    # explicit exit requests from within a Click command. The command uses Click's context 
    # management to request an exit with a specific exit code (17 in this case).
    # The test checks if the `noexit` decorator correctly captures and returns this exit code.

    @click_noexit.noexit()
    @click.command()
    @click.pass_context
    def hello(ctx: click.Context) -> None:
        ctx.exit(17)

    assert hello() == 17

