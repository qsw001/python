#对于环境,我们首先要确定地图，

class Env:
    def __init__(self):
        self.map = [
            ['S', '.', '.', '.', '.', 'C'],
            ['.', '#', '.', '#', '.', '.'],
            ['.', '#', '.', '.', '.', '.'],
            ['.', '.', '.', '#', '.', '.'],
            ['C', '.', '.', '.', '#', '.'],
            ['.', '.', '.', '.', '.', 'G']
        ]

        self.colMap = len(map[0])
        self.rowMap = len(map)

        self.actions = {
            0: (1,0),
            1: (0,1),
            2: (-1,0),
            3: (0,-1),
        }

        self.done = False

        self.steps = 0
        self.maxsteps = 100

    #改为更像函数的形式
    # def posChest(self):
    #     for i in range(self.rowMap):
    #         for j in range(self.colMap):
    #             if self.map[i-1][j-1] == 'C':

    def findPos(self, target):
        for i in range(self.rowMap):
            for j in range(self.colMap):
                if self.map[i][j] == target:
                    return (i,j)
        return None
    
    #
    def step(self, action):
        #算出下一步的状态
        dx, dy = self.actions[action]
        x, y = self.findPos('S')
        nx, ny = x + dx, y + dy 

        if (nx, ny) == self.findPos('G'):
            self.done = True
            return (x, y), reward

        #游戏没结束的话，步数和奖励变化
        if not self.done:
            self.steps + 1
            reward = -1
        
        #撞墙扣分
        if (nx, ny) == self.findPos('#'):
            reward -= 5
            return (x, y), reward
        
        #出界扣分
        if not (0 <= nx < self.rowMap and 0 <= ny < self.colMap):
            reward -= 5
            return (x, y), reward

        #吃到宝箱加分
        if self.findPos('C'):
            reward += 50
            return (nx, ny), reward
        
        #到达终点加分
        if self.findPos('G'):
            reward += 100
            return (nx, ny), reward
        
        
        