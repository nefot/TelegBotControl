import os
import subprocess


def Setup(app):
    dir = os.getcwd()
    result = subprocess.run(dir + "/" + app, shell=True, encoding='utf-8')
    if result.returncode == 0:
        return f"файл {result.args} открыт"
    else:
        return f"файл {result.args} открыть не удалось"


def get_answer(simple_command):
    FIELDS = ('data', 'time', 'type', 'name')

    def DirOut(command):

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
        for index, str in enumerate(lst_data[3:-2]):
            lst_data_sorted.append(
                dict(zip(FIELDS, [str.split()[0], str.split()[1], str.split()[2], " ".join(str.split()[3:])])))
            lst_data_out.insert(2, lst_data_sorted[index]['data'] + ' | ' + lst_data_sorted[index]['type'] + ' | ' +
                                lst_data_sorted[index]['name'] + "\n")
        return " ".join(lst_data_out)

    # def DirOut(command):
    #
    #     ss = []
    #
    #     lst_data = []
    #     lst_data2 = []
    #
    #     word = command.split("\n")
    #     for index, name in enumerate(word):
    #         if word[index] != "" and word[index] != "/n":
    #             lst_data.append(word[index])
    #     cur_dir = (lst_data[2].split(" "))[3]
    #     ss.append(f"текущая директория - {cur_dir}\n")
    #     ss.append("время          тип        имя\n")
    #     for index, str in enumerate(lst_data[3:-2]):
    #         str_word = str.split(" ")
    #
    #         str_word = list(filter(None, str_word))
    #
    #         lst_data2.append(dict(zip(FIELDS, [str_word[0], str_word[1], str_word[2], " ".join(str_word[3:])])))
    #
    #         ss.append(f"{lst_data2[index]['data']} | {lst_data2[index]['type']} | {lst_data2[index]['name']}" + "\n")
    #
    #     return " ".join(ss)
    #     # lst_data.append(dict(zip(FIELDS,)))

    def ChDir(command):
        a = (command.split(' '))
        del a[0]
        info = ' '.join(a)
        # print(info)
        os.chdir(info)
        return DirOut(os.popen("dir").read().encode('cp1251').decode('cp866'))

    if simple_command == "dir":
        return DirOut(os.popen(simple_command).read().encode('cp1251').decode('cp866'))

    elif simple_command.split(" ")[0] == "cd":
        return ChDir(simple_command)

    else:
        try:

            return os.popen(simple_command).read().encode('cp1251').decode('cp866')

        except Exception:
            return "нет такой команды"
