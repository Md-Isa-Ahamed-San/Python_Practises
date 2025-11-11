# Minimum Distance Between Three Equal Elements I
def minimumDistance(nums) -> int:
    ds = {}
    min_dist = 999999999999999999
    for idx, value in enumerate(nums):
        if value not in ds:
            ds[value] = [idx]
        else:
            ds[value].append(idx)
            if len(ds[value]) >= 3:
                last_idx = ds[value][-1]
                second_last_idx = ds[value][-2]
                third_last_idx = ds[value][-3]
                dist = (
                    abs(third_last_idx - second_last_idx)
                    + abs(second_last_idx - last_idx)
                    + abs(last_idx - third_last_idx)
                )
                if dist < min_dist:
                    min_dist = dist

    print(min_dist)
    return min_dist if min_dist != 999999999999999999 else -1


minimumDistance([1, 2, 1, 1, 3])
# minimumDistance([1,1,2,3,2,1,2])
# minimumDistance([5, 3, 5, 5, 5])
minimumDistance([4, 4, 3, 4, 3, 3, 4, 4, 4, 4])
