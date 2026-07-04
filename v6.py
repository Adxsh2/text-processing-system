from text_v5 import TextSystemV5

# 版本6：文本摘要与关键词提取系统
class TextSystemV6(TextSystemV5):
    def __init__(self):
        super().__init__()

    def extract_keywords(self, top_n=5):
        """提取关键词（按频率排序+过滤停用词）"""
        if not self.word_list.get_all():
            self.split_text()
        self.stat_word_frequency()
        words = self.word_list.get_all()
        counts = self.count_list.get_all()
        word_count = list(zip(words, counts))
        word_count.sort(key=lambda x: x[1], reverse=True)
        stop_words = {"的", "了", "是", "在", "和", "有", "我", "你", "他", "这", "那", "一个", "我们", "他们"}
        keywords = []
        for word, cnt in word_count:
            if word not in stop_words and len(word) > 1:
                keywords.append((word, cnt))
                if len(keywords) >= top_n:
                    break
        print("\n===== 关键词提取结果 =====")
        for i, (word, cnt) in enumerate(keywords, 1):
            print(f"{i}. {word}（{cnt}次）")
        print("==========================\n")
        return keywords

    def generate_summary(self, max_sentences=3):
        """生成文本摘要（句子长度+关键词权重打分）"""
        text_data = self.text_list.get_all()
        if len(text_data) == 0:
            return "无文本内容，无法生成摘要"
        keywords_tuple = self.extract_keywords(top_n=10)
        keyword_dict = {word: cnt for word, cnt in keywords_tuple}

        sentence_score = []
        for sent in text_data:
            score = 0
            for kw, weight in keyword_dict.items():
                if kw in sent:
                    score += weight
            sent_len = len(sent)
            if 10 < sent_len < 80:
                score *= 1.2
            sentence_score.append((sent, score))
        sentence_score.sort(key=lambda x: x[1], reverse=True)
        top_sentences = sentence_score[:max_sentences]
        summary_sent = [s[0] for s in top_sentences]
        return summary_sent

    def show_summary(self, max_sentences=3):
        """格式化打印摘要面板"""
        summary_result = self.generate_summary(max_sentences)
        print("\n===== V6 文本摘要结果 =====")
        if isinstance(summary_result, str):
            print(summary_result)
        else:
            for idx, sent in enumerate(summary_result, 1):
                print(f"{idx}. {sent}")
        print("==========================\n")
        return summary_result

# 本地单独测试V6，修复循环导入错误（删掉内部from v6 import）
if __name__ == "__main__":
    sys = TextSystemV6()
    sys.load_text()
    sys.extract_keywords(top_n=5)
    sys.show_summary(max_sentences=3)