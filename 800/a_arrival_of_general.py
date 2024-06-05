n = int(input())
heights = list(map(int, input().split()))

def min_swap(n, heights):
    left_index = heights.index(max(heights))
    
    right_index = n - 1 - heights[::-1].index(min(heights))
    
    swap = left_index + (n - 1 - right_index)
    
    if left_index > right_index:
        swap -= 1
        
    return swap

print(min_swap(n, heights))
