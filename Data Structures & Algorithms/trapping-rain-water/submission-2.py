class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointers
        
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        m_pref = height[0]
        for i in range(len(height)):
            m_pref = max(height[i], m_pref)
            prefix[i] = m_pref

        m_suff = height[-1]
        for i in range(len(height)-1, -1, -1):
            m_suff = max(height[i], m_suff)
            suffix[i] = m_suff

        area = 0
        for i in range(len(height)):
            area += min(prefix[i], suffix[i]) - height[i]
        return area