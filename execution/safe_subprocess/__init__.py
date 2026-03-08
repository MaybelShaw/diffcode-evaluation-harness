import os
import signal
import subprocess
from dataclasses import dataclass


@dataclass()
class Result:
    status: str
    returncode: int | None
    stdout: str
    stderr: str
    timeout: bool = False


def run(cmd, timeout=10):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, start_new_session=True,text=True)

    try:
        stdout, stderr = p.communicate(timeout=timeout)

    except subprocess.TimeoutExpired:
        os.killpg(os.getpgid(p.pid), signal.SIGTERM)

        return Result(status="timeout", returncode=1)

    return Result(status="success", returncode=p.returncode, stdout=stdout, stderr=stderr, timeout=False)
