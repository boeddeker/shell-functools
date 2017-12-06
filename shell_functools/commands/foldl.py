#!/usr/bin/env python3

from shell_functools.utils.types import T_ARRAY
from shell_functools.utils.internal import add_dynamic_type
from shell_functools.utils.command import Command
from shell_functools.utils.error import panic


class Foldl(Command):
    def __init__(self):
        super().__init__("foldl")

    def partial_application(self):
        # Skip partial application
        pass

    def initialize(self):
        # Initial value
        if len(self.arguments) != 1:
            panic("Initial value to foldl is required")

        self.acc = add_dynamic_type(self.arguments[0])

    def handle_input(self, value):
        if value.fttype == T_ARRAY and self.column is not None:
            idx = self.column - 1
            self.acc = self.function(value.value[idx], self.acc)
        else:
            self.acc = self.function(value, self.acc)

    def finalize(self):
        self.print_formatted(self.acc)
