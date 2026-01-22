def build_front(args):
    import subprocess
    import os
    import shutil

    front_dir = os.path.join(os.path.dirname(__file__), '../http/frontend')
    npm_path = shutil.which('npm')
    if not npm_path:
        raise FileNotFoundError("npm is not installed or not in PATH")
    
    subprocess.run([npm_path, 'install'], cwd=front_dir, check=True)
    subprocess.run([npm_path, 'run', 'build'], cwd=front_dir, check=True)

    return 0
