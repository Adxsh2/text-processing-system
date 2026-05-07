from v1 import TextSystemV1  # 从 v1 导入基础系统

# 版本2：文本查找与统计系统
class TextSystemV2(TextSystemV1):
    def __init__(self):
        super().__init__()

    def search_by_keyword(self, keyword):
        """按关键词查找（行+字符级）"""
        matches = []
        text_data = self.text_list.get_all()
        for line_idx, line in enumerate(text_data):
            if keyword in line:
                char_indices = []
                start = 0
                while start < len(line):
                    idx = line.find(keyword, start)
                    if idx == -1:
                        break
                    char_indices.append(idx)
                    start = idx + len(keyword)
                matches.append({
                    "line_num": line_idx + 1,
                    "line_content": line,
                    "char_indices": char_indices
                })
        return matches

    def show_search_result(self, keyword, matches):
        """展示查找结果并高亮"""
        if not matches:
            print(f"未找到包含【{keyword}】的内容！")
            return
        print(f"\n===== 查找【{keyword}】结果 =====")
        for match in matches:
            line = match["line_content"]
            highlighted_line = line.replace(keyword, f"\033[31m{keyword}\033[0m")
            print(f"第{match['line_num']}行：{highlighted_line}")
            print(f"  字符位置：{match['char_indices']}\n")

    def stat_text(self, keyword):
        """文本统计（把input移到外面，避免二次输入）"""
        text_data = self.text_list.get_all()
        total_lines = self.text_list.get_length()
        total_chars = sum(len(line) for line in text_data)
        count = sum(line.count(keyword) for line in text_data)

        print("\n===== 文本统计结果 =====")
        print(f"总行数：{total_lines}")
        print(f"总字符数：{total_chars}")
        print(f"关键词【{keyword}】出现次数：{count}")
        print("========================\n")


# 测试入口
if __name__ == "__main__":
    system = TextSystemV2()
    system.load_text()
    system.show_text()
    keyword = input("输入查找关键词：")
    matches = system.search_by_keyword(keyword)
    system.show_search_result(keyword, matches)
    system.stat_text(keyword)
