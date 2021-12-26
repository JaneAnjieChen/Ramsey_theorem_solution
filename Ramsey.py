# By Chen Anjie, 21/12/2021

# In discrete mathematics, Ramsey’s theorem states that for any positive
# integer k, there is an integer m such that in any party with at least m guests, one of the
# following statements must be true:
# (1) There are at least k guests who know each other.
# (2) There are at least k guests who do not know each other.
# For example, for k = 3, then in any party of at least 6 guests, either there are three
# guests who know each other, or there are three guests who do not know each other.

# This question asks you to write a program (using either Python, C, C++ or Java) to help
# verify Ramsey’s theorem. The input of the program is organized as follows:
#  The first line of the input has an integer m, followed by m lines of string, each
# representing a guest (so there are totally m guests for this input).
#  Then, there is another line of integer n, followed by n lines of pair of guests (guest
# a and guest b know each other if and only if there is a line of pair a, b in the
# input).
#  Then, there is a line containing an integer k.
# For the output, your program should print a set of k guests who knows each other, and if
# there is no such set, the program should print a set of k guests who do not know each
# other.


def get_graph_nodes(relation_list):
    nodes = []
    for relation in relation_list:
        if relation[0] not in nodes:
            nodes.append(relation[0])
        if relation[1] not in nodes:
            nodes.append(relation[1])
    return nodes

def compare_relations(r1, r2):
    '''
    :param r1: tuple
    :param r2: tuple
    :return: BOOL
    '''
    if r1 == r2:
        return True
    elif r1[0] == r2[1] and r1[1] == r2[0]:
        return True
    else:
        return False


def compare_graphs(g1, g2):
    '''
    :param g1: a list of tuples
    :param g2: a list of tuples
    :return: BOOL
    '''
    if len(g1) != len(g2):
        return False
    elif set(get_graph_nodes(g1)) != set(get_graph_nodes(g2)):
        return False
    else:
        count = 0
        for r1 in g1:
            for r2 in g2:
                if compare_relations(r1, r2) == True:
                    count += 1
                    break
        if count == len(g1):
            return True
        else:
            return False


def solution(guest_num, guest_list, relation_num, relation_list, k):
    '''
    :param guest_num: int
    :param guest_list: a list consists of all the guests
    :param relation_num: int
    :param relation_list: a tuple list
    :param k: int
    :return: a list of k guests
    '''
    # connected_guest_list: 图里所有的节点
    connected_guest_list = get_graph_nodes(relation_list)
    connected_guest_num = len(connected_guest_list)

    # 找relation_list构成的所有连通子图
    connected_graphs = []
    for i in range(relation_num):
        # 连通图从一条边开始，逐步增加边
        connected_graph = [relation_list[i]]
        # 连通图里所有的节点
        connected_graph_guest_list = get_graph_nodes(connected_graph)

        for connected_guest in connected_guest_list:
            if connected_guest not in connected_graph_guest_list:
                # 向连通图里新加节点，则需要加‘和每个已有节点’的边
                newly_add_relations = []
                for guest in connected_graph_guest_list:
                    newly_add_relations.append((guest, connected_guest))

                # check需要加的所有边是否在图里
                count = 0
                for newly_add_relation in newly_add_relations:
                    for relation in relation_list:
                        if compare_relations(newly_add_relation, relation) == True:
                            count += 1
                            break
                if count == len(newly_add_relations):
                    connected_graph += newly_add_relations
                    connected_graph_guest_list = get_graph_nodes(connected_graph)

        already_have = False
        for g in connected_graphs:
            if compare_graphs(g, connected_graph) == True:
                already_have = True
        if already_have == False:
            print(connected_graph)
            connected_graphs.append(connected_graph)

    print('-'*50+'The connected graphs'+'-'*50)

    # 全连接图包含的点数
    connected_graphs_nums = {}
    for connected_graph in connected_graphs:
        connected_graphs_nums[tuple(connected_graph)] = len(get_graph_nodes(connected_graph))
    print('graphs and the numbers of nodes: ', connected_graphs_nums)

    sorted_connected_graphs_nums = sorted(connected_graphs_nums.items(), key=lambda a: a[1], reverse=True)
    print('Sorted according to the number of nodes', sorted_connected_graphs_nums)
    MAX = sorted_connected_graphs_nums[0][1]

    if k <= MAX:
        return get_graph_nodes(sorted_connected_graphs_nums[0][0])[:k]
    else:
        not_connected_nodes = []
        not_connected_nodes += list(set(guest_list) - set(connected_guest_list))
        # print(not_connected_nodes)

        # try从每个连通图中找到一个不在其他任何连通图里的点
        # 如果没有，就找下一个连通子图
        connected_guests_count = {}
        for connected_graph in connected_graphs:
            for node in get_graph_nodes(connected_graph):
                if node not in connected_guests_count:
                    connected_guests_count[node] = 1
                else:
                    connected_guests_count[node] += 1

        for guest, count in connected_guests_count.items():
            if count == 1:
                not_connected_nodes.append(guest)

        return not_connected_nodes[:k]


if __name__ == '__main__':
    # # TEST SAMPLES
    # k_list = solution(guest_num=4, guest_list=['a', 'b', 'c', 'd'],
    #                   relation_num=2, relation_list=[('a', 'b'), ('a', 'c')],
    #                   k=3)

    # k_list = solution(guest_num=4, guest_list=['a', 'b', 'c', 'd'],
    #                   relation_num=3, relation_list=[('a', 'b'), ('a', 'c'), ('b', 'c')],
    #                   k=3)

    k_list = solution(guest_num=7, guest_list=['1', '2', '3', '4', '5', '6', '7'],
                      relation_num=8, relation_list=[('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4'), ('3', '4'), ('5', '6'), ('4', '7')],
                      k=4)
    print(k_list)







