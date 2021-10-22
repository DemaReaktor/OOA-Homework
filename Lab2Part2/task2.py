from os.path import *


class File_Operation:
    """static class for operations under files"""
    @classmethod
    def open(cls, file_name):
        """will open file and return this if it is possible"""
        if not isfile(file_name):
            raise FileNotFoundError("file has not found")
        file = open(file_name, 'r')
        if not file:
            raise ValueError("file has not opened")
        return file

    @classmethod
    def get_characters_count(cls, file_name):
        """count number of characters in file"""
        file = cls.open(file_name)
        count = 0
        while file.read(1) != '':
            count += 1
        file.close()
        return count

    @classmethod
    def get_lines_count(cls, file_name):
        """count number of lines in file"""
        file = cls.open(file_name)
        count = 1
        char = file.read(1)
        while char != '':
            if char == '\n':
                count += 1
            char = file.read(1)
        file.close()
        return count

    @classmethod
    def get_sentences_count(cls, file_name):
        """count number of sentences in file"""
        file = cls.open(file_name)
        count = 0
        is_sentence = False
        while True:
            char = file.read(1)
            if char != '.' and char != '!' and char != '?':
                if not is_sentence:
                    count += 1
                    is_sentence = True
            elif is_sentence:
                is_sentence = False
            if char == '':
                break
        return count

    @classmethod
    def get_words_count(cls, file_name):
        """count number of words in file"""
        file = cls.open(file_name)
        count = 0
        is_word = False
        while True:
            char = file.read(1)
            if char == '':
                break
            if char.isalnum() and not is_word:
                count += 1
                is_word = True
            elif not char.isalnum() and is_word:
                is_word = False
        file.close()
        return count


print("words:", File_Operation.get_words_count("yes.txt"))
print("characters:", File_Operation.get_characters_count("yes.txt"))
print("sentences:", File_Operation.get_sentences_count("yes.txt"))
print("lines:", File_Operation.get_lines_count("yes.txt"))