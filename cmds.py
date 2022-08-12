import os
import subprocess


def GetAnswer(simple_command):

    if simple_command == "dir":
        return DirOut(os.popen(simple_command).read().encode('cp1251').decode('cp866'))
    elif simple_command.split(" ")[0] == "cd":
        return ChDir(simple_command)
    else:
        return os.popen(simple_command).read().encode('cp1251').decode('cp866')




def Setup(app):
    dir = os.getcwd()
    result = subprocess.Popen(dir + "/" + app, shell=True, encoding='utf-8')

    return f"файл {result.args} открыт"



def DirOut(command):
    fields = ('data', 'time', 'type', 'name')
    lst_data = list(filter(None, command.split("\n")))
    cur_dir = (lst_data[2].split(" "))[3] + '\n'
    folders = list(filter(None, (lst_data[-1].split(" "))))[-5]
    files = list(filter(None, (lst_data[-2].split(" "))))[-4]
    size = list(filter(None, (lst_data[-1].split(" "))))[-3]

    lst_data_out = [f"директория {cur_dir}\n", "время         |   тип   |    имя\n",
                    "____________________________________\n",
                    f'{folders} папок\n',
                    f'{files} файлов\n',
                    f'{size}  байт свободно\n']

    lst_data_sorted = []
    for index, stroke in enumerate(lst_data[3:-2]):
        lst_data_sorted.append(
            dict(zip(fields, [stroke.split()[0], stroke.split()[1], stroke.split()[2],
                              " ".join(stroke.split()[3:])])))
        lst_data_out.insert(2, lst_data_sorted[index]['data'] + ' | ' + lst_data_sorted[index]['type'] + ' | ' +
                            lst_data_sorted[index]['name'] + "\n")
    return " ".join(lst_data_out)

def ChDir(command):

    os.chdir(command.split(" ")[1])
    return DirOut(os.popen("dir").read().encode('cp1251').decode('cp866'))
