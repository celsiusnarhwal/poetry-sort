import re

from cleo.events.console_events import TERMINATE
from cleo.events.console_terminate_event import ConsoleTerminateEvent
from cleo.events.event_dispatcher import EventDispatcher
from cleo.io.inputs.option import Option
from poetry.console.application import Application
from poetry.console.commands.add import AddCommand
from poetry.console.commands.command import Command
from poetry.console.commands.init import InitCommand
from poetry.core.toml import TOMLFile
from poetry.plugins.application_plugin import ApplicationPlugin


def get_plugin_config(poetry_file: TOMLFile):
    config = {
        "sort-python": False,
        "format": True,
    }

    config.update(poetry_file.read().get("tool", {}).get("sort", {}).get("config", {}))

    return config


def sort_dependencies(cmd: Command, include: list, exclude: list, only: list):
    class Dependency:
        def __init__(self, name: str, version: str):
            self.name = name
            self.version = version

        def __eq__(self, other):
            return self.name == other.name

        def __gt__(self, other):
            return other < self

        def __lt__(self, other):
            if not sort_config.get("sort-python") and "python" in [self.name, other.name]:
                return self.name == "python" and other.name != "python"

            return self.name < other.name

    def sort(dependencies: dict) -> dict:
        return {k: v for k, v in (sorted(dependencies.items(), key=lambda dep: Dependency(*dep)))}

    sort_config = get_plugin_config(cmd.poetry.file)

    pyproject = cmd.poetry.file.read()
    poetry = pyproject["tool"]["poetry"]
    groups: dict = poetry.get("group", {})
    group_names = *groups.keys(),

    match {*include, *exclude, *only}.difference(["main", *group_names]):
        case invalid_groups if invalid_groups:
            cmd.line_error(f"Invalid group(s): {', '.join(invalid_groups)}", style="error")
            return 1

    groups_to_sort = only or set(group_names).intersection(include or group_names).union(["main"]).difference(exclude)

    if "main" in groups_to_sort:
        poetry["dependencies"] = sort(poetry["dependencies"])

    for group, data in groups.items():
        if group in groups_to_sort:
            data["dependencies"] = sort(data["dependencies"])

    pyproject["tool"]["poetry"] = poetry

    contents = re.sub(r"\n{3,}", "\n\n", pyproject.as_string()) if sort_config.get("format") else pyproject.as_string()
    cmd.poetry.file.path.open("w").write(contents)


class PoetrySortCommand(Command):
    name = "sort"
    description = "Sort the dependencies in your pyproject.toml."
    options = [
        Option("--with", description="The optional dependency groups to sort.", flag=False, is_list=True),
        Option("--without", description="The dependency groups to skip. Supersedes --with.", flag=False, is_list=True),
        Option("--only", description="The only dependency groups to sort. Supersedes --with and --without.", flag=False,
               is_list=True),
    ]

    def handle(self) -> int:
        sort_dependencies(
            cmd=self,
            include=self.option("with"),
            exclude=self.option("without"),
            only=self.option("only"),
        )


# noinspection PyMethodMayBeStatic,PyUnboundLocalVariable
class PoetrySortPlugin(ApplicationPlugin):
    def activate(self, application: Application) -> None:
        application.command_loader.register_factory("sort", self.sort_command_factory)
        application.event_dispatcher.add_listener(TERMINATE, self.sort_dependencies)

    @staticmethod
    def sort_command_factory():
        return PoetrySortCommand()

    def sort_dependencies(self, event: ConsoleTerminateEvent, event_name: str, dispatcher: EventDispatcher) -> None:
        command = event.command

        triggers = (AddCommand, InitCommand)

        if not isinstance(command, triggers):
            return

        if isinstance(command, InitCommand):
            groups = ["main", *command.poetry.file.read()["tool"]["poetry"].get("group", {}).keys()]
        elif isinstance(command, AddCommand):
            groups = [command.option("group")]

        sort_dependencies(
            cmd=command,
            include=[],
            exclude=[],
            only=groups,
        )
