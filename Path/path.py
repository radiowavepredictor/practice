from pathlib import Path

base_A=Path(__file__).parent
data_A=base_A/"data"
for path in data_A.iterdir():
    print(f"\n{path}ファイルの中身を記述します") 
    print(path.read_text(encoding="utf-8"))    