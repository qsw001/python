#主函数

#从...模块导入...类
from env import TreasureHuntEnv
from q_learning import QLearningAgent

def train():
    #实例化类
    env = TreasureHuntEnv()
    agent = QLearningAgent(action_dim=4, alpha=0.1, gamma=0.99, epsilon=0.3)

    #设置训练次数
    episodes = 3000000

    #进入训练
    for episode in range(episodes):
        #初始化地图状态
        state = env.reset()
        total_reward = 0

        #进入寻路循环
        while not env.done:
            #分为三个步骤
            #1.获取下一步的action
            #2.进行下一步操作
            #3.更新q值表
            action = agent.choose_action(state)
            next_state, reward, done, info = env.step(action)
            agent.update(state, action, reward, next_state, done)

            state = next_state
            total_reward += reward

        #加入判断获得结果
        # if len(env.collected_chests) == 2:
        #     print("第{}轮拿到了两个宝箱".format(episode+1))
        #     print(
        #         f"Episode {episode + 1}, "
        #         f"total_reward = {total_reward}, "
        #         f"steps = {info['steps']}, "
        #         f"chests = {info['collected_chests']}"
        #     )

        if (episode + 1) % 10000 == 0:
            print(
                f"Episode {episode + 1}, "
                f"total_reward = {total_reward}, "
                f"steps = {info['steps']}, "
                f"chests = {info['collected_chests']}"
            )

        #观察当出现多个宝箱时它的情况

    agent.save("q_table.pkl")
    print("训练完成，Q表已保存到 q_table.pkl")


if __name__ == "__main__":
    train()
