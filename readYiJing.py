import configparser

def get_key_value_by_index():
    config = configparser.ConfigParser()
    config.read('config.txt')

    index = int(config.get('key', 'index', fallback='0'))

    result_list = []
    file_path = '易经简化版.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        key = None
        value = None

        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith('【白话】'):
                value = line[4:]
            else:
                key = line

            if key and value:
                result_list.append((key, value))
                key = None
                value = None

    if 0 <= index < len(result_list):
        key, value = result_list[index]
        return key, value
    else:
        return None, None

def increment_and_get_index():
    config = configparser.ConfigParser()
    config.read('config.txt')

    try:
        current_index = int(config.get('key', 'index', fallback='0'))
    except ValueError:
        current_index = 0

    new_index = current_index + 1

    config.set('key', 'index', str(new_index))

    with open('config.txt', 'w', encoding='utf-8') as config_file:
        config.write(config_file)

    return new_index
