import os
import signal
import subprocess


def run(cmd, timeout=10):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, start_new_session=True)

    try:
        stdout, stderr = p.communicate(timeout=timeout)

    except subprocess.TimeoutExpired:
        os.killpg(os.getpgid(p.pid), signal.SIGTERM)

        return {"timeout": True}

    return {"timeout": False,
            "returncode": p.returncode,
            "stdout": stdout,
            "stderr": stderr
            }
