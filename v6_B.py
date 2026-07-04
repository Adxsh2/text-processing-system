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