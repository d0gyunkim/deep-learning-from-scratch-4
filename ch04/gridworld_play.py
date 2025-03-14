import numpy as np
from gridworld import GridWorld

env = GridWorld()
V = {}
for state in env.states():
    V[state] = np.random.randn()  # 더미 상태 가치 함수
env.render_v(V)
