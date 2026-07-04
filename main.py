from v6 import TextSystemV6

if __name__ == "__main__":
    print("===== 完整文本处理系统 V6（整合V1~V5所有功能） =====")
    sys = TextSystemV6()

    # ========== V1 基础文本功能 ==========
    print("\n【1. V1：文本加载、展示、编辑】")
    sys.load_text()
    sys.show_text()

    # ========== V2 检索、文本统计 ==========
    print("\n【2. V2：关键词检索、高亮、全局统计】")
    search_key = input("输入检索关键词：")
    match_result = sys.search_by_keyword(search_key)
    sys.show_search_result(search_key, match_result)
    sys.stat_text(search_key)

    # ========== V3 BF/KMP匹配性能测试 ==========
    print("\n【3. V3：BF暴力匹配 & KMP算法耗时对比】")
    test_str = "ababcabcabxabcab"
    test_pat = "abcab"
    sys.time_compare(test_str, test_pat, times=2000)

    # ========== V4 备份、截取、回滚 ==========
    print("\n【4. V4：文本备份、行截取、数据回滚】")
    sys.backup()
    try:
        s = int(input("输入截取起始行号："))
        e = int(input("输入截取结束行号："))
        cut_data = sys.cut_text(s, e)
        if cut_data:
            print("截取内容：", cut_data)
    except ValueError:
        print("行号输入格式错误，跳过截取")
    sys.rollback()
    sys.show_text()

    # ========== V5 分词、词频、词语共现图 ==========
    print("\n【5. V5：中文分词、词频统计、词语关联图谱】")
    words, sents = sys.split_text()
    sys.show_word_frequency()
    sys.build_word_graph()
    sys.show_full_graph_info()
    query_word = input("输入需要查询关联的词语：")
    sys.search_word_neighbor(query_word)

    # ========== V6 新增：关键词提取 + 自动摘要 ==========
    print("\n【6. V6：过滤停用词提取关键词、文本自动摘要】")
    sys.extract_keywords(top_n=6)
    sys.show_summary(max_sentences=3)
