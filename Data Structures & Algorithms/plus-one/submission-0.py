class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_string = ''.join(map(str,digits))
        new_number = int(new_string)
        new_number+=1
        res_array = []
        for c in str(new_number):
            res_array.append(int(c))
            
        return res_array
        
        