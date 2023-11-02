import os
def create_file_list(folder):
    file_list = os.listdir(folder)
    new_file_list = []
    for file in file_list:
        with open(folder + "/" + file, 'r', encoding='utf-8') as temp_file:
            new_file_list.append([file, 0, []])
            for line in temp_file:
                new_file_list[-1][2].append(line.strip())
                new_file_list[-1][1] += 1
    return sorted(new_file_list, key=lambda x: x[1], reverse=False)

#print(create_file_list('txt'))

def create_new_file(folder, filename):
    with open(filename + '.txt', 'w+', encoding='utf-8') as new_file:
        for file in create_file_list(folder):
            new_file.write(f'Название файла: {file[0]}\n')
            new_file.write(f'Количество строк: {file[1]}\n')
            for string in file[2]:
                new_file.write(string + '\n')
            new_file.write('\n')
    return print('Файл создан')


create_new_file('txt', 'new_file')