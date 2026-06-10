from v3 import TextSystemV3

class TextSystemV4(TextSystemV3):
    def __init__(self):
        super().__init__()
        self.backup_text = None

    def backup(self):
        """全量备份文本列表"""
        self.backup_text = self.text_list.get_all().copy()
        print("✅数据备份成功")

    def rollback(self):
        """回滚至上一次备份"""
        if self.backup_text is not None:
            self.text_list.load_from_list(self.backup_text)
            print("✅数据回滚完成")
        else:
            print("❌无备份记录，无法回滚")

    def cut_text(self, start_line, end_line):
        """截取指定起止行文本，行号从1开始"""
        try:
            start = start_line - 1
            end = end_line
            total = self.text_list.get_length()
            # 边界合法性校验
            if start < 0 or end > total or start >= end:
                print("❌截取行号超出范围")
                return None
            res = self.text_list.get_all()[start:end]
            print(f"✅截取成功，共{len(res)}行")
            return res
        except ValueError:
            print("❌行号必须输入数字")
            return None


# 程序入口（放在类定义外面，文件最末尾）
if __name__ == "__main__":
    system = TextSystemV4()
    # 加载并展示文本
    system.load_text()
    system.show_text()

    # 备份数据
    system.backup()

    # 编辑文本
    system.edit_text()
    system.show_text()

    # 关键词查找与统计
    key = input("请输入查找关键词：")
    res = system.search_by_keyword(key)
    system.show_search_result(key, res)
    system.stat_text(key)

    # 截取文本
    try:
        s_line = int(input("输入起始行号："))
        e_line = int(input("输入结束行号："))
        cut_res = system.cut_text(s_line, e_line)
        if cut_res:
            print("截取内容：")
            for line in cut_res:
                print(line)
    except ValueError:
        print("行号请输入数字！")

    # 数据回滚
    system.rollback()
    system.show_text()

    # BF/KMP 算法耗时测试
    print("\n===== BF & KMP 性能对比 =====")
    test_text = "ababcabcabx"
    test_pattern = "abcab"
    system.time_compare(test_text, test_pattern)
