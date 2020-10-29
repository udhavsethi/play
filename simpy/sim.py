import simpy
import random

from constants import *
from queue import PriorityQueue


class Transaction:
    def __init__(self, timestamp, type):
        self.type = type
        self.deadline = timestamp + SLACK * EXECTIME[type][NFREQ-1]   # exec time at highest freq level
        self.start_time = 0
        self.pending_work = 0


class Generator(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())   # Start the run process everytime an instance is created.

    def run(self):
        global arrival
        while True:
            trx = Transaction(env.now, random.randint(0, 3))    # randomly chosen trx type
            print("t =", env.now, "gen: push trx {}, {} to queue".format(trx.type, trx.deadline))
            transactionQueue.put((trx.deadline, trx))   # EDF order
            arrival.succeed()
            arrival = self.env.event()
            print("t =", env.now, "gen: sleep for", THINKTIME)
            yield self.env.timeout(THINKTIME)


class Worker(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        global completion
        while True:
            if not transactionQueue.empty():
                state_snapshot = get_state_snapshot(transactionQueue.queue)
                print(state_snapshot)
                print("t =", env.now, "wor: Try dequeue")
                nextTrx = transactionQueue.get()[1]
                print("t =", env.now, "wor: got trx {}, {} from queue".format(nextTrx.type, nextTrx.deadline))
                chosenFreq = random.randint(0, NFREQ-1)   # randomly chosen freq
                print("t =", env.now, "wor: choose freq to run:", chosenFreq)
                completion = self.env.process(self.execute_trx(nextTrx, chosenFreq))
            yield arrival | completion
            # Interrupt the running trx, if any: check if completion is a "process" and has been triggered
            if hasattr(completion, 'is_alive') and not completion.triggered:
                print("t =", env.now, "wor: interrupting trx {}, {} execution".format(nextTrx.type, nextTrx.deadline))
                completion.interrupt('recompute frequency')
                self.update_pending_trx(nextTrx, chosenFreq)
            else:
                completion = self.env.event()   # reset completion event if triggered

    def execute_trx(self, trx, freq):
        try:
            # check if resuming trx
            if trx.pending_work > 0:
                exec_time = trx.pending_work / FLEVELS[freq]
                print("t =", env.now, "wor: resume trx {}, {}".format(trx.type, trx.deadline))
            else:
                exec_time = EXECTIME[trx.type][freq]
                trx.start_time = self.env.now
            print("t =", env.now, "wor: run trx for", exec_time)
            yield self.env.timeout(exec_time)
            print("t =", env.now, 'wor: trx completed execution')
        except simpy.Interrupt:
            pass

    def update_pending_trx(self, trx, freq):
        # record remaining work for transaction
        elapsed_time = self.env.now - trx.start_time
        trx.pending_work = (EXECTIME[trx.type][freq] - elapsed_time) * FLEVELS[freq]
        # Add pending transaction to top of transaction queue (priority=0)
        transactionQueue.put((0, trx))


def get_state_snapshot(transactionList):
    num_transactions = len(transactionList)
    state_snapshot = []
    backlog = (len(transactionList) - NSLOTS) if len(transactionList) > NSLOTS else 0
    state_snapshot.append(backlog)      # backlog
    for i in range(num_transactions):
        state_snapshot.append(transactionList[i][1].type)   # trx type
        state_snapshot.append(transactionList[i][1].deadline - env.now)     # time until deadline
    return state_snapshot


env = simpy.Environment()
transactionQueue = PriorityQueue()
# TODO: review global vars
arrival = env.event()
completion = env.event()
gen = Generator(env)
worker = Worker(env)
env.run(until=SIMTIME)
