import subprocess
import sys



subprocess.check_output('git add .',shell=True, text=True)
subprocess.check_output(f'git commit -m "{sys.argv[1]}"',shell=True, text=True)
subprocess.check_output('git push',shell=True, text=True)