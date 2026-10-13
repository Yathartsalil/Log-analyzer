from pathlib import Path
import re
import sys
import hashlib

with open("c.txt", "rb") as file:
    data = file.read()

hasher = hashlib.sha256()
hasher.update(data)

if hasher.hexdigest() == "":

    if len(sys.argv) < 3:
        print("Usage: python scanner.py <log_file_or_folder> <authorized_file>")
        sys.exit(1)

    authorized_ips = set()

    user_input = sys.argv[1]
    authorized_file = Path(sys.argv[2])
    path = Path(user_input)

    if not authorized_file.exists():
        print("Path Error in authorized file")
        sys.exit(1)

    if not path.exists():
        print("Path Error")
        sys.exit(1)

    elif path.is_dir():
        print("Folder")
        files = path.rglob("*.log")

    elif path.is_file():
        files = [path]

    else:
        print("Unknown error")
        sys.exit(1)

    try:
        with open(authorized_file, "r", encoding="latin-1") as filereader1:
            content1 = filereader1.read()
            final1 = re.findall(r"\d+\.\d+\.\d+\.\d+", content1)
            authorized_ips = set(final1)

    except PermissionError:
        print("Permission error: cannot read authorized file.")
        sys.exit(1)

    except FileNotFoundError:
        print("Error: authorized file was not found.")
        sys.exit(1)

    except IsADirectoryError:
        print("Error: authorized file path is a directory.")
        sys.exit(1)

    except OSError as error:
        print(f"Error reading authorized file: {error}")
        sys.exit(1)

    with open("logger.txt", "a") as logg:
        for file in files:

            if "venv" in file.parts or ".venv" in file.parts:
                continue

            if file.resolve() == authorized_file.resolve():
                continue

            try:
                with open(file, "r", encoding="latin-1") as filereader:
                    for line in filereader:
                        content = line.strip()
                        final = re.findall(r"\d+\.\d+\.\d+\.\d+", content)

                        for k in final:
                            if k in authorized_ips:
                                logg.write(f"Authorized : {k}\n")
                            else:
                                logg.write(f"NOT AUTHORIZED : {k}\n")

            except (PermissionError, FileNotFoundError, OSError) as error:
                print(f"Could not read {file}: {error}")

else:
    print("IP file is not valid.")