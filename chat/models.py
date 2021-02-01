from django.db import models


class User(models.Model):
    userId = models.CharField(max_length=50)


class Room(models.Model):
    room_name = models.CharField(max_length=100, unique=True)
    user = models.ManyToManyField(User)

class Message(models.Model):
    messageId = models.CharField(max_length=50)
    messageDate = models.DateTimeField()
    messageText = models.TextField()
    user_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    # def __str__(self):
    # return self.messageText

    # create a static method to return all the messages saved for same room

    @staticmethod
    def messages(room_id):
        ur = Room.objects.filter(room_id=room_id)
        mult_messages = Message.objects.filter(user_room=ur)
        data = {}
        data['messages'] = mult_messages
        return mult_messages
