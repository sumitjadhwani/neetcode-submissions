class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = []
        for s in strs:
            encoded_string.append(f"{len(s)}#{s}")
        return "".join(encoded_string)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        decoded_strs = []
        i = 0
        
        while i < len(s):
            # Find the delimiter
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract length and the string itself
            length = int(s[i:j])
            string_start = j + 1
            string_end = string_start + length
            
            decoded_strs.append(s[string_start:string_end])
            
            # Move pointer forward
            i = string_end
            
        return decoded_strs