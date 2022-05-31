from django.db import models


class Doctor(models.Model):
    """Врачи"""
    name = models.CharField("Имя", max_length=50)
    description = models.TextField("Описание")
    img = models.ImageField(upload_to='doctors/')

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

    def __str__(self):
        return self.name


class Enroll(models.Model):
    WEEK = (
        ("sun", "Понедельник"),
        ("mon", "Вторник"),
        ("tue", "Среда"),
        ("wed", "Четверг"),
        ("thu", "Пятница"),
    )

    name = models.CharField("Имя", max_length=50)
    email = models.EmailField("E-mail")
    weeks = models.CharField("Недели", max_length=50, choices=WEEK, default="sun")
    time = models.TimeField("Время")
    doctors = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Врачи")
    messages = models.TextField("Сообщения")

    class Meta:
        verbose_name = "Запись на прием"
        verbose_name_plural = "Запись на прием"

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField("Имя", max_length=50)
    email = models.EmailField("E-mail")
    telephone = models.CharField("Телефон", max_length=50)
    requirements = models.CharField("Требования", max_length=50)
    messages = models.TextField("Сообщения")

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return self.name


class Subscription(models.Model):
    email = models.EmailField("E-mail")
    date = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        pass
