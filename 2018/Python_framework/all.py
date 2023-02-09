import os

for day in range(1, 26):
    print("======== DAY", day, "========")
    os.system("python3 main.py " + "{:02d}".format(day) + "\n\n")