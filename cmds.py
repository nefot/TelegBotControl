import os
import subprocess


# проверяет есть ли лишние строки у команды
def GetAnswer(simple_command):
    if simple_command.split(" ")[0] == "/c":
        return CheckCommand(simple_command[3:])
    else:
        return CheckCommand(simple_command)


# проверка быстрых команд
def CheckCommand(commands):
    if commands.split(" ")[0] == "dir":
        return DirOut(os.popen(commands).read().encode('cp1251').decode('cp866'))
    elif commands.split(" ")[0] == "cd":
        return ChDir(commands)
    else:
        try:
            return os.popen(commands).read().encode('cp1251').decode('cp866')
        except Exception as error:
            return error


# запуск приложения в новом потоке

def Setup(app):
    # print(app)
    dir = os.getcwd()
    try:
        result = subprocess.Popen(dir + "/" + app, shell=True, encoding='utf-8', stdout=subprocess.PIPE)
        return f"файл {result.args} открыт"
    except Exception as err:
        return err


# директория возвращает форматированную команду
def DirOut(command):
    try:
        fields = ('data', 'time', 'type', 'name')
        lst_data = list(filter(None, command.split("\n")))
        cur_dir = (" ".join(lst_data[2].split(" "))[3:]) + '\n'

        folders = list(filter(None, (lst_data[-1].split(" "))))[-5]
        files = list(filter(None, (lst_data[-2].split(" "))))[-4]
        size = list(filter(None, (lst_data[-1].split(" "))))[-3]

        lst_data_out = [f"директория {cur_dir}\n", "время         |   тип   |    имя\n",
                        "____________________________________\n",
                        f'{folders} папок\n',
                        f'{files} файлов\n',
                        f'{size}  байт свободно\n']
        s = ''
        lst_data_sorted = []
        for index, stroke in enumerate(lst_data[3:-2]):
            # print(len(stroke.split()[2]))
            if len(stroke.split()[2]) < 7:
                s = stroke.split()[2]
                # print(lst_data)
                for i in range(6 - len(stroke.split()[2])):
                    s = str(stroke.split()[2]) + "  " * (i + 1)
            # print(len(stroke.split()[2]))
            lst_data_sorted.append(dict(zip(fields, [stroke.split()[0], stroke.split()[1], s,
                                                     " ".join(stroke.split()[3:])])))  # 'data', 'time', 'type', 'name'
            lst_data_out.insert(2, lst_data_sorted[index]['data'] + ' | ' + lst_data_sorted[index]['type'] + ' | ' +
                                lst_data_sorted[index]['name'] + "\n")
        return " ".join(lst_data_out)
    except Exception as error:
        return error


# метод добавляет файл в архив
def SendFile(command):
    try:
        pass
    except Exception as error:
        return error


# метод изменяет директорию
def ChDir(command):
    try:
        os.chdir(" ".join(command.split(" ")[1:]))
        return DirOut(os.popen("dir").read().encode('cp1251').decode('cp866'))
    except FileNotFoundError:
        return "Файл не найден проверьте синтаксис"
    except OSError:
        return "Файл не найден проверьте синтаксис"
    except Exception as error:
        return (error)
