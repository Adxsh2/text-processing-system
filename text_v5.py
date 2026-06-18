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
        print("\n===== V5 词语共现邻接图 =====")
        for word, neighbor_dict in self.adj_table.items():
            print(f"顶点【{word}】关联关系：{neighbor_dict}")
        print("=============================\n")

    # 嵌入TextSystemV5类内部的建图函数
    def build_word_graph(self):
        _, sentences = self.split_text()
        self.word_graph = WordGraph()
        for sent in sentences:
            for i in range(len(sent)-1):
                w1 = sent[i]
                w2 = sent[i+1]
                self.word_graph.add_edge(w1, w2)
        print("V5词语共现图构建完成")
