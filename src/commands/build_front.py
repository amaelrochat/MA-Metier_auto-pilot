def build_front(args):
    import subprocess
    import os

    front_dir = os.path.join(os.path.dirname(__file__), '../http/frontend')
    subprocess.run(['npm', 'install'], cwd=front_dir, check=True)
    subprocess.run(['npm', 'run', 'build'], cwd=front_dir, check=True)

    return 0
