# Esqueletos de las clases utilizadas en el modelo UML


class User:

    def __init__(self, id, name, email, role):
        self.id = id
        self.name = name
        self.email = email
        self.role = role

    def __str__(self):
        return f"{self.id} - {self.name} - {self.email} - {self.role}"


class Ticket:

    def __init__(self, id, title, category, priority):
        self.id = id
        self.title = title
        self.category = category
        self.priority = priority
        self.status = "Open"

    def change_status(self, new_status):
        self.status = new_status
        return True


class Comment:

    def __init__(self, id, text, created_at):
        self.id = id
        self.text = text
        self.created_at = created_at

    def __str__(self):
        return f"{self.id} - {self.text}"


class History:

    def __init__(self, id, action, created_at):
        self.id = id
        self.action = action
        self.created_at = created_at

    def __str__(self):
        return f"{self.id} - {self.action}"


class Article:

    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def __str__(self):
        return f"{self.id} - {self.title}"