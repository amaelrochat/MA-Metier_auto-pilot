import sys
import os
from src.commands.default import default

arguments = sys.argv[1:]

if not arguments:
    default()
    exit(0)

if os.path.exists("src/commands/{}.py".format(arguments[0])):
    command_module = __import__(
        "src.commands.{}".format(arguments[0]), fromlist=[''])
    command = getattr(command_module, arguments[0])
    exit(command(arguments[1:]))
