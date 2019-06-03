import qlearn as qlearn

e = qlearn.Env(qlearn.DEFAULT_STATE)

qT = qlearn.QTable(e,qlearn.ACTIONS)

# qT.learn_episode()
qT.learn(100)
# qT.learn(5)
print(qT)