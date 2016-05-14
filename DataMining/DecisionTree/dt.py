import sys
import math

""" this function is for inducting decision tree """
def induct_dt(argv):
    training_file_name, test_file_name = argv
    training_file = open("./%s" % training_file_name, 'r')
    test_file = open("./%s" % test_file_name, 'r')
    output_file = open("./dt_result3.txt", 'w')

    """ make attribute list and attribute dictionary for containing attribute value
        EX : {Safety : Low, Med, High} """
    attribute_list = []
    tuples = []
    for attribute in training_file.readline().rstrip("\n").split("\t"):
        attribute_list.append(attribute)
        attribute_dict[attribute] = set()

    """ get data tuples from training_file and test_file """
    origin_attr_list = attribute_list.copy()
    id = 0
    for data_list in training_file:
        index = 0
        tuples.append({})
        for data in data_list.rstrip("\n").split("\t"):
            tuples[id][attribute_list[index]] = data
            attribute_dict[attribute_list[index]].add(data)
            index += 1
        id += 1

    id = 0
    test_file.readline()
    input_tuples = []
    for data_list in test_file:
        index = 0
        input_tuples.append({})
        for data in data_list.rstrip("\n").split("\t"):
            input_tuples[id][attribute_list[index]] = data
            index += 1
        id += 1

    """ seperate class_label for checking class easily """
    global class_label
    class_label = attribute_list.pop()

    """ generate decision tree, dt will be updated in global scope """
    gen_dt(tuples, attribute_list, 0)

    """ put test tuple datas into decision tree for parsing class """
    parse_data_by_dt(input_tuples)

    """ make result """
    make_output(output_file, input_tuples, origin_attr_list)

    training_file.close()
    test_file.close()
    output_file.close()

""" this function is for generating decision tree
    It follows the algorithm in text book totally.
    the list[dict] data structure to play a role as a node here. """
def gen_dt(tuples, attribute_list, level):
    if check_class(tuples, class_label):
        return {"Type" : "Class", "Value" : tuples[0][class_label], "Level" : level}
    if not len(attribute_list):
        return {"Type" : "Class", "Value" : find_majority(tuples, class_label), "Level" : level}
    attribute = select_attribute(tuples, attribute_list, class_label)
    dt.append({"Type" : "Attribute", "Value" : attribute, "Level" : level})
    attribute_list.remove(attribute)

    partitioned_tuples = {x: [] for x in attribute_dict[attribute]}
    for tuple in tuples:
        partitioned_tuples[tuple[attribute]].append(tuple)

    for tuple_value in partitioned_tuples:
        dt.append({"Type" : "AttributeValue", "Value" : tuple_value, "Level" : level})
        if not len(partitioned_tuples[tuple_value]):
            dt.append({"Type" : "Class", "Value" : find_majority(tuples, class_label), "Level" : level + 1})
        else:
            node = gen_dt(partitioned_tuples[tuple_value], attribute_list, level + 1)
            if node:
                dt.append(node)
    attribute_list.append(attribute)

""" this function is for checking whether data tuples in data list(D) is all the same class. """
def check_class(tuples, label):
    first_tuple = tuples.pop()
    check_flag = first_tuple[label]
    for tuple in tuples:
        if tuple[label] != check_flag:
            tuples.append(first_tuple)
            return False
    tuples.append(first_tuple)
    return True

""" this function is for finding which label in the tuples is major. """
def find_majority(tuples, label):
    result, count = None, 0
    majority_dict = {x: 0 for x in attribute_dict[label]}
    for tuple in tuples:
        majority_dict[tuple[label]] += 1
    for key in majority_dict:
        if majority_dict[key] > count:
            result = key
            count = majority_dict[key]
    return result

""" this function is to find best splitting_criterion.
    this function uses the algorithm ID3. """
def select_attribute(tuples, attribute_list, class_label):
    label_count = {x: 0 for x in attribute_dict[class_label]}
    attribute_count = {x: {} for x in attribute_list}
    total_count = 0

    for tuple in tuples:
        total_count += 1
        label_value = tuple[class_label]
        label_count[label_value] += 1
        for attribute in attribute_list:
            attribute_value = tuple[attribute]
            if attribute_value in attribute_count[attribute]:
                target_attribute = attribute_count[attribute][attribute_value]
                target_attribute["value"] += 1
                if label_value in target_attribute:
                    target_attribute[label_value] += 1
                else:
                    target_attribute[label_value] = 1
            else:
                attribute_count[attribute][attribute_value] = {}
                target_attribute = attribute_count[attribute][attribute_value]
                target_attribute["value"] = 1
                target_attribute[label_value] = 1

    label_info = get_information(label_count.values())
    gain, prev_gain = 0, 0
    for attribute in attribute_count:
        attr_info = 0
        for attribute_value in attribute_count[attribute]:
            target_attribute = attribute_count[attribute][attribute_value]
            attr_label_count = target_attribute.pop("value")
            attr_info += attr_label_count / total_count * get_information(target_attribute.values())
        gain = max(label_info - attr_info, prev_gain)
        if gain != prev_gain:
            result = attribute
            prev_gain = gain
    return result


""" this function is for getting information value. """
def get_information(p_list):
    result = 0
    s = 0
    for p in p_list:
        s += p
    for p in p_list:
        if p:
            result -= (p / s) * math.log2(p / s)
    return result

""" this function is for adding input_tuples with class_label and class_label's value. """
def parse_data_by_dt(input_tuples):
    for tuple in input_tuples:
        cur_level = 0
        cur_attribute = None
        for node in dt:
            if cur_level == node["Level"]:
                if node["Type"] == "Attribute":
                    cur_attribute = node["Value"]
                elif node["Type"] == "AttributeValue" and tuple[cur_attribute] == node["Value"]:
                    cur_level += 1
                elif node["Type"] == "Class":
                    tuple[class_label] = node["Value"]
                    break

""" this function make output file with pre-required format. """
def make_output(output_file, input_tuples, attribute_list):
    attribute_output = ""
    for attribute in attribute_list:
        attribute_output += "%s\t" % attribute
    output_file.write(attribute_output[::-1].replace("\t", "\n", 1)[::-1])

    for tuple in input_tuples:
        tuple_output = ""
        for attribute in attribute_list:
            tuple_output += "%s\t" % tuple[attribute]
        output_file.write(tuple_output[::-1].replace("\t", "\n", 1)[::-1])

if __name__ == "__main__":
    attribute_dict = {}
    dt = []
    induct_dt(sys.argv[1:])
