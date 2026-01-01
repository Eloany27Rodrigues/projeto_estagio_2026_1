from django.db import models

# Certifique-se de que o nome da classe é Mensagem
class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.email})"