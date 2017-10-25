
import os
import shutil


src_dir = r"D:\backups\ags"
tgt_dir = r"\\server\share\folder"
files = os.listdir(src_dir)
for f in files:
    shutil.move(os.path.join(src_dir, f), os.path.join(tgt_dir, f))