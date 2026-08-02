class Solution:
    def isOverSixty(self, citizen):
        age = int(citizen[11:13])
        return age > 60

    def countSeniors(self, details: List[str]) -> int:
        filteredCitizens = filter(self.isOverSixty, details)
        return len(list(filteredCitizens))