# 线性表核心封装（所有版本共用）
class TextLineList:
    def __init__(self):
        self.data = []  # 底层用列表实现顺序表

    def add(self, text):
        """尾部添加元素"""
        self.data.append(text)

    def insert(self, index, text):
        """指定索引插入元素"""
        if 0 <= index <= len(self.data):
            self.data.insert(index, text)
        else:
            raise IndexError("索引越界")

    def delete(self, index):
        """删除指定索引元素"""
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        else:
            raise IndexError("索引越界")

    def update(self, index, text):
        """修改指定索引元素"""
        if 0 <= index < len(self.data):
            self.data[index] = text
        else:
            raise IndexError("索引越界")

    def get(self, index):
        """获取指定索引元素"""
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            return None

    def get_all(self):
        """获取所有元素"""
        return self.data.copy()

    def get_length(self):
        """获取长度"""
        return len(self.data)

def load_from_list(self, data_list):
    """从列表加载数据，用于回滚功能"""
    self.data = data_list.copy()
    
# 版本1：基础文本存储与显示系统
class TextSystemV1:
    def __init__(self):
        self.text_list = TextLineList()

    def load_text(self, file_path=None):
        """加载文本（支持手动输入或文件读取）"""
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        self.text_list.add(line.strip('\n'))
                print(f"成功加载 {self.text_list.get_length()} 行文本")
            except FileNotFoundError:
                print("文件不存在，将创建新文本库")
        else:
            print("请手动输入文本（输入空行结束）：")
            while True:
                line = input()
                if not line:
                    break
                self.text_list.add(line)

    def show_text(self):
        """带行号显示文本"""
        if self.text_list.get_length() == 0:
            print("当前文本为空！")
            return
        print("\n===== 文本内容 =====")
        for idx, text in enumerate(self.text_list.get_all()):
            print(f"第{idx+1}行：{text}")
        print("====================\n")

    def edit_text(self):
        """基础编辑：修改指定行"""
        self.show_text()
        try:
            line_num = int(input("输入要修改的行号：")) - 1
            new_text = input("输入新的文本内容：")
            self.text_list.update(line_num, new_text)
            print("修改成功！")
        except ValueError:
            print("请输入数字行号！")
        except IndexError:
            print("行号越界，修改失败！")


# 测试入口
if __name__ == "__main__":
    system = TextSystemV1()
    system.load_text()
    system.show_text()
    system.edit_text()
    system.show_text()
