class Solution:
    def findRestaurant(self, list1, list2):
        index_sum = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    index_sum[list1[i]] = i + j

        min_sum = min(index_sum.values())
        result = []
        for restaurant, sum in index_sum.items():
            if sum == min_sum:
                result.append(restaurant)

        return result
