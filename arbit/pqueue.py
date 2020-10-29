from queue import PriorityQueue


class Transaction:
    def __init__(self, timestamp, type):
        self.type = type
        self.deadline = timestamp + 5

    def __gt__(self, other):
        return True if self.deadline > other.deadline else False


transactionQueue = PriorityQueue()
trx1 = Transaction(1, 1)
trx2 = Transaction(2, 1)

transactionQueue.put((0, trx1))
transactionQueue.put((0, trx2))

t1 = transactionQueue.get()
print(t1.deadline)
t2 = transactionQueue.get()
print(t2.deadline)
