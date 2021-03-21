from collections import Counter


class ShiftUtility:

    @staticmethod
    def check_for_optimum_result_two_shifts(shift, partition):
        partition_type = "two"
        if shift == (7, 3) or shift == (3, 7):
            count_A, count_B, distinct_elements_A, distinct_elements_B = ShiftUtility.get_stats(partition, partition_type)
            if shift == (7, 3):
                if (max(count_A.values()) >= shift[0] - 2) and (max(count_A.values()) - len(distinct_elements_A) >= 2):
                    if max(count_B.values()) >= shift[1] - 1:
                        return True
            else:
                if max(count_A.values()) >= shift[0] - 1:
                    if (max(count_B.values()) >= shift[1] - 2) and (
                            max(count_B.values()) - len(distinct_elements_B) >= 2):
                        return True
        elif shift == (6, 4) or shift == (4, 6):
            count_A, count_B, distinct_elements_A, distinct_elements_B = ShiftUtility.get_stats(partition, partition_type)
            if shift == (6, 4):
                if (max(count_A.values()) >= shift[0] - 2) and (max(count_A.values()) - len(distinct_elements_A) >= 2):
                    if max(count_B.values()) >= shift[1] - 1:
                        return True
            else:
                if max(count_A.values()) >= shift[0] - 1:
                    if (max(count_B.values()) >= shift[1] - 2) and (
                            max(count_B.values()) - len(distinct_elements_B) >= 2):
                        return True
        else:
            count_A, count_B, distinct_elements_A, distinct_elements_B = ShiftUtility.get_stats(partition, partition_type)
            if (max(count_A.values()) >= shift[0] - 2) and (max(count_A.values()) - len(distinct_elements_A) >= 2):
                if (max(count_B.values()) >= shift[0] - 2) and (max(count_B.values()) - len(distinct_elements_B) >= 2):
                    return True
        return False


    @staticmethod
    def check_for_optimum_result_three_shifts(shift, partition):
        partition_type = "three"
        if shift == (3, 3, 4):
            count_A, count_B, distinct_elements_A, distinct_elements_B, count_C, distinct_elements_C = ShiftUtility().get_stats(partition, partition_type)
            if max(count_A.values()) == 2 and max(count_B.values()) == 2:
                if max(count_C.values()) >= shift[2] - 2 and len(distinct_elements_C) <= shift[2] - 1:
                    return True
        elif shift == (3, 4, 3):
            count_A, count_B, distinct_elements_A, distinct_elements_B, count_C, distinct_elements_C = ShiftUtility().get_stats(
                partition, partition_type)
            if max(count_A.values()) == 2 and max(count_C.values()) == 2:
                if max(count_B.values()) >= shift[1] - 2 and len(distinct_elements_B) <= shift[1] - 1:
                    return True
        else:
            count_A, count_B, distinct_elements_A, distinct_elements_B, count_C, distinct_elements_C = ShiftUtility().get_stats(
                partition, partition_type)
            if max(count_B.values()) == 2 and max(count_C.values()) == 2:
                if max(count_A.values()) >= shift[0] - 2 and len(distinct_elements_A) <= shift[0] - 1:
                    return True

        return False

    @staticmethod
    def get_stats(partition, partition_type):
        if partition_type == "two":
            count_A = Counter(partition[0])
            distinct_elements_A = set(partition[0])
            count_B = Counter(partition[1])
            distinct_elements_B = set(partition[1])
            return count_A, count_B, distinct_elements_A, distinct_elements_B
        else:
            count_A = Counter(partition[0])
            distinct_elements_A = set(partition[0])
            count_B = Counter(partition[1])
            distinct_elements_B = set(partition[1])
            count_C = Counter(partition[2])
            distinct_elements_C = set(partition[2])
            return count_A, count_B, distinct_elements_A, distinct_elements_B, count_C, distinct_elements_C

