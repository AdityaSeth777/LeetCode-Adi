from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_path = defaultdict(list)
        for path in paths:
            directory, *files = path.split()
            for file in files:
                filename, content = file.split("(")
                content = content[:-1]
                full_path = directory + "/" + filename
                content_to_path[content].append(full_path)

        return [group for group in content_to_path.values() if len(group) > 1]