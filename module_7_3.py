class WordsFinder:
    def __init__(self, *files):
        self.file_names = []
        for file in files:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                file_list = []
                for line in file:
                    for word in line.lower().replace(',', '').replace('.', '').replace(
                            '=', '').replace('!', '').replace(';', '').replace(
                            ':', '').replace(' - ', '').split():
                        file_list.append(word)
                all_words[name] = file_list
        return all_words

    def find(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            find_dict[name] = int(words.index(word.lower())) + 1
        return find_dict

    def count(self, word):
        count_dict = {}
        for name, words in self.get_all_words().items():
            count_dict[name] = words.count(word.lower())
        return count_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

# Вывод в консоль:
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки',
# 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}

# {'test_file.txt': 3}
# {'test_file.txt': 4}
