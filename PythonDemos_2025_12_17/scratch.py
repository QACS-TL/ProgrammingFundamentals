import glob, os.path
def list_dir(dirname):
    print("Searching", dirname, "...")
    for fname in glob.iglob(dirname + '/*'):
        if os.path.isdir(fname):
            list_dir(fname)
        else:
            print(fname, os.path.getsize(fname))
            list_dir("C:\\Temp\\ToDoApp")

list_dir("C:\\Temp\\ToDoApp")


