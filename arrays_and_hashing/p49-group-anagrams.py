class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagrams = {}

        # Loop runs n times (see time complexity)
        for word in strs:
            # Create an array of counts for each letter in the alphabet
            counts = [0] * 26
            
            # Loop runs at most k times (see time complexity)
            for char in word:
                # Get index of letter (using ASCII mappings)
                counts[ord(char) - ord('a')] += 1

            if anagrams.get(tuple(counts)):
                anagrams[tuple(counts)].append(word)
            else:
                anagrams[tuple(counts)] = [word]
        
        return anagrams.values()

        # Time Complexity: O(n * k) - n is the length of str, k is the maximum length of a string in strs
        # Space Complexity: O(n * k) - total information content stored in 'anagrams'