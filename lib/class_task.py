class ClassTask:
    def __init__(self):
        self.todo = []
        self.complete = False

    def add(self, task):
        self.todo.append(task)
        return self.list()

    def list(self):
        return ", ".join(self.todo)
    
    def mark_completed(self, task):
        if task in self.todo:
            self.todo.remove(task)
        else:
            raise Exception("No such task exists")
        return self.list()