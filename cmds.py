import os
import multiprocessing, subprocess
# subprocess.run("C:\Shvyrev_IoT/Blender.lnk",shell =True)


def Setup(app):
    dir =os.getcwd()
    result = subprocess.run(dir+"/"+app,shell =True, encoding='utf-8')
    if result.returncode == 0:
        return f"файл {result.args} открыт"
    else:
        return f"файл {result.args} открыть не удалось"





def get_answer(simple_command):
    def DirOut(command):
        word = command.split(" ")
        for i in range(len(word)):
            if word[i] == "<DIR>":
                word[i - 1] = "-"
                word[i + 1] = "-"
        return " ".join(word)

    def ChDir(command):
        a = (command.split(' '))
        del a[0]
        info = ' '.join(a)
        # print(info)
        os.chdir(info)
        return os.popen("dir").read().encode('cp1251').decode('cp866')


    if simple_command == "dir":
        return DirOut(os.popen(simple_command).read().encode('cp1251').decode('cp866'))

    elif simple_command.split(" ")[0] == "cd":
        return ChDir(simple_command)

    else:
        try:

            return os.popen(simple_command).read().encode('cp1251').decode('cp866')

        except Exception:
            return "нет такой команды"

