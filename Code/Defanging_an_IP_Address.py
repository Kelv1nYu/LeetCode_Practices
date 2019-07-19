class Solution:
    def defangIPaddr(self, address: str) -> str:
        nums = address.split(".")
        str2 = nums[0] + "[.]" + nums[1] + "[.]" + nums[2] + "[.]" + nums[3]
        return str2