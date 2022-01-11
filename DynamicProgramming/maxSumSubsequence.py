def find_max_sum_nonadjacent(a):
  def repeating_max(i, end, a):
    if i > end:
      return 0
    if i == end-1 or i == end - 2:
      return max(0, a[i])

    if a[i] > 0:
      return a[i] + repeating_max(i+2, end, a)
    return repeating_max(i+1, end, a)

  
  return repeating_max(0, len(a)-1, a)


def find_max_sum_nonadjacentdp(a):
    def repeating_max(i, end, a):
        if i > end:
            return 0
        if i == end-1 or i == end - 2:
            return max(0, a[i])
        if dp[i] != -1000:
            return dp[i]
        if a[i] > 0:
            dp[i] = a[i] + repeating_max(i+2, end, a)
        else:
            dp[i] = repeating_max(i+1, end, a)
        return dp[i]

    dp = [-1000] * (len(a)-1)
    return repeating_max(0, len(a)-1, a)

assert(find_max_sum_nonadjacentdp([1, 6, 10, 14, 50, -20, -5, -10]) == 61)