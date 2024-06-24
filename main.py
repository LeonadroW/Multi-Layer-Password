import hashlib
import os
"""
整个代码说明：
"""
def hash_string(word):
    """
    使用SHA-256哈希函数将字符串转换为一个固定长度的数值
    :param word: 输入的单词字符串
    :return: 哈希值的整数表示
    """
    sha256 = hashlib.sha256()
    sha256.update(word.encode('utf-8'))
    hash_hex = sha256.hexdigest()
    return int(hash_hex, 16)

def build_hash_index(word_list):
    """
    为单词列表构建哈希索引
    :param word_list: 单词列表
    :return: 哈希值到单词的映射
    """
    hash_index = {}
    for word in word_list:
        hash_value = hash_string(word)
        if hash_value in hash_index:
            hash_index[hash_value].append(word)
        else:
            hash_index[hash_value] = [word]
    return hash_index

def fuzzy_match_by_hash(query_hash, hash_index):
    """
    通过给定的哈希值，模糊匹配到一个字符串列表的某个字符串
    :param query_hash: 查询的哈希值
    :param hash_index: 哈希值到单词的映射
    :return: 匹配的单词列表
    """
    # 找到最接近的哈希值
    closest_hash = min(hash_index.keys(), key=lambda x: abs(x - query_hash))
    return hash_index[closest_hash]

def txt2list(filename):
    """
    读取文本文件，并将每一行存储到列表中。

    参数:
    filename (str): 要读取的文本文件的名称。

    返回:
    list: 包含文件每一行的字符串列表。
    """
    lines_list = []  # 创建一个空列表，用于存储每一行的内容
    with open(filename, 'r', encoding='utf-8') as file:  # 打开文件，指定编码为utf-8
        for line in file:  # 遍历文件中的每一行
            lines_list.append(line.strip())  # 去除行尾的换行符并添加到列表中
    return lines_list  # 返回包含所有行的列表

def compute_one_syllable(str):
    sum = 0
    for charA in str:
        sum += ord(charA)
    print(sum)
    return sum

def expand(ok):
    # 设置要搜索的目录路径
    directory_path = '.'
    # 初始化一个空列表来存储文件名
    txt_files = []
    # 遍历目录中的文件
    for filename in os.listdir(directory_path):
        # 检查文件扩展名是否为.txt，并且文件名不是指定的两个文件
        if filename.endswith('.txt') and filename not in ['second_piece.txt', 'third_piece.txt']:
            txt_files.append(filename)
    if len(txt_files) == 0:
        return ok
    final = ok
    # 打印所有符合条件的文件名
    for txt_file in txt_files:
        print(txt_file)
        second_list = txt2list(txt_file)
        second_index = build_hash_index(second_list)
        print(second_index)
        # 查询哈希值
        query_hash = hash_string(ok)
        # 模糊匹配
        matched_words = fuzzy_match_by_hash(query_hash, second_index)
        for one in matched_words:
            print(f"匹配的单词: {one}")
            final += one
            break



    return final
    # # 如果需要读取文件内容
    # for txt_file in txt_files:
    #     file_path = os.path.join(directory_path, txt_file)
    #     with open(file_path, 'r') as file:
    #         content = file.read()
    #         print(content)  # 打印文件内容，或者你可以对content进行其他操作

def run():
    first_piece = input()
    if first_piece == 'q':
        quit()
    second_list = txt2list('second_piece.txt')
    second_index = build_hash_index(second_list)
    print(second_index)
    # 查询哈希值
    query_hash = hash_string(first_piece)
    # 模糊匹配
    matched_words = fuzzy_match_by_hash(query_hash, second_index)
    print(f"匹配的单词: {matched_words}")
    third_list = txt2list('third_piece.txt')
    third_index = build_hash_index(third_list)
    print(third_index)
    # 查询哈希值
    for second_match in matched_words:
        query_hash2 = hash_string(second_match)
        break
    # 模糊匹配
    matched_words2 = fuzzy_match_by_hash(query_hash2, third_index)
    standard_password = ''
    for third_match in matched_words2:
        print(f"final password: {first_piece + second_match + third_match}")
        standard_password = first_piece + second_match + third_match

    final = expand(standard_password)
    print(final)

if __name__ == '__main__':
    while(True):
        run()


