class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        c={0}
        stack=[0]
        while(stack):
            i=stack.pop()
            for j in rooms[i]:
                if (j not in c):
                    c.add(j)
                    stack.append(j)
        if(len(c)==len(rooms)):
            return True
        else:
            return False




            