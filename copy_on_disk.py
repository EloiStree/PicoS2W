
import shutil
from pathlib import Path

# Resolve paths from the script's location, not the current working directory.
script_dir = Path(__file__).resolve().parent
source = script_dir / "copy_me_on_pico"

mount = next(
    (Path(f"{letter}:/") for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     if (Path(f"{letter}:/") / "boot_out.txt").is_file()),
    None,
)
destination = mount

if not source.is_dir():
    print(f"Error: Source folder not found: {source}")
else:
    if destination is None:
        print("Error: CIRCUITPY drive not found.")
    else:
        try:
            shutil.copytree(source, destination, dirs_exist_ok=True)
            print(f"Folder copied successfully to: {destination}")
        except OSError as e:
            print(f"Copy failed: {e}")
