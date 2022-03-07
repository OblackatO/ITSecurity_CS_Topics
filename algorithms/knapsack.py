# 0/1 KnapSack problem overview: https://en.wikipedia.org/wiki/Knapsack_problem

from typing import List

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
    for weight_index in range(0, KnapSackItem.BAG_MAX_WEIGHT): # weights are the columns
        optimal_weight.append([])
        for item_index in range(0, len(list_items)): # items are the rows
            if weight_index == 0:
                optimal_weight[weight_index].append(0)
                continue
            print(f"optimal_weight so far: {optimal_weight}")
            item_weight = list_items[item_index].weight
            item_value = list_items[item_index].value
            if weight_index >= item_weight:
                optimal_value = max(
                    optimal_weight[weight_index-1][item_index-1],
                    item_value+optimal_weight[weight_index-item_weight][item_index-1]
                )
            else:
                optimal_value = optimal_weight[weight_index-1][item_index-1]
            optimal_weight[weight_index].append(optimal_value)
    return optimal_weight

items_list = [KnapSackItem(3, 2), KnapSackItem(5, 4), KnapSackItem(7, 3), KnapSackItem(4, 6)]
print(build_weights_table(items_list))

