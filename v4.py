from v3 import TextSystemV3

class TextSystemV4(TextSystemV3):
    def __init__(self):
        super().__init__()
        self.backup_text = None

    # 新增：给V5调用的添加文本方法
    def add_text(self, text):
        self.text_list.add(text)

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
