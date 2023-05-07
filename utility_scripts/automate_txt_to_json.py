import os

os.system("cd utility_scripts; make clean; make; cd ..")
dirnames = next(os.walk("."))[1]
for dirname in dirnames:
    filename = f"{dirname}/{dirname}.vectormap.txt"
    if os.path.exists(filename):
        os.system(
            f"./utility_scripts/txt_to_json {filename} > {dirname}/{dirname}.vectormap.json")

os.system("cd utility_scripts; make clean; cd ..")
