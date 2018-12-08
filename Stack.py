class Stack:
    def __init__(self, initial_capacity):
        self.length_ = initial_capacity
        self.array_ = self.length_ * [0]
        self.top_ = -1

    def increase_capacity(self):
        new_length = 1 if self.length_ == 0 else 2 * self.length_
        old_array = self.array_
        self.array_ = new_length * [0]
        for i in range(self.length_):
            self.array_[i] = old_array[i]
        self.length_ = new_length

    def empty(self):
        return self.top_ == -1

    def push(self, x):
        if self.top_ == self.length_: 
            print('stack overflow')
        if self.empty(): self.increase_capacity()
        self.top_ += 1
        self.array_[self.top_] = x

    def pop(self):
        if self.empty(): 
            print('stack underflow')
            return
        self.top_ -=1
        return self.array_[self.top_ + 1]

    def as_list(self):
        return self.array_[0:(self.top_ + 1)]

    def __str__(self):
        return "Stack: %s" % (str(self.as_list()))
        