# These library we need for views .
from rest_framework import generics
from .serializer import AskTheTeacherSerializers, AskTheGBTSerializers
from .models import AskTheTeacher, AskTheGBT
from rest_framework import status
import os
from openai import OpenAI
from rest_framework.views import APIView
from rest_framework.response import Response
import json

client = OpenAI(
  api_key=os.environ.get('OPENAI_API_KEY'), 
)#Initialize an OpenAI client with your API key from environment variable.


MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB


class AskTheTeacherCreateView(generics.CreateAPIView):
    queryset = AskTheTeacher.objects.all()
    serializer_class = AskTheTeacherSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check file size before saving
        # maximum file size should be 2 mg
        uploaded_file = request.FILES.get('file')
        if uploaded_file and uploaded_file.size > MAX_FILE_SIZE:
            return Response({'error': 'File size exceeds the limit of 2 MB.'}, status=status.HTTP_400_BAD_REQUEST)

        # Save the object with the serializer
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AskTheGBTCreateView(APIView):
    def post(self, request): # Define the post method for the view.
        question = request.data['question']# Get the question from the request data.

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="gpt-3.5-turbo",
        )   # Send the question to OpenAI API and get the response.

        response_json = json.loads(response.json())   # Parse the JSON response.
        answer = response_json['choices'][0]['message']['content']   # Extract the answer from the response.

        ask_the_ai = AskTheGBT(question=question, answer=answer)   # Create an AskTheGBT instance with the question and answer.
        ask_the_ai.save() # Save the instance to the database.

        #  Return the response with the serialized data.
        return Response(AskTheGBTSerializers(ask_the_ai).data)


