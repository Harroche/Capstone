def calc(A, B):
    # Step 1: Compute prefix sum array
    n = len(A)
    prefix_sum = [0] * n
    prefix_sum[0] = A[0]
    
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]
    
    # Step 2: Process each query
    result = []
    
    for l, r in B:
        if l == 0:
            result.append(prefix_sum[r])
        else:
            result.append(prefix_sum[r] - prefix_sum[l - 1])
    
    return result
