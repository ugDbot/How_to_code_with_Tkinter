import os
user = os.getlogin()
path = "C:/Users/" + user + "/Documents/plans"
try:
    os.mkdir(path)
except OSError:
    print("failed")
else:
    print("success")