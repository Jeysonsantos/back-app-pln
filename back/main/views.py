
from .resumir import resumir,stopwords
from .models import Texto
from rest_framework import viewsets
from .serializers import TextoSerializer
from rest_framework.response import Response


class TextoViewSet(viewsets.ModelViewSet):
    queryset = Texto.objects.all()
    serializer_class = TextoSerializer

    def create(self, request):
        request.data['resumo'] = resumir(request.data['link'],stopwords)
        serializer= TextoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
