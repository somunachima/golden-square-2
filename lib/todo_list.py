class TodoList:
    def __init__(self):
        self.list = []

    def add(self, todo):
        self.list.append(todo)

    def incomplete(self):
        task_list = []
        for todo in self.list:
            if todo.completed == False:
                task_list.append(todo.task)
        return ", ".join(task_list)

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_task_list = []
        for todo in self.list:
            if todo.completed == True:
                complete_task_list.append(todo.task)
        return ", ".join(complete_task_list)

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        # marked_all_complete = []
        for todo in self.list:
            todo.mark_complete()
        return self.list

