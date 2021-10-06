class File_status:
    text = ""
    sentences_count = 0
    words_count = 0
    characters_count = 1
    words_sent = []

    @classmethod
    def get_status(cls, filename):
        file = open(filename, 'r')
        cls.text = file.read()
        cls.sentences_count = cls.words_count = 0
        cls.characters_count = 1
        cls.words_sent = [0]
        is_word = 0
        for char in cls.text:
            if char.isalpha():
                is_word = 1
            else:
                cls.words_count += is_word
                cls.words_sent[len(cls.words_sent)-1] += is_word
                if char == '\n':
                    cls.characters_count += 1
                elif cls.words_sent[len(cls.words_sent)-1] > 0 and (char == '.' or char == '?' or char == '!'):
                    cls.sentences_count += 1
                    cls.words_sent.append(0)
                is_word = 0
        if is_word:
            cls.words_sent[len(cls.words_sent)-1] += 1
            cls.words_count += 1
            cls.sentences_count += 1


# there is text in this file in yes.txt
file = open("yes.txt", 'r')
File_status.get_status(file.name)
print(File_status.text)
print(File_status.characters_count)
print(File_status.words_count)
print(File_status.sentences_count)
