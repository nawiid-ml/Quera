from django.db import models


"""
"""
QUESTION_CHOICES =(
    ("CODE","کد "),
    ("ALGORITHMS","الگوریتم"),
    ("MATH","ریاضی"),
    ("DESIGN","طراحی"),
    ("LEARN","یادگیری یا اموزش"),
    ("OTHER","سایر ")
)


class AskTheTeacher(models.Model):
    """
    This class represents a question and answer from a teacher.
    It is used to ask questions about algorithms, math problems or other issues.
    The user can also provide an example of the problem he/she wants to
    solve in order to get more specific help.
    """
    title_of_the_question = models.CharField(max_length=200,verbose_name='عنوان سوال ')
    question = models.CharField(max_length=200,choices=QUESTION_CHOICES,verbose_name='مسئله')
    file= models.FileField(
        blank=True,
        verbose_name ='ضمیمه',
        help_text= 'ضمیمه پاسخ ارسالی'
    )
    text_question = models.TextField(verbose_name='متن سوال ',
                                     help_text='لطفا مشکلی که باهاش مواجه شدین رو اینجا توضیح بدین.')
    image = models.ImageField(blank=True,verbose_name='انتخاب عکس',
                              help_text=" انتخاب عکس")


class AskTheGBT(models.Model):
    """
    This class represents a question and answer from a (quera gbt).
    """
    question = models.TextField()
    answer = models.TextField()