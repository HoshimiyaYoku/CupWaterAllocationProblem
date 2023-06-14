from collections import deque

def divide_water(cup_volumes, cup_water, divisions):
    total_water = sum(cup_water)
    if total_water % divisions != 0:
        #print("无法整除")
        return None, 0  # 无解

    target_water = total_water // divisions
    
    #if(target_water) > min(cup_volumes):
        #print("杯子太小")
        #return None, 0  # 无解
        #这段剪枝是错误的，但是此处暂时不想更新

    # 初始状态的初始化
    initial_state = tuple(cup_water)

    # 初始化队列和已访问状态集合
    queue = deque([initial_state])
    visited = set([initial_state])

    # 记录状态转移路径和步数
    prev_state = {initial_state: None}
    steps = {initial_state: 0}

    # BFS
    while queue:
        state = queue.popleft()

        # 检查是否达到目标状态
        if sum(c == target_water for c in state) == divisions and sum(state) == total_water:
            # 构建转移路径
            path = []
            while state:
                path.append(state)
                state = prev_state[state]
            path.reverse()
            return path, steps[path[-1]]

        #print("current_state:", state)

        # 尝试所有可能的倒水操作
        for i in range(len(cup_volumes)):
            for j in range(len(cup_volumes)):
                if i != j:
                    # 同一个杯子不能倒水
                    # 计算可倒入的最大水量
                    max_pour = min(state[i], cup_volumes[j] - state[j])

                    # 生成新状态
                    new_state = list(state)
                    new_state[i] -= max_pour
                    new_state[j] += max_pour
                    new_state = tuple(new_state)

                    # 标记
                    if new_state not in visited:
                        queue.append(new_state)
                        visited.add(new_state)
                        prev_state[new_state] = state
                        steps[new_state] = steps[state] + 1

                        #print("new_stete:", new_state)

    return None, 0  # 无解

# 输入
N = int(input("コップの数N:"))
cup_volumes = []
cup_water = []
for i in range(N):
    volume = int(input(f"第 {i+1} 個コップのサイズ："))
    cup_volumes.append(volume)
for i in range(N):
    water = int(input(f"第 {i+1} 個コップの水の量："))
    cup_water.append(water)
divisions = int(input("何等分したい？"))

result, num_steps = divide_water(cup_volumes, cup_water, divisions)
if result:
    print(f" {num_steps} 歩が必要：")
    for state in result:
        print(state)
else:
    print("均等分割ができない")

