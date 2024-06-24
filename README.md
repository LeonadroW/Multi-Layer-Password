使用说明
背景
我们认为，为了方便记忆。 用户设置的密码可以是多个有意义片段的组合，或者与软件本身相关，或者与用户本身经历相关，或者完全随机 例如 password = website_related + user_related1 + user_related2 + random_part1 + random_part2 一些网站会要求密码符合大小写，特殊字符的要求，这对于用户来讲比较难记

概述
本程序通过用户设定的片段密码文本文件，分层确定片段密码，最终组合 确定性地为用户创建最终的密码，每一步都是确定，并且可复现的，不会存在随机性 具体是通过哈希值进行字符串的模糊匹配，并生成一个最终的密码。程序包含以下几个主要功能： 用户可以自己创建新的txt文件，增加片段密码的层数

哈希字符串：使用SHA-256哈希函数将字符串转换为一个固定长度的数值。
构建哈希索引：为单词列表构建哈希索引，将哈希值映射到对应的字符串。
模糊匹配：通过给定的哈希值，模糊匹配到一个字符串列表的某个字符串。
读取文本文件：读取文本文件，并将每一行存储到列表中。
计算单音节：计算字符串中所有字符的ASCII值之和。
依赖
Python 3.x
hashlib 库（通常随Python标准库一起提供）
文件结构
second_piece.txt：包含用于模糊匹配的第二个单词列表。
third_piece.txt：包含用于模糊匹配的第三个单词列表。
用户可以自行创建新的txt文本，增加整个片段密码的层数，可用于自行增加特殊字符的排列规则
使用方法
运行程序：

直接运行脚本，程序将进入一个无限循环，等待用户输入。
输入一个字符串后，程序将进行以下操作：
循环读取 second_piece.txt 和 third_piece.txt 等文件，构建哈希索引。
对用户输入的字符串进行哈希处理，并进行模糊匹配。
根据匹配结果生成最终的密码。
输入和输出：

输入：用户输入一个字符串。
输出：匹配的单词列表和最终生成的密码。
退出程序：

输入 q 或 Q 将退出程序。
示例
$ python script.py
输入：

example
输出：

匹配的单词: ['matched_word1', 'matched_word2']
final password: examplematched_word1matched_word3
函数说明
hash_string(word)：

功能：使用SHA-256哈希函数将字符串转换为一个固定长度的数值。
参数：word - 输入的单词字符串。
返回值：哈希值的整数表示。
build_hash_index(word_list)：

功能：为单词列表构建哈希索引。
参数：word_list - 单词列表。
返回值：哈希值到单词的映射。
fuzzy_match_by_hash(query_hash, hash_index)：

功能：通过给定的哈希值，模糊匹配到一个字符串列表的某个字符串。
参数：query_hash - 查询的哈希值，hash_index - 哈希值到单词的映射。
返回值：匹配的单词列表。
txt2list(filename)：

功能：读取文本文件，并将每一行存储到列表中。
参数：filename - 要读取的文本文件的名称。
返回值：包含文件每一行的字符串列表。
compute_one_syllable(str)：

功能：计算字符串中所有字符的ASCII值之和。
参数：str - 输入的字符串。
返回值：字符的ASCII值之和。
run()：

功能：主运行函数，处理用户输入并生成最终密码。
参数：无。
返回值：无。
注意事项
确保 second_piece.txt 和 third_piece.txt 文件存在且格式正确。
输入字符串时，确保输入有效字符。
输入 q 或 Q 将退出程序。
![F_Spg71aYAAB0Em](https://github.com/LeonadroW/Multi-Layer-Password/assets/137982256/1a391de4-cab7-42be-a2eb-1d4dbdf44321)
