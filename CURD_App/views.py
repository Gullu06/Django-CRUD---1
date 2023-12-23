from django.shortcuts import get_object_or_404, redirect, render
from .models import CURD_table
from .form import Userform
# Create your views here.
def read_operation(request):
    data = CURD_table.objects.all()
    return render(request, "CURD_App/read_operation.html", {'data': data})

def read_operation_with_primary_key(request, pk):
    data = get_object_or_404(CURD_table, pk=pk)
    return render(request, 'CURD_App/read_operation_with_primary_key.html', {'data': data})

def create_operation(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('read_operation_with_primary_key', pk=data.pk)
    else:
        form = Userform()
    return render(request, 'CURD_App/user_form.html', {'form': form})

def update_operation(request, pk):
    data = get_object_or_404(CURD_table, pk=pk)
    if request.method == 'POST':
        form = Userform(request.POST, instance=data)
        if form.is_valid():
            data = form.save()
            return redirect('read_operation_with_primary_key', pk=data.pk)
    else:
        form = Userform(instance=data)
    return render(request, 'CURD_App/user_form.html', {'form': form})

def delete_operation(request, pk):
    data = get_object_or_404(CURD_table, pk=pk)
    data.delete()
    return redirect('read_operation')
