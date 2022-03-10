# 0/1 KnapSack problem overview: https://en.wikipedia.org/wiki/Knapsack_problem

from typing import List
from xmlrpc.client import boolean

class KnapSackItem:

    BAG_MAX_WEIGHT = 10

    def __init__(self, value:int, weight:int):
        self.value = value
        self.weight = weight

"""
General idea:
- Put the optimal items in the bag according to value and weight.
- The maximum weight of the bag carrying the items is KnapSackItem.BAG_MAX_WEIGHT
- Build table with the maxium weight of the bag as columns
- Each item as rows. Put the most valuable item, according to its weight and the weight
of its predecessors on each case (row,column) case.
"""

def build_weights_table(list_items:List[KnapSackItem]) -> List[int]:
    optimal_weight:List[int] = []
    optimal_weight_hits:List[bool] = []
    for item_index in range(0, len(list_items)):
        optimal_weight.append([])
        optimal_weight_hits.append([])
        if item_index == 0:
            for weight_index in range(0, KnapSackItem.BAG_MAX_WEIGHT+1):
                optimal_weight[item_index].append(0)
                optimal_weight_hits[item_index].append(False)
            continue
        item_weight = list_items[item_index].weight
        item_value = list_items[item_index].value
        for weight_index in range(0, KnapSackItem.BAG_MAX_WEIGHT+1):
            previous_item_value = optimal_weight[item_index-1][weight_index] < item_value + optimal_weight[item_index-1][weight_index-item_weight]
            if weight_index != 0 and weight_index >= item_weight and previous_item_value:
                optimal_value = item_value + optimal_weight[item_index-1][weight_index-item_weight]
                optimal_weight_hits[item_index].append(True)
            else:
                optimal_value = optimal_weight[item_index-1][weight_index]
                optimal_weight_hits[item_index].append(False)
            optimal_weight[item_index].append(optimal_value)
    return (optimal_weight, optimal_weight_hits)

def print_selected_items(boolean_list:List[boolean], items_list:List[KnapSackItem]):
    max_weight = KnapSackItem.BAG_MAX_WEIGHT
    for item_index in range(len(boolean_list)-1, 0, -1):
        #print(item_index, max_weight)
        if boolean_list[item_index][max_weight]:
            print(f"Selected item number: {item_index}")
            max_weight -= items_list[item_index].weight

items_list = [
    KnapSackItem(10, 5),
    KnapSackItem(40, 4),
    KnapSackItem(30, 6),
    KnapSackItem(60, 3)
]
items_list.insert(0, KnapSackItem(0,0)) # First element is 0,0 -> Covers the 'no objects' case.
results = build_weights_table(items_list)
print(f"Maximized value: {results[0][-1][-1]}")
print(f"Full table: {results[0]}")
print(f"Full boolean table: {results[1]}")
print_selected_items(boolean_list=results[1], items_list=items_list)


