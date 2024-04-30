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

    # Druckt die Überschriften für die Tabelle der ausgeführten Tasks
    print("Task\t Execution Time\t Waiting Time")

    # Initialisiert Variablen für die Gesamtwartezeit, Gesamtumlaufzeit und maximale Burst-Zeit eines Tasks
    total_wait_time = 0
    total_turnaround_time = 0
    max_burst_time = 0

    # Iteriert über die ausgeführten Tasks, um Wartezeit und Umlaufzeit zu berechnen
    for task_name, burst_time in executed_tasks:
        # Addiert die Wartezeit jedes Tasks zur Gesamtwartezeit
        total_wait_time += waiting_time[task_name]
        # Berechnet die Umlaufzeit jedes Tasks und addiert sie zur Gesamtumlaufzeit
        turnaround_time = burst_time + waiting_time[task_name]
        # Aktualisiert die maximale Burst-Zeit, falls die Burst-Zeit des aktuellen Tasks größer ist
        total_turnaround_time += turnaround_time
        max_burst_time = max(max_burst_time, burst_time)
        # Druckt für jeden Task dessen Bezeichner, Ausführungszeit und Wartezeit in der Tabelle
        print(f"{task_name}\t {burst_time}\t\t {waiting_time[task_name]}")

    num_tasks = len(tasks)
    avg_wait_time = total_wait_time / num_tasks
    avg_turnaround_time = total_turnaround_time / num_tasks
    print(f"\nDurchschnittliche Wartezeit: {avg_wait_time}")
    print(f"Durchschnittliche Umlaufzeit: {avg_turnaround_time}")
    print(f"Maximale Laufzeit eines Tasks: {max_burst_time}")

import matplotlib.pyplot as plt

# Beispielaufruf
tasks1 = [("Task1(wenig)", 10), ("Task2(wenig)", 5), ("Task3(wenig)", 8)]
quantum1 = 2
tasks2 = [("Task1(viel)", 1000), ("Task2(viel)", 800), ("Task3(viel)", 1200)]
quantum2 = 100

# Funktion zur Berechnung der Durchschnittswartezeit und durchschnittlichen Umlaufzeit
def calculate_metrics(tasks, quantum):
    total_wait_time = 0
    total_turnaround_time = 0
    for task_name, burst_time in tasks:
        total_wait_time += (burst_time - quantum) * (tasks.index((task_name, burst_time)) + 1)
        total_turnaround_time += burst_time * (tasks.index((task_name, burst_time)) + 1)
    avg_wait_time = total_wait_time / len(tasks)
    avg_turnaround_time = total_turnaround_time / len(tasks)
    return avg_wait_time, avg_turnaround_time

# Berechnung der Metriken für beide Beispielaufrufe
avg_wait_time1, avg_turnaround_time1 = calculate_metrics(tasks1, quantum1)
avg_wait_time2, avg_turnaround_time2 = calculate_metrics(tasks2, quantum2)

# Labels für die x-Achse
labels = ['Durchschnittliche Wartezeit', 'Durchschnittliche Umlaufzeit']

# Werte für den ersten Beispielaufruf
values1 = [avg_wait_time1, avg_turnaround_time1]

# Werte für den zweiten Beispielaufruf
values2 = [avg_wait_time2, avg_turnaround_time2]

# Erstellen des Liniendiagramms
plt.figure(figsize=(10, 6))

# Linie für den ersten Beispielaufruf
plt.plot(labels, values1, marker='o', label='Task1(wenig), Task2(wenig), Task3(wenig)')

# Linie für den zweiten Beispielaufruf
plt.plot(labels, values2, marker='o', label='Task1(viel), Task2(viel), Task3(viel)')

# Beschriftungen und Titel hinzufügen
plt.xlabel('Metrik')
plt.ylabel('Zeiteinheit')
plt.title('Vergleich der Metriken für verschiedene Prozessaufrufe')
plt.legend()

# Anzeigen des Plots
plt.show()

