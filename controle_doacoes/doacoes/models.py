from django.db import models

class Doador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nome


class Doacao(models.Model):
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE, related_name="doacoes")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Doação de {self.valor} - {self.doador.nome}"
