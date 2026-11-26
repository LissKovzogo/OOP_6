import sys
import os
# tests/test_z1.py
import pytest
from oop_6.Zadania.z_1 import Task, TaskList


def test_task_creation_valid():

    task = Task(text="Купить хлеб", priority=2)
    assert task.text == "Купить хлеб"
    assert task.priority == 2
    assert not(task.is_completed)

def test_task_creation_completed():
    task = Task(text="Помыть посуду", priority=1, is_completed=True)
    assert task.is_completed


def test_task_list_empty_init():
    todo = TaskList()
    assert len(todo.tasks) == 0
    assert isinstance(todo.tasks, list)


def test_add_task():
    todo = TaskList()
    task = Task(text="Сделать лабу", priority=5)

    todo.add_task(task)

    assert len(todo.tasks) == 1
    assert todo.tasks[0] == task


def test_get_incomplete_sorted_by_priority():
    todo = TaskList()

    todo.add_task(Task(text="Низкий приоритет", priority=1))
    todo.add_task(Task(text="Выполненная", priority=10, is_completed=True))
    todo.add_task(Task(text="Высокий приоритет", priority=5))
    todo.add_task(Task(text="Средний приоритет", priority=3))

    result = todo.get_incomplete_sorted_by_priority()

    assert len(result) == 3

    task_texts = [t.text for t in result]
    assert "Выполненная" not in task_texts
    assert result[0].priority == 5
    assert result[1].priority == 3
    assert result[2].priority == 1


def test_get_incomplete_when_all_completed():
    todo = TaskList()
    todo.add_task(Task(text="Задача 1", priority=2, is_completed=True))
    todo.add_task(Task(text="Задача 2", priority=1, is_completed=True))

    result = todo.get_incomplete_sorted_by_priority()

    assert len(result) == 0
    assert result == []


def test_get_incomplete_empty_list():
    todo = TaskList()
    result = todo.get_incomplete_sorted_by_priority()

    assert result == []