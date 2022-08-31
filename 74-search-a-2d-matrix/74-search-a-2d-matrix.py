class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix)-1
        columns = len(matrix[0])
    
        while(low<=high):
            mid = (low+high)//2
            
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0]>target:
                high = mid - 1
            if matrix[mid][0]<target:
                low = mid + 1
            for i in range(1,columns):
                if matrix[mid][i] == target:
                    return True
            
        return False
                