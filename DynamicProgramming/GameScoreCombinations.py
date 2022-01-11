def scoring_options(n):
  def need(n):
    if n < 1:
      return 0
    if n == 1:
      return 1
    if n == 2:
      return 2
    if n == 4:
      return 1 + need(n-2) + need(n-1)

    return need(n-1) + need(n-2) + need(n-4)
  return need(n)

def scoring_optionsDP(n):
  def need(n):
    if n < 1:
      return 0
    if n in dp:
        return dp[n]
    if n == 4:
        if n not in dp:
            dp[n] = 1 + need(n-2) + need(n-1)
        return dp[n]

    dp[n] = need(n-1) + need(n-2) + need(n-4)
    return dp[n]
    
  dp = {}
  dp[1] = 1
  dp[2] = 2
  return need(n)


assert(scoring_options(4) == 6)
assert(scoring_options(5) == 10)

assert(scoring_optionsDP(4) == 6)
assert(scoring_optionsDP(5) == 10)