from psutil import virtual_memory


print(virtual_memory().percent)
