def round_robin(tasks, quantum):
    """
    Führt eine Round-Robin-Zeitplanung für eine Liste von Tasks aus.

    :param tasks: Liste von Tupeln (task_name, burst_time), wobei task_name ein Bezeichner für den Task und
                  burst_time die Zeit ist, die der Task benötigt, um ausgeführt zu werden.
    :param quantum: Die Zeitscheibe (Quantum), die jedem Task zugewiesen wird.
    """
    total_time = 0  # Gesamtzeit, die zum Ausführen aller Tasks benötigt wird
    remaining_time = {task[0]: task[1] for task in tasks}  # Verbleibende Zeit für jeden Task
    waiting_time = {task[0]: 0 for task in tasks}  # Wartezeit für jeden Task
    executed_tasks = []  # Liste der ausgeführten Tasks

    while any(remaining_time.values()):  # Solange noch nicht alle Tasks ausgeführt wurden
        for task_name, burst_time in tasks:
            if remaining_time[task_name] > 0:  # Prüfen, ob der Task noch nicht fertig ist
                execute_time = min(quantum, remaining_time[task_name])  # Zeit, die der Task in diesem Durchlauf bekommt
                remaining_time[task_name] -= execute_time  # Verbleibende Zeit des Tasks aktualisieren
                total_time += execute_time  # Gesamtzeit aktualisieren
                executed_tasks.append((task_name, execute_time))  # Den Task zur Liste der ausgeführten Tasks hinzufügen

                # Wartezeit für andere Tasks aktualisieren
                for other_task in tasks:
                    if other_task[0] != task_name and remaining_time[other_task[0]] > 0:
                        waiting_time[other_task[0]] += execute_time

    print("Task\t Execution Time\t Waiting Time")
    for task_name, burst_time in executed_tasks:
        print(f"{task_name}\t {burst_time}\t\t {waiting_time[task_name]}")

# Beispielaufruf
tasks = [("Task1", 10), ("Task2", 5), ("Task3", 8)]  # Liste der Tasks mit ihren Burst-Zeiten
quantum = 2  # Die Zeitscheibe (Quantum) für die Round-Robin-Zeitplanung
round_robin(tasks, quantum)  # Aufruf der Funktion round_robin mit den gegebenen Tasks und dem Quantum
