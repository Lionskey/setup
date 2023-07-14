import glob
import os
import time
import subprocess

files = []
for file in glob.glob("*"):
	path = file
	ti_c = os.path.getctime(path)
	c_ti = time.ctime(ti_c)
	t_obj = time.strptime(c_ti)
	year = time.strftime("%Y", t_obj)

	print(f"The file {path} was created in the year {year}")
	if(os.path.isdir(year)):
		subprocess.call(["copy", path, year])
	else:
		subprocess.call(["mkdir", year])
		subprocess.call(["copy", path, year])

