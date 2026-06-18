    def show_word_relation(self, target):
        self.build_word_graph()
        neighbor = self.word_graph.get_neighbors(target.lower())
        print(f"\n===== 词语「{target}」关联关系 =====")
        if not neighbor:
            print("无匹配关联词汇")
        else:
            for word, weight in neighbor.items():
                print(f"关联词汇：{word}，共同出现 {weight} 次")
        print("===================================\n")

    def show_all_graph(self):
        self.build_word_graph()
        self.word_graph.print_full_graph()
