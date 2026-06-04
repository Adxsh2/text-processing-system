from v3 import TextSystemV3

class TextSystemV4(TextSystemV3):
    def __init__(self):
        super().__init__()
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