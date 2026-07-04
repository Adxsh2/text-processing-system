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