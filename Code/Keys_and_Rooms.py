class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        # generate a set to store dfs node
        visited = set()
        
        # dfs function
        def dfs(room):
            if room not in visited:
                visited.add(room)

                # get key from current room and go to next room by dfs function
                for key in rooms[room]:
                    dfs(key)
        
        # start dfs
        dfs(0)
        return len(visited) == len(rooms)