from text_v5 import TextSystemV5

if __name__ == "__main__":
    print("===== 文本处理系统 V5.0（整合V1~V4 + 图结构分词词频） =====")
    sys = TextSystemV5()

    # V1功能
    print("\n【1. V1功能：文本加载、展示】")
    sys.load_text()
    sys.show_text()

    # V2功能
    print("\n【2. V2功能：关键词检索、文本统计】")
    search_key = input("输入检索关键词：")
    match_result = sys.search_by_keyword(search_key)
    sys.show_search_result(search_key, match_result)
    sys.stat_text(search_key)

    # V3功能
    print("\n【3. V3功能：BF、KMP字符串匹配耗时对比】")
    test_str = "ababcabcabxabcab"
    test_pat = "abcab"
    sys.time_compare(test_str, test_pat, times=2000)

    # V4功能
    print("\n【4. V4功能：数据备份、文本截取、回滚】")
    sys.backup()
    try:
        s = int(input("输入截取起始行号："))
        e = int(input("输入截取结束行号："))
        cut_data = sys.cut_text(s, e)
        if cut_data:
            print("截取内容：", cut_data)
    except ValueError:
        print("行号输入错误，跳过文本截取")
    sys.rollback()
    sys.show_text()

    # V5新增图功能（修正方法名 + 补充建图步骤）
    print("\n【5. V5新增功能：分词、词频、词语共现图】")
    words, sents = sys.split_text()
    sys.show_word_frequency()

    # 必须先构建共现图才能查询、打印图
    sys.build_word_graph()

    # 打印整张邻接图
    sys.show_full_graph_info()

    # 查询单个词语相邻关联词
    query_word = input("输入需要查询关联的词语：")
    sys.search_word_neighbor(query_word)
