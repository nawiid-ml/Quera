from rest_framework.serializers import ModelSerializer
from .models import AskTheTeacher , AskTheGBT

class AskTheTeacherSerializers(ModelSerializer):
    class Meta :
        model = AskTheTeacher
        fields = '__all__'  #  This will include all fields of the AskTheTeacher model.

class AskTheGBTSerializers(ModelSerializer):
    """
    """
    class Meta :
        model = AskTheGBT    #  The model that the serializer is for, in this case AskTheGBT.
        fields = ('id', 'question', 'answer')    #  The fields that the serializer should include, in this case id, question, and answer.