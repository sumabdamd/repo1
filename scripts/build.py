from pathlib import Path
from datetime import datetime
import zipfile

DIST_DIR = Path("dist")

def clean_dist():
    if DIST_DIR.exists():
        for item in DIST_DIR.iterdir():
            if item.is_file():
                item.unlink()
    else:
        DIST_DIR.mkdir()

def generate_artifacts():
    (DIST_DIR / "output.txt").write_text("Hello World from Python\n")
    (DIST_DIR / "build-time.txt").write_text(
        f"Build time: {datetime.utcnow().isoformat()} UTC\n"
    )

def zip_artifacts():
    zip_path = DIST_DIR / "artifacts.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in DIST_DIR.iterdir():
            if file.is_file() and file.name != zip_path.name:
                zipf.write(file, arcname=file.name)

def main():
    print("Starting Python build...")
    clean_dist()
    generate_artifacts()
    zip_artifacts()
    print("Artifacts generated in dist/")

if __name__ == "__main__":
    main()
