Explanation:
Initialization: Start by initializing the first substring and updating the frequency map.
Sliding Window: For each subsequent position, update the current window by removing the first character and adding the next character in the sequence.
Frequency Update: Update the frequency map and track the maximum frequency substring as before.
Complexity Analysis:
Time Complexity: 
𝑂
(
𝑛
)
O(n)
Constructing each new substring in the sliding window takes 
𝑂
(
1
)
O(1) time because it involves removing the first character and appending the next character.
The loop runs 
𝑛
−
𝑘
+
1
n−k+1 times, which is 
𝑂
(
𝑛
)
O(n).
Space Complexity: 
𝑂
(
𝑛
)
O(n)
In the worst case, all substrings of length 
𝑘
k are unique and stored in the dictionary.
This approach efficiently reduces the complexity to 
𝑂
(
𝑛
)
O(n) by leveraging the sliding window technique.