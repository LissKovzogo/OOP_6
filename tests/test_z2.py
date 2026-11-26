import sys
import os

# tests/test_z2.py
import pytest
from oop_6.Zadania.z_2 import Queue


def test_queue_init_and_history():
    q = Queue()

    assert len(q) == 0
    assert len(q.get_history()) == 1
    assert q.get_history()[0] == "Инициализация очереди"


def test_queue_push_and_peek():
    q = Queue[str]()

    q.push("Первый")
    q.push("Второй")

    assert len(q) == 2

    assert q.peek() == "Первый"
    assert len(q) == 2

    history = q.get_history()
    assert "push('Первый')" in history
    assert "push('Второй')" in history
    assert "peek() -> 'Первый'" in history


def test_queue_pop_fifo():
    q = Queue[int]()

    q.push(10)
    q.push(20)
    q.push(30)

    assert q.pop() == 10
    assert q.pop() == 20
    assert q.pop() == 30

    assert len(q) == 0


def test_queue_pop_empty():
    q = Queue[float]()

    result = q.pop()

    assert result is None
    assert len(q) == 0

    history = q.get_history()
    assert "pop() -> пустая очередь" in history


def test_queue_peek_empty():
    q = Queue[bool]()

    result = q.peek()

    assert result is None
    assert len(q) == 0
    assert "peek() -> пустая очередь" in q.get_history()


def test_queue_repr_hidden_fields(capsys):
    q = Queue[str]()
    q.push("Тест")

    print(q)
    captured = capsys.readouterr()

    assert "_items" not in captured.out
    assert "history" not in captured.out
    assert "Queue(" in captured.out


def test_queue_generic_typing():
    q_int = Queue[int]()
    q_str = Queue[str]()

    q_int.push(42)
    q_str.push("Ответ")

    assert q_int.peek() == 42
    assert q_str.peek() == "Ответ"

