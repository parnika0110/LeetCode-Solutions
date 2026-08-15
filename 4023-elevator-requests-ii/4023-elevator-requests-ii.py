class Solution:
    def elevatorRequests(self, n: int, start: int, requests: List[int]) -> int:
        a = sorted(set(requests + [start]))
        m = len(a)
        req = set(requests)
        w = [1 if x in req else 0 for x in a]
        pref = [0] * (m + 1)
        for i in range(m):
            pref[i + 1] = pref[i] + w[i]
        p = a.index(start)
        INF = 10**18
        dpL = [INF] * m
        dpR = [INF] * m
        dpL[p] = 0
        dpR[p] = 0

        total_requests = len(requests)

        for length in range(1, m):
            ndpL = [INF] * m
            ndpR = [INF] * m
            lo = max(0, p - length + 1)
            hi = min(p, m - length)

            for l in range(lo, hi + 1):
                r = l + length - 1
                fulfilled = pref[r + 1] - pref[l]
                remaining = total_requests - fulfilled

                left_cost = dpL[l]
                right_cost = dpR[l]
                if l > 0:
                    ndpL[l - 1] = min(
                        ndpL[l - 1],
                        left_cost + (a[l] - a[l - 1]) * remaining,
                        right_cost + (a[r] - a[l - 1]) * remaining
                    )
                if r + 1 < m:
                    ndpR[l] = min(
                        ndpR[l],
                        left_cost + (a[r + 1] - a[l]) * remaining,
                        right_cost + (a[r + 1] - a[r]) * remaining
                    )

            dpL, dpR = ndpL, ndpR

        return min(dpL[0], dpR[0])