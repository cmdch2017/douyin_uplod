def get_key_value_by_index():
    with open('index.txt', 'r', encoding='utf-8') as index_file:
        index = int(index_file.read().strip())

    result_list = []
    file_path = '易经简化版.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        key = None
        value = None

        for line in lines:
            line = line.strip()
            if not line:
                # 如果是空行，跳过处理
                continue
            if line.startswith('【白话】'):
                # 当前行是“白话”行，将其作为value
                value = line[4:]
            else:
                # 当前行不是“白话”行，将其作为key
                key = line

            # 如果key和value都存在，将其添加到列表中
            if key and value:
                result_list.append((key, value))
                key = None
                value = None

    # 返回结果
    if 0 <= index < len(result_list):
        key, value = result_list[index]
        return key, value
    else:
        return None, None

def increment_and_get_index():
    file_path = 'index.txt'
    try:
        # 读取当前索引值
        with open(file_path, 'r', encoding='utf-8') as index_file:
            current_index = int(index_file.read().strip())
    except (FileNotFoundError, ValueError):
        # 处理文件不存在或者无法解析为整数的情况
        current_index = 0

    # 增加索引值
    new_index = current_index + 1

    # 将新的索引值写回文件
    with open(file_path, 'w', encoding='utf-8') as index_file:
        index_file.write(str(new_index))

    return new_index