import subprocess

def main():
    results = subprocess.run(["dir"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return results