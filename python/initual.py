from pathlib import Path

folders = [
    Path('/src/data'),
    Path('/src/organized')
]

for folder in folders:
    if not folder.exists():
        folder.mkdir()
