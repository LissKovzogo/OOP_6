from dataclasses import dataclass
from typing import Any

@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42

print(WithoutExplicitTypes(3.14, 'pi day'))
