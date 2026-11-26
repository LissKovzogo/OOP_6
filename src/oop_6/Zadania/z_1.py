'''
9. Список задач (TODO-list)
Создайте датакласс Task с полями:
текст задачи, приоритет, статус выполнения.
Выведите только невыполненные задачи, отсортированные по приоритету.
'''
from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    text: str
    priority: int
    is_completed: bool = False

@dataclass
class TaskList:
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def get_incomplete_sorted_by_priority(self) -> List[Task]:
        incomplete_tasks = [task for task in self.tasks if not task.is_completed]
        sorted_tasks = sorted(incomplete_tasks, key=lambda t: t.priority, reverse=True)
        return sorted_tasks

if __name__ == "__main__":
    my_todo_list = TaskList()
    task1 = Task("Купить продукты", priority=2)
    task2 = Task("Сдать лабораторную работу", priority=5)
    task3 = Task("Помыть посуду", priority=1, is_completed=True)
    task4 = Task("Позвонить маме", priority=4)

    my_todo_list.add_task(task1)
    my_todo_list.add_task(task2)
    my_todo_list.add_task(task3)
    my_todo_list.add_task(task4)

    result_tasks = my_todo_list.get_incomplete_sorted_by_priority()

    print("Невыполненные задачи:")
    for task in result_tasks:
        print(f"[{task.priority}] {task.text}")