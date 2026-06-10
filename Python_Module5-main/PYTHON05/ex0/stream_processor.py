from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def counts(self, data: Any) -> int:
        cont: int = 0
        for i in data:
            cont += 1
        return cont

    def plus(self, data: Any) -> int:
        value: int = 0
        for i in data:
            value += i
        return value

    def validate(self, data: Any) -> bool:
        if data.__class__ == list:
            for x in data:
                if not (x.__class__ == int or x.__class__ == float):
                    return False
        else:
            return False
        return True

    def process(self, data: List[Union[int, float]]) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Numeric data verification failed")
            count = self.counts(data)
            total = self.plus(data)
            avg = total / count if count > 0 else 0
            res = f"Processed {count} num values, sum={total}, avg={avg:.1f})"
            return self.format_output(res)
        except Exception as e:
            return f"Error in NumericProcessor: {e}"


class TextProcessor(DataProcessor):
    def counts(self, data: Any) -> int:
        cont: int = 0
        for i in data:
            cont += 1
        return cont

    def validate(self, data: Any) -> bool:
        if data.__class__ != str:
            return False
        return True

    def ft_split(self, data: Any) -> list:
        value: str = ""
        list_str = []
        i = 0
        n = self.counts(data)
        while i < n:
            if ((data[i] >= 'A' and data[i] <= 'Z') or
               (data[i] >= 'a' and data[i] <= 'z')):
                while i < n and ((data[i] >= 'A' and data[i] <= 'Z') or
                                 (data[i] >= 'a' and data[i] <= 'z')):
                    value += data[i]
                    i += 1
                list_str += [value]
                value = ""
            else:
                i += 1
        return list_str

    def process(self, data: str) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Text data verification failed")
            chars = self.counts(data)
            words = self.counts(self.ft_split(data))
            res = f"Processed text: {chars} characters, {words} words"
            return self.format_output(res)
        except Exception as e:
            return f"Error in TextProcessor: {e}"


class LogProcessor(DataProcessor):
    def counts(self, data: Any) -> int:
        cont: int = 0
        for i in data:
            cont += 1
        return cont

    def find_separator(self, data: str) -> Optional[int]:
        i = 0
        while i < self.counts(data):
            if data[i] == ":":
                return i
            i += 1
        return None

    def validate(self, data: Any) -> bool:
        if data.__class__ != str and ":" not in data:
            return False
        return True

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Log entry verification failed")
            sep_idx = self.find_separator(data)
            level = data[:sep_idx]
            message = data[sep_idx + 1:]
            res = f"[{level}] level detected:{message}"
            return self.format_output(res)
        except Exception as e:
            return f"Error in LogProcessor: {e}"

    def format_output(self, result: str) -> str:
        if "ERROR" in result:
            return f"Output: [ALERT] {result}"
        else:
            return f"Output: {result}"


def run_demo():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    np = NumericProcessor()
    print("Initializing Numeric Processor...")
    print("Processing data: [1, 2, 3, 4, 5]")
    print("Validation: Numeric data verified")
    print(np.process([1, 2, 3, 4, 5]))
    print()
    tp = TextProcessor()
    print("Initializing Text Processor...")
    print("Processing data: \"Hello Nexus World\"")
    print("Validation: Text data verified")
    print(tp.process("Hello Nexus World"))
    print()
    lp = LogProcessor()
    print("Initializing Log Processor...")
    print("Processing data: \"ERROR: Connection timeout\"")
    print("Validation: Log entry verified")
    print(lp.process("ERROR: Connection timeout"))
    print()
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    stats_summary: Dict[str, int] = {"processed_items": 0}
    processors: List[DataProcessor] = [NumericProcessor(), TextProcessor(),
                                       LogProcessor()]
    data_items: List[Any] = [[1, 2, 3, 4, 5],
                             "Hello Nexus World", "ERROR:Connection timeout"]
    i = 0
    num_items = 3
    while i < num_items:
        proc = processors[i]
        item = data_items[i]
        result = proc.process(item)
        print(f"Result {i + 1}: {result}")
        stats_summary["processed_items"] += 1
        i += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    run_demo()
