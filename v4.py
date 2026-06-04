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

    def replace_text(self, old_str, new_str, replace_all=True):
        """字符串替换，True全局替换，False每行只替换首个"""
        self.backup()
        all_data = self.text_list.get_all()
        new_data = []
        for line in all_data:
            if replace_all:
                line = line.replace(old_str, new_str)
            else:
                line = line.replace(old_str, new_str, 1)
            new_data.append(line)
        self.text_list.load_from_list(new_data)
        print(f"✅替换完成：{old_str}→{new_str}")


if __name__ == "__main__":
    obj = TextSystemV4()
    obj.load_text()
    print("====原始文本====")
    obj.show_text()

    cut_res = obj.cut_text(2, 4)
    print("截取结果：", cut_res)

    obj.replace_text("a", "A", True)
    print("====替换后====")
    obj.show_text()

    obj.rollback()
    print("====回滚后====")
    obj.show_text()
        self.backup_text = None  # 文本备份

    def backup(self):
        """备份当前文本"""
        self.backup_text = self.text_list.get_all().copy()
        print("文本已备份！")

    def rollback(self):
        """回溯到备份版本"""
        if self.backup_text:
            self.text_list.load_from_list(self.backup_text)
            print("已回溯到备份版本！")
        else:
            print("无备份版本，无法回溯！")
