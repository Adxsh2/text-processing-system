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

# V6独立测试入口
if __name__ == "__main__":
    sys = TextSystemV6()
    sys.load_text()
    sys.extract_keywords(top_n=5)
    sys.show_summary(max_sentences=3)