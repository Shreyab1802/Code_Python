class NoActiveTransactionException(Exception):
    pass

class DatabaseSimulator:
    def __init__(self):
        self.permanent_storage = {}
        self.transaction_stack = []

    def begin(self):
        self.transaction_stack.append({})

    def get(self, key):
        if not self.transaction_stack:
            return self.permanent_storage.get(key)
        for transaction in reversed(self.transaction_stack):
            if key in transaction:
                return transaction.get(key)
        return self.permanent_storage.get(key)

    def set(self, key, value):
        if not self.transaction_stack:
            raise NoActiveTransactionException("No active transaction")
        self.transaction_stack[-1][key] = value

    def count(self):
        return len(self.permanent_storage)

    def commit(self):
        if not self.transaction_stack:
            raise NoActiveTransactionException("No active transaction")
        final_changes = self.transaction_stack[0]
        for transaction in self.transaction_stack[1:]:
            final_changes.update(transaction)
        self.permanent_storage.update(final_changes)
        self.transaction_stack.clear()

    def rollback(self):
        if not self.transaction_stack:
            raise NoActiveTransactionException("No active transaction")
        self.transaction_stack.pop()

db = DatabaseSimulator()

# Begin a transaction
db.begin()

# Set a key-value pair
db.set("a", "value1")

# Get the value of a key
print(db.get("a"))  # Output: "value1"

# Begin another transaction
db.begin()

# Set another key-value pair
db.set("b", "value2")

# Get the value of a key
print(db.get("b"))  # Output: "value2"

# Rollback the transaction
db.rollback()

# The value of key "b" should be None after rollback
print(db.get("b"))  # Output: None

# Commit the transaction
db.commit()

# The value of key "a" should be "value1" after commit
print(db.get("a"))  # Output: "value1"

# Count the number of keys in the permanent storage
print(db.count())  # Output: 1
