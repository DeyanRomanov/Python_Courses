class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


peoples = input()
emails = []

while not peoples == 'Stop':
    senders, receivers, contents = peoples.split()
    email = Email(senders, receivers, contents)
    emails.append(email)
    peoples = input()

sending = input().split(', ')
sending = [int(num) for num in sending]

for num in sending:
    emails[num].send()

for email in emails:
    print(email.get_info())
