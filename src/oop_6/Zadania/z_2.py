'''
9. Очередь с историей операций
Создайте Queue(Generic[T]) с методами push, pop, peek.
Храните историю операций (строки) в скрытом поле history:
list[str] с repr=False.
'''
from dataclasses import dataclass, field
from typing import Generic, TypeVar, List, Optional
T = TypeVar('T')


@dataclass
class Queue(Generic[T]):
    _items: List[T] = field(default_factory=list, repr=False)
    history: List[str] = field(default_factory=list, repr=False)

    def __post_init__(self) -> None:

        self.history.append("Инициализация очереди")

    def push(self, item: T) -> None:
        self._items.append(item)
        self.history.append(f"push({item!r})")

    def pop(self) -> Optional[T]:
        if not self._items:
            self.history.append("pop() -> пустая очередь")
            return None

        item = self._items.pop(0)
        self.history.append(f"pop() -> {item!r}")
        return item

    def peek(self) -> Optional[T]:
        if not self._items:
            self.history.append("peek() -> пустая очередь")
            return None

        item = self._items[0]
        self.history.append(f"peek() -> {item!r}")
        return item

    def get_history(self) -> List[str]:
        return self.history.copy()

    def __len__(self) -> int:
        return len(self._items)

if __name__ == "__main__":
    string_queue: Queue[str] = Queue()

    string_queue.push("Первый")
    string_queue.push("Вторый")
    string_queue.push("Третий")

    print(f"Первый в очереди (peek): {string_queue.peek()}")
    print(f"Извлечен (pop): {string_queue.pop()}")
    print(f"Извлечен (pop): {string_queue.pop()}")

    print("\nРабота с очередью чисел")
    int_queue: Queue[int] = Queue()

    int_queue.push(10)
    int_queue.push(20)

    print(f"Первый в очереди (peek): {int_queue.peek()}")
    print(f"Извлечен (pop): {int_queue.pop()}")

    print("\nПроверка пустой очереди")
    empty_queue: Queue[float] = Queue()
    print(f"Pop из пустой: {empty_queue.pop()}")
    print(f"Peek из пустой: {empty_queue.peek()}")

    print("\nИстория операций для первой очереди")
    for event in string_queue.get_history():
        print(event)

    print("\nПроверка скрытого поля (repr=False)")
    print(f"Представление объекта: {string_queue}")