from v4 import TextSystemV4
import string

# V5顶层系统类，继承V4，复用V1-V4全部功能
class TextSystemV5(TextSystemV4):
    def __init__(self):
        super().__init__()
        self.word_list = TextLineList()
        self.count_list = TextLineList()
        self.word_graph = None

    def split_text(self):
        text_data = self.text_list.get_all()
        all_text = " ".join(text_data)
        all_words = []
        sentence_word_list = []
        current_word = ""
        temp_sentence = []

        for char in all_text:
            if char.isspace() or char in string.punctuation:
                if current_word:
                    low_word = current_word.lower()
                    all_words.append(low_word)
                    temp_sentence.append(low_word)
                    current_word = ""
                if char in ".?!。？！":
                    if temp_sentence:
                        sentence_word_list.append(temp_sentence)
                        temp_sentence = []
            else:
                current_word += char
        if current_word:
            low_word = current_word.lower()
            all_words.append(low_word)
            temp_sentence.append(low_word)
        if temp_sentence:
            sentence_word_list.append(temp_sentence)

        self.word_list.data = all_words
        print(f"V5分词完成，总分词数量：{len(all_words)}")
        return all_words, sentence_word_list

    def stat_word_frequency(self):
        if self.word_list.get_length() == 0:
            self.split_text()
        words = self.word_list.get_all()
        count_dict = {}
        for w in words:
            count_dict[w] = count_dict.get(w, 0) + 1
        self.word_list.data = []
        self.count_list.data = []
        for word, cnt in count_dict.items():
            self.word_list.add(word)
            self.count_list.add(cnt)
        print("V5词频统计完成")

    def show_word_frequency(self):
        if self.word_list.get_length() == 0:
            self.split_text()
            self.stat_word_frequency()
        word_cnt_pairs = list(zip(self.word_list.get_all(), self.count_list.get_all()))
        word_cnt_pairs.sort(key=lambda x: x[1], reverse=True)
        print("\n===== V5 词频统计（降序） =====")
        for idx, (word, cnt) in enumerate(word_cnt_pairs, 1):
            print(f"{idx}. {word}：{cnt}次")
        print("==============================\n")
