class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}

        for word in strs:
            # Use the sorted version of the word as the key
            key = ''.join(sorted(word))
            
            # Add the word to the corresponding group
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]

        # Extract the groups and return as a list of lists
        return list(anagrams.values())