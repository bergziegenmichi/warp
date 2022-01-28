import os.path
import sys

MARKERS = os.path.expanduser("~/.warp/markers.txt")


def read_raw(file: str = MARKERS) -> list[str]:
    locations = []
    with open(file, "r") as file:
        for line in file:
            if line.strip() != "":
                locations.append(line.strip())
    return locations


def read(file: str = MARKERS) -> dict[str:str]:
    locations = {}
    for line in read_raw(file):
        name, path = line.split(":")
        locations[name] = path


def finish(message: str, command: str = "echo", exit: bool = True):
    print(f"{command} {message}")
    if exit:
        sys.exit()


def main():
    try:
        command = sys.argv[1]
    except IndexError:
        finish("Error: no command specified")

    if command == "add":
        try:
            name = sys.argv[2].replace(":", "")
        except IndexError:
            finish("Error: no name specified")
        if name in ["add", "list", "remove"]:
            finish("Error: forbidden name")
        if name in read().keys():
            finish("Error: name already in use")
        try:
            path = sys.argv[3]
            if not os.path.isdir(path):
                finish(f"Error: {path} isn't a directory")
        except IndexError:
            path = os.getcwd()
        with open(MARKERS, "a") as file:
            file.write(f"{name}:{path}\n")

    elif command == "list":
        s = ""
        for name, path in sorted(read().items()):
            s += f"{name} -> {path}\\n"
        finish({s[:-2]})

    elif command == "remove":
        try:
            name = sys.argv[2].replace(":", "")
        except IndexError:
            finish("Error: no name specified")
        with open(f"{MARKERS}.tmp", "w") as tmpfile:
            raw = read_raw()
            for line in raw:
                if name != line.split(":")[0]:
                    tmpfile.write(f"{line}\n")
        if read_raw() == read_raw(f"{MARKERS}.tmp"):
            finish(f"Error: no entry for {name}", exit=False)
        os.replace("/home/michael/.warp/markers.txt.tmp", "/markers.txt")

    else:
        try:
            location = sys.argv[1].replace(":", "")
        except IndexError:
            finish("Error: no name specified")
        for name, path in read().items():
            if name == location:
                finish(path, "cd")
        finish(f"Error: no entry for {location}")


main()
