from django.shortcuts import render,get_object_or_404
from .models import IjtimoiyNewModels,SiyosiyNewModel
from .serializers import siyo_serializer,ijti_serializer
from rest_framework.views import APIView
from rest_framework.response import Response

class AllContentView(APIView):
    def get(self, request):
        all_data = SiyosiyNewModel.objects.all()
        serializer = siyo_serializer(all_data, many=True)
        return Response(serializer.data)
    
class allContentView(APIView):
    def get(self,request):
        all_data = IjtimoiyNewModels.objects.all()
        serializer = ijti_serializer(all_data, many=True) 
        return Response(serializer.data)
    
class SDetailContentView(APIView):
    def get(self, request, *args, **kwargs):
        content = get_object_or_404(SiyosiyNewModel, id=kwargs['content_id'])
        serialzier = siyo_serializer(content)

        return Response(serialzier.data)
    
class IDetailContentView(APIView):
    def get(self, request, *args, **kwargs):
        content = get_object_or_404(IjtimoiyNewModels, id=kwargs['content_id'])
        serialzier = ijti_serializer(content)

        return Response(serialzier.data)


class SCreateContentView(APIView):
    def post(self, request):
        serializer = siyo_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class ICreateContentView(APIView):
    def post(self, request):
        serializer = ijti_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class SUpdateContentView(APIView):
    def patch(self,request, *args, **kwargs):
        content = get_object_or_404(SiyosiyNewModel, id=kwargs['content_id'])
        serializer = siyo_serializer(SiyosiyNewModel,data= request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class IUpdateContentView(APIView):
    def patch(self,request, *args, **kwargs):
        content = get_object_or_404(IjtimoiyNewModels, id=kwargs['content_id'])
        serializer = ijti_serializer(IjtimoiyNewModels,data= request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class SDeleteContentView(APIView):
    def delete(self,request,*args,**kwargs):
        content = get_object_or_404(SiyosiyNewModel, id=kwargs['content_id'])
        content.delete()
        return Response ({'smg':'delete'})
    
class IDeleteContentView(APIView):
    def delete(self,request,*args,**kwargs):
        content = get_object_or_404(IjtimoiyNewModels, id=kwargs['content_id'])
        content.delete()
        return Response ({'smg':'delete'})