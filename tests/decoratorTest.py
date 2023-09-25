import os
from time import time

os.utime(r"C:\Projects\Python\SimpleCache\simple_cache\ProcessCache.py", (time() + 3000,30))
print(os.path.getctime(r"C:\Projects\Python\SimpleCache\simple_cache\ProcessCache.py"))
print(os.path.getmtime(r"C:\Projects\Python\SimpleCache\simple_cache\ProcessCache.py"))
