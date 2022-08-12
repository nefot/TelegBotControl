import psutil

dict_proc = {}


def GetTask():
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        dict_proc[proc.name()] = proc.pid
    sorted(dict_proc.items())
    strings = []
    for key, item in dict_proc.items():
        strings.append("{}: {}".format(key.capitalize(), item))
    result = "\n ".join(strings)
    return (str(result))


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def KillTask(name):
    for process in psutil.process_iter():
        if process.name() == name:
            process.kill()


def KillTaskInt(pids):
    for proc in psutil.process_iter(['pid', 'name', 'username']):

        if proc.pid == pids:
            proc.kill()
#
