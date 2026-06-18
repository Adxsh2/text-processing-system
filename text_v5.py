from v4 import TextSystemV4
import string

# V5顶层系统类，继承v4，复用V1-V4全部功能
class TextSystemV5(TextSystemV4):
    def __init__(self):
        super().__init__()
        self.word_list = TextList()
        self.count_list = TextList()
        self.word_graph = None

    def split_text(self):
        text_data = self.text_list.get_all()
        all_text = " ".join(text_data)
        all_words = []
        sentence_word_list = []
        current_word = ""
        temp_sentence = []

        for char in all_text:
            if char.isspace():
                if current_word:
                    low_word = current_word.lower()
                    all_words.append(low_word)
                    temp_sentence.append(low_word)
                current_word = ""
            elif char in "，。！？；、":
                if current_word:
                    low_word = current_word.lower()
                    all_words.append(low_word)
                    temp_sentence.append(low_word)
                if temp_sentence:
                    sentence_word_list.append(temp_sentence)
                temp_sentence = []
                current_word = ""
            else:
                current_word += char
        if current_word:
            low_word = current_word.lower()
            all_words.append(low_word)
            temp_sentence.append(low_word)
        if temp_sentence:
            sentence_word_list.append(temp_sentence)

        self.word_list.data = all_words
        print(f"v5分词完成，总分词数量：{len(all_words)}")
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
        print("v5词频统计完成")

    def show_word_frequency(self):
        if self.word_list.get_length() == 0:
            self.split_text()
            self.stat_word_frequency()
        word_cnt_pairs = list(zip(self.word_list.get_all(), self.count_list.get_all()))
        word_cnt_pairs.sort(key=lambda x: x[1], reverse=True)
        print("\n==== V5 词频统计（降序） ====")
        for idx, (word, cnt) in enumerate(word_cnt_pairs, 1):
            print(f"{idx}. 【{word}】：{cnt}次")
        print("===================================\n")

    # 嵌入TextSystemV5类内部的建图函数
    def build_word_graph(self):
        _, sentences = self.split_text()
        self.word_graph = WordGraph()
        for sent in sentences:
            for i in range(len(sent)-1):
                w1 = sent[i]
                w2 = sent[i+1]
                self.word_graph.add_edge(w1, w2)
        print("v5词语共现图构建完成")

    # ========== C新增：图查询接口 ==========
    def search_word_neighbor(self, target):
        if not self.word_graph:
            self.build_word_graph()
        res = self.word_graph.get_neighbors(target)
        print(f"词语「{target}」的相邻词：{res}")
        return res

    def show_full_graph_info(self):
        if not self.word_graph:
            self.build_word_graph()
        self.word_graph.print_full_graph()


# 自定义无向加权邻接图（作业要求图逻辑结构）
class WordGraph:
    def __init__(self):
        self.adj_table = {}

    def add_vertex(self, word):
        if word not in self.adj_table:
            self.adj_table[word] = {}

    def add_edge(self, w1, w2):
        self.add_vertex(w1)
        self.add_vertex(w2)
        self.adj_table[w1][w2] = self.adj_table[w1].get(w2, 0) + 1
        self.adj_table[w2][w1] = self.adj_table[w2].get(w1, 0) + 1

    def get_neighbors(self, target_word):
        return self.adj_table.get(target_word, {})

    def print_full_graph(self):
        print("\n==== V5 词语共现邻接图 ====")
        for word, neighbor_dict in self.adj_table.items():
            print(f"顶点【{word}】关联关系：{neighbor_dict}")
        print("===================================\n")