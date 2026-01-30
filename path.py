from pathlib import Path

base_A=Path.cwd()
date_A=base_A/"practice"/"deta"
for path in date_A.iterdir():
    print(path)     #
    print(path.read_text(encoding="utf-8"))    