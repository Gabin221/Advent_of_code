from pathlib import Path
from typing import List

def read_input(file_name: str) -> List[str]:
    """Lit un fichier situé dans le même dossier que le script appelant"""
    path = Path(__file__).resolve().parent / file_name
    with path.open("r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]
