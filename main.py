import os
import subprocess

root_dir = '/Users/brianabbott/apps/lscloud/liftstation.cloud'

files = []


def get_file_paths():
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d != 'node_modules']
        for filename in filenames:
            if not filename.endswith('.json'):
                files.append(os.path.join(dirpath, filename))


def compare_files(file_paths, last_commit_hash, latest_commit_hash):
    for file_path in file_paths:
        diff = subprocess.run(['git', 'diff', last_commit_hash, latest_commit_hash, '--', file_path],
                              capture_output=True, text=True, cwd=root_dir)
        output_file_path = file_path + '.txt'
        with open(output_file_path, 'w') as output_file:
            output_file.write(diff.stdout)


get_file_paths()
compare_files(files, '6828394792dfe4ab09787ba9219470df9c82326f', 'e45a979999fb6c54e68cea9bffeb79781b0eb936')