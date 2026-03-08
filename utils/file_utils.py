from tempfile import TemporaryDirectory
from pathlib import Path


class TempWorkSpace:
    def __init__(self):
        self.tmpdir = TemporaryDirectory()
        self.root = Path(self.tmpdir.name)

    def write(self, path, content):
        path = self.root / path
        path.write_text(content)
        return path

    def cleanup(self):
        self.tmpdir.cleanup()
