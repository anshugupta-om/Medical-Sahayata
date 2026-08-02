from pathlib import Path
import shutil
from uuid import uuid4

UPLOAD_DIR = Path("../uploads")


def save_uploaded_file(file):

    UPLOAD_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    extension = Path(file.filename).suffix

    filename = f"{uuid4()}{extension}"

    filepath = UPLOAD_DIR / filename

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(filepath)