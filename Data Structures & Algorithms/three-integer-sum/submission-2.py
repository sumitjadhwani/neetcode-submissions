class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        occ = {}
        for i,n in enumerate(nums):
            if n not in occ:
                occ[n]=[i]
            else:
                occ[n].append(i)
        length = len(nums)
        res = []
        for i,n in enumerate(nums):
            for j in range(i+1, length):
                target = -1 * (nums[i] + nums[j])
                if(target == nums[i] and len(occ[nums[i]])>1 and target!=0):
                    
                    res.append(sorted([nums[i],nums[j],target] ))
                elif(target == nums[j] and len(occ[nums[j]])>1 and target!=0):
                    
                    res.append(sorted([nums[i],nums[j],target]))
                elif occ.get(target) is not None and target != nums[i] and target!= nums[j]:
                    res.append(sorted([nums[i],nums[j],target]))
                elif (target == 0 and nums[i]==0 and len(occ[nums[i]])>2):
                    res.append([0,0,0])
                else:
                    continue
        # 1. Convert sublists to tuples and filter using a set
        unique_tuples = set(tuple(sublist) for sublist in res)

        # 2. Convert back to lists and print
        unique_lists = [list(t) for t in unique_tuples]
        print(unique_lists)

        
        return unique_lists
                

