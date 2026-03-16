from env import TreasureHuntEnv
from q_learning import QLearningAgent


def test_agent(model_path="q_table.pkl", episodes=5, render=True):
    env = TreasureHuntEnv()
    agent = QLearningAgent(action_dim=4)
    agent.load(model_path)

    total_rewards = []

    for episode in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0

        print(f"\n===== 测试第 {episode + 1} 局 =====")

        if render:
            env.render()

        while not done:
            action = agent.greedy_action(state)
            next_state, reward, done, info = env.step(action)

            state = next_state
            total_reward += reward

            print(
                f"动作: {action}, 奖励: {reward}, "
                f"步数: {info['steps']}, 宝箱: {info['collected_chests']}"
            )

            if render:
                env.render()

        total_rewards.append(total_reward)

        print(f"本局总奖励: {total_reward}")
        print(f"总步数: {info['steps']}")
        print(f"收集宝箱数: {info['collected_chests']}")

    avg_reward = sum(total_rewards) / len(total_rewards)
    print("\n===== 测试结束 =====")
    print(f"平均奖励: {avg_reward}")


if __name__ == "__main__":
    test_agent()