import sys
import os

from dotenv import load_dotenv

load_dotenv()

arguments = sys.argv[1:]

if len(arguments) > 0 and os.path.exists("src/commands/{}.py".format(arguments[0])):
    command_module = __import__(
        "src.commands.{}".format(arguments[0]), fromlist=[''])
    command = getattr(command_module, arguments[0])
    exit(command(arguments[1:]))
else:
    commands_dir = "src/commands"
    commands = [
        f[:-3] for f in os.listdir(commands_dir) if f.endswith('.py') and f != '__init__.py']
    print("Available commands:")
    for cmd in commands:
        print(f" - {cmd}")
