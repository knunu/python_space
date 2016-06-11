import sys
import math
from operator import itemgetter


def dbscan_clustering(argv):
    input_file_name, cluster_count = argv
    cluster_count = int(cluster_count)
    file_number = input_file_name[5]
    eps, minpts = find_parameter(file_number)

    result_size_list, cur_cluster_count = dbscan(input_file_name, eps, minpts)
    if file_number != '1' or file_number != '2' or file_number != '3':
        while cur_cluster_count < cluster_count:
            eps = update_eps(eps, cur_cluster_count, cluster_count)
            result_size_list, cur_cluster_count = dbscan(input_file_name, eps, minpts)

    if cur_cluster_count > cluster_count:
        refine_cluster(result_size_list, cluster_count)

    make_output(file_number)


def dbscan(input_file_name, eps, minpts):
    input_file = open("./%s" % input_file_name, 'r')
    cur_cluster_count = 0
    visited_set, unvisited_set = set(), set()
    cluster_list, visited_list, result_size_list = [], [], []

    for line in input_file.readlines():
        line = line.rstrip("\n").split("\t")
        object_dict[int(line[0])] = (float(line[1]), float(line[2]))
        unvisited_set.add(int(line[0]))
        # 1. mark all objects as unvisited
        visited_list.append(False)
        cluster_list.append(-1)

    while unvisited_set:
        # 2, 16. while no object is unvisited
        selected_id = unvisited_set.pop()
        # 3. randomly select an unvisited object by popping from set
        visited_list[selected_id] = True
        visited_set.add(selected_id)
        # 4. mark the object as visited(let P)
        neighbor_set = find_neighbor_set(eps, selected_id)
        if len(neighbor_set) >= minpts:
            # 5. if the eps-neighborhood(satisfy the condition, '<= eps') of P has at least minpts objects
            cluster_set = {selected_id, }
            # 6. create a new cluster set(let C), and add P to C
            cluster_list[selected_id] = cur_cluster_count

            while neighbor_set:
                # 7. neighbor_set(let N) is the set of objects in the eps-neighborhood of P.
                neighbor_id = neighbor_set.pop()
                # 8. for each object(let P') in N
                if not visited_list[neighbor_id]:
                    # 9. if P' is unvisited
                    visited_list[neighbor_id] = True
                    visited_set.add(neighbor_id)
                    unvisited_set -= {neighbor_id, }
                    # 10. mark P' as visited
                    another_neighbor_set = find_neighbor_set(eps, neighbor_id)
                    if len(another_neighbor_set) >= minpts:
                        neighbor_set |= another_neighbor_set
                        # 11. if the eps-neighborhood of P' has at least minpts objects, add those objects to N
                if cluster_list[neighbor_id] == -1:
                    cluster_set.add(neighbor_id)
                    cluster_list[neighbor_id] = cur_cluster_count
                    # 12. if P' is not yet a member of any cluster, add P' to C
            result_dict[cur_cluster_count] = cluster_set
            result_size_list.append((cur_cluster_count, len(cluster_set)))
            # 13. make output data.
            cur_cluster_count += 1
        else:
            cluster_list[selected_id] = -2
            # 14. mark p as noise, -2.
    input_file.close()

    return result_size_list, cur_cluster_count


def find_neighbor_set(eps, selected_id):
    x, y = object_dict.pop(selected_id)
    neighbor_set = set()

    for id, coordinate in object_dict.items():
        if math.hypot(x - coordinate[0], y - coordinate[1]) <= eps:
            neighbor_set.add(id)

    object_dict[selected_id] = (x, y)
    return neighbor_set


def refine_cluster(result_size_list, cluster_count):
    result_size_list.sort(key=itemgetter(1), reverse=True)
    while cluster_count != len(result_size_list):
        id, length = result_size_list.pop()
        result_dict.pop(id)


def update_eps(eps, cur_cluster_count, cluster_count):
    if cluster_count - cur_cluster_count > 1:
        return eps - 1
    elif cluster_count > cur_cluster_count:
        return eps - 0.1
    elif cur_cluster_count - cluster_count > 1:
        return eps + 1
    elif cur_cluster_count > cluster_count:
        return eps + 0.1
    else:
        return eps


def make_output(file_number):
    id = 0
    for cluster_set in result_dict.values():
        output_file_name = "output" + file_number + "_cluster_%s" % id + ".txt"
        output_file = open("./%s" % output_file_name, 'w')
        for item_id in cluster_set:
            output_file.write("%s\n" % item_id)
        output_file.close()
        id += 1


def find_parameter(file_number):
    if file_number == '1':
        return 8.416, 5
    elif file_number == '2':
        return 2.235, 10
    elif file_number == '3':
        return 6.6, 7
    return 10, 5


if __name__ == "__main__":
    object_dict, result_dict = {}, {}
    dbscan_clustering(sys.argv[1:])
