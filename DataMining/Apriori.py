from itertools import chain, combinations
import sys

""" this function gets necessary subsets of specific set. """
def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))

""" this function do main apriori process really, also takes a main function role. """
def apriori(argv):
    min_sup, input, output = argv
    input_file = open("./%s" % input, 'r')
    output_file = open("./%s" % output, 'w')

    """ set minimum_support value for checking whether itemsets are frequent or not. """
    min_sup = float(min_sup) / 100
    transaction_list = []

    """ make transaction list and get the number of transaction(s) by using input text file. """
    for line in input_file:
        transaction_list.append(set(line.rstrip("\n").split("\t")))
    transaction_count = len(transaction_list)

    """ we need to make two frequent itemsets.
        next_freq_itemsets is for making K frequent itemsets by using K-1 frequent itemsets.
        freq_itemsets is whole frequent itemsets. """
    next_freq_itemsets = find_frequent_1_itemsets(min_sup, transaction_list, transaction_count)
    freq_itemsets = next_freq_itemsets.copy()
    k = 2

    """ find candidate itemsets by using apriori_gen function, and count proper candidate number(s) of transaction database.
        At last, save the count to support count dictionary. """
    while len(next_freq_itemsets) != 0:
        cand_itemsets = apriori_gen(next_freq_itemsets)
        for transaction in transaction_list:
            for candidate in cand_itemsets:
                candidate_set = set(candidate)
                if candidate_set <= transaction:
                    if candidate in sup_count_dict.keys():
                        sup_count_dict[candidate] += 1
                    else:
                        sup_count_dict[candidate] = 1

        """ set next frequent itemsets that satisfy minimum support by using K-1 subsets in support count dictionary. """
        next_freq_itemsets.clear()
        for item in sup_count_dict:
            if k != len(item): continue
            if sup_count_dict[item] / transaction_count >= min_sup:
                next_freq_itemsets.add(item)
        k += 1
        """ frequent itemset is updated with next frequent itemsets. """
        freq_itemsets |= next_freq_itemsets

    """ make output file by using frequent itemsets and total transaction's count. """
    make_output(output_file, freq_itemsets, transaction_count)

    input_file.close()
    output_file.close()

""" this function makes first frequent itemsets.
    save count of 1-itemsets in transaction database to support count dictionary.
    check all 1-itemsets whether it satisfies the minimum support or not, if it satisfies, then add itemset to frequent 1-itemsets. """
def find_frequent_1_itemsets(min_sup, transaction_list, transaction_count):
    freq_1_itemsets = set()

    for transaction in transaction_list:
        for item in transaction:
            item = frozenset({item})
            if item in sup_count_dict.keys():
                sup_count_dict[item] += 1
            else:
                sup_count_dict[item] = 1

    for item in sup_count_dict:
        if sup_count_dict[item] / transaction_count >= min_sup:
            freq_1_itemsets.add(item)

    return freq_1_itemsets

""" this function makes candidate itemsets to make next frequent item set.
    use two frequent itemsets for self-joining to generate base candidate itemsets.
    remove infrequent itemsets by calling has_infrequent_subset function to make candidates improved. """
def apriori_gen(freq_itemset):
    temp_freq_itemset = freq_itemset.copy()
    cand_itemset = set()

    for l1 in freq_itemset:
        temp_freq_itemset.remove(l1)

        for l2 in temp_freq_itemset:
            c = set(l1)
            for item in l2: c.add(item)

            if has_infrequent_subset(c, freq_itemset):
                continue
            else:
                cand_itemset.add(frozenset(c))

    return cand_itemset

""" this function check whether specific candidate itemset's K-1 subset is infrequent or not.
    if the subset is infrequent, return true. if not, return false. """
def has_infrequent_subset(cand_itemset, freq_itemset):
    for candidate in cand_itemset:
        K_1_subset = cand_itemset - set({candidate})
        if not frozenset(K_1_subset) in freq_itemset:
            return True
    return False

""" this function make output file with pre-required format. """
def make_output(output_file, freq_itemsets, transaction_count):
    for freq_frz_itemset in freq_itemsets:
        if len(freq_frz_itemset) != 1:
            support = sup_count_dict[freq_frz_itemset] / transaction_count * 100
            freq_itemset = set(freq_frz_itemset)
            for itemset in map(set, powerset(freq_itemset)):
                asso_itemset = freq_itemset - itemset
                confidence = sup_count_dict[freq_frz_itemset] / sup_count_dict[frozenset(itemset)] * 100
                output_file.write("%s\t%s\t%.2f\t%.2f\n" % (itemset, asso_itemset, support, confidence))

if __name__ == "__main__":
    sup_count_dict = {}
    apriori(sys.argv[1:])
