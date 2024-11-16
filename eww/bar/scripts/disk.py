from psutil import disk_usage

print(int(disk_usage("/").free / 1000000000))
