# Файл data/todo.txt: каждая строка - одна задача. Написать программу, которая:
# 1) читает todo.txt в список (list)
# 2) спрашивает у пользователя новую задачу (input)
# 3) добавляет задачу в список
# 4) сохраняет обновленный список обратно в todo.txt (режим w)
# 5) выводит на экран сколько задач всего

todos = []

with open("data/todo.txt", "r", encoding="utf-8") as f:
    for line in f:
        todos.append(line.strip())

new_todo = input("Enter a  task: ")

todos.append(new_todo)

with open("data/todo.txt", "w", encoding="utf-8") as f:
    for task in todos:
        f.write(task + "\n")

print("Total of todos:", len(todos))
