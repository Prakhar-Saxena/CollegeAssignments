import sys

import qlearn as qlearn

command = str(sys.argv[1])

env = qlearn.Env(qlearn.DEFAULT_STATE)

if len(sys.argv) > 2:
    envString = str(sys.argv[2])
    env = qlearn.Env(envString)

qTable = qlearn.QTable(env, qlearn.ACTIONS)

if command == "learn":
    qTable.learn(100)
