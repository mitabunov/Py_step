arr=[1,2,3,4,5]

# class FileManager:
#     def read(self, file):
#         with open(file) as f:
#             return f.read()
    
#     def write(self, file, data):
#         with open(file, 'a') as f:
#             f.write(data)            

class FromArraySearch:

    def summ_arr(self,arr):
        return sum(arr)

    def mean_arr(self,arr):
        return sum(arr)/len(arr)
            
    def max_arr(self, arr):
        return max(arr)

    def min_arr(self, arr):
        return min(arr)
