import subprocess

x = subprocess.check_output(["python", "hello.py"])
if x != b'hello\n':
  exit(1)
else:
  exit(0)