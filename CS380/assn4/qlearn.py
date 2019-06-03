import random
import sys
from random import randint


DEFAULT_STATE = '       | ###  -| # #  +| # ####|       '


class Action:

    def __init__(self, name, dx, dy):
        self.name = name
        self.dx = dx
        self.dy = dy


ACTIONS = [
    Action('UP', 0, -1),
    Action('RIGHT', +1, 0),
    Action('DOWN', 0, +1),
    Action('LEFT', -1, 0)
]


class State:

    def __init__(self, env, x, y):
        self.env = env
        self.x = x
        self.y = y

    def clone(self):
        return State(self.env, self.x, self.y)

    def is_legal(self, action):
        cell = self.env.get(self.x + action.dx, self.y + action.dy)
        return cell is not None and cell in ' +-'
    
    def legal_actions(self, actions):
        legal = []
        for action in actions:
            if self.is_legal(action):
                legal.append(action)
        return legal
    
    def reward(self):
        cell = self.env.get(self.x, self.y)
        if cell is None:
            return None
        elif cell == '+':
            return +10
        elif cell == '-':
            return -10
        else:
            return 0

    def at_end(self):
        return self.reward() != 0

    def execute(self, action):
        self.x += action.dx
        self.y += action.dy
        return self

    def __str__(self):
        tmp = self.env.get(self.x, self.y)
        self.env.put(self.x, self.y, 'A')
        s = ' ' + ('-' * self.env.x_size) + '\n'
        for y in range(self.env.y_size):
            s += '|' + ''.join(self.env.row(y)) + '|\n'
        s += ' ' + ('-' * self.env.x_size)
        self.env.put(self.x, self.y, tmp)
        return s


class Env:

    def __init__(self, string):
        self.grid = [list(line) for line in string.split('|')]
        self.x_size = len(self.grid[0])
        self.y_size = len(self.grid)

    def get(self, x, y):
        if x >= 0 and x < self.x_size and y >= 0 and y < self.y_size:
            return self.grid[y][x]
        else:
            return None

    def put(self, x, y, val):
        if x >= 0 and x < self.x_size and y >= 0 and y < self.y_size:
            self.grid[y][x] = val

    def row(self, y):
        return self.grid[y]

    def random_state(self):
        x = random.randrange(0, self.x_size)
        y = random.randrange(0, self.y_size)
        while self.get(x, y) != ' ':
            x = random.randrange(0, self.x_size)
            y = random.randrange(0, self.y_size)
        return State(self, x, y)


class QTable:

    def __init__(self, env, actions):
        # initialize your q table
        self.env = env
        self.actions = actions
        self.table = []
        for action in actions:
            self.table.append( [ action.name , [ [0 for i in range(env.x_size)] for j in range(env.y_size)] ] )
    
    def get_q(self, state, action):
        # return the value of the q table for the given state, action
        qValues = self.get_q_row_with_action(state)
        for qValue in qValues:
            if qValue[0] == action.name:
                return qValue[1]

    def get_q_row_with_action(self, state):
        # return the row of q table corresponding to the given state
        l = []
        for i in self.table:            
            l.append([i[0],i[1][state.y][state.x]])
        return l

    def get_q_row(self, state):
        # return the row of q table corresponding to the given state
        l = []
        for i in self.table:            
            l.append(i[1][state.y][state.x])
        return l

    def set_q(self, state, action, val):
        # set the value of the q table for the given state, action
        for i in self.table:
            if i[0] == action.name:
                i[1][state.y][state.x] = val
        # actionIndex = self.actions.index(action)
        # self.table[actionIndex][state.y][state.x] = val

    def learn_episode(self, alpha=.10, gamma=.90):
        # with the given alpha and gamma values,
        # from a random initial state,
        nextState = self.env.random_state()
        originalState = nextState.clone()

        # consider a random legal action, execute that action,

        # compute the reward, and update the q table for (state, action).

        # repeat until an end state is reached (thus completing the episode)
        # also print the state at each state
        while(not nextState.at_end()):
            legalActions = nextState.legal_actions(ACTIONS)
            actionIndex = randint(0, len(legalActions)-1)
            randomAction = legalActions[actionIndex]
            nextState.execute(randomAction)
            reward = nextState.reward()
            getQ = self.get_q(originalState, randomAction)
            maxQ = max(self.get_q_row(nextState))
            qValue = ( (1-alpha) * getQ ) + ( alpha * (reward + (gamma * maxQ ) ) )
            self.set_q(originalState, randomAction, qValue)
            originalState = nextState.clone()
            print(nextState)
    
    def learn(self, episodes, alpha=.10, gamma=.90):
        # run <episodes> number of episodes for learning with the given alpha and gamma
        for i in range(episodes):
            self.learn_episode(alpha,gamma)

    def __str__(self):
        # return a string for the q table as described in the assignment
        s = ''
        for a in self.table:
            s += a[0] + '\n'
            for y in a[1]:
                for x in y:
                    if x == 0:
                        s += '---- '
                    else:
                        s += str(round(x,2)) + ' '
                s += '\n'
        return s

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        env = Env(sys.argv[2] if len(sys.argv) > 2 else DEFAULT_STATE)
        if cmd == 'learn':
            qt = QTable(env, ACTIONS)
            qt.learn(100)
            print(qt)
