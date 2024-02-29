from typing import List, Tuple

from openpyxl import Workbook

# changing format of output view:


def save_to_file(tasks: List[Tuple[bool, int, str]], file_name: str) -> None:
    wb = Workbook()
    ws = wb.active

    ws.append(["Completed", "Index", "Title"])

    for task in tasks:
        ws.append(task)

    wb.save(f"C:\\Users\\Olena\\pb_17_task_manager\\tasks\\{file_name}.xlsx")
