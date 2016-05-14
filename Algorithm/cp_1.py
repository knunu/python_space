# 6
# 슬리퍼,50
# 운동화,8
# 슬립퍼,22
# 나이키,74
# 슬리뻐,32
# 나이크,7
# 3
# 슬리퍼,슬립퍼
# 나이키,나이크
# 슬립퍼,슬리뻐

f_in = open("/Volumes/Transcend/test_case.txt", 'r')
f_out = open("/Volumes/Transcend/result.txt", 'w')
keyword_list = list()
keyword_dict = dict()
relation_set = set()
relation_dict = dict()
keyword_num = int(f_in.readline())

for _ in range(keyword_num):
    keyword, count = f_in.readline().split(',')
    count = int(count)
    keyword_list.append(keyword)
    keyword_dict[keyword] = count

relation_num = int(f_in.readline())
for _ in range(relation_num):
    keyword, rel_keyword = f_in.readline().split(',')
    rel_keyword = rel_keyword.rstrip()
    relation_set.add(rel_keyword)
    if keyword not in relation_dict:
        relation_set.add(keyword)
        flag = True
        for k, v in relation_dict.items():
            if keyword in v:
                relation_dict[k] += [rel_keyword]
                flag = False
                break
        if flag:
            relation_dict[keyword] = [keyword, rel_keyword]
    else:
        relation_dict[keyword] += [rel_keyword]

f_out.write("%d\n" % (len(relation_dict) + len(set(keyword_list) - relation_set)))
for keyword, count in keyword_dict.items():
    if keyword in relation_set and len(keyword_dict) != len(relation_set) + len(keyword_list):
        for represent, item_list in relation_dict.items():
            if represent not in keyword_list:
                continue
            total_count = 0
            for item in item_list:
                keyword_list.remove(item)
                total_count += keyword_dict[item]
            f_out.write("%s,%d\n" % (represent, total_count))
    elif keyword not in relation_set:
        f_out.write("%s,%d\n" % (keyword, count))
f_in.close()
f_out.close()
