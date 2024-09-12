# Fnction based views with models

### List View

```python
# views.py
from django.shortcuts import render
from .models import YourModel

def model_list(request):
    objects = YourModel.objects.all()
    return render(request, 'yourapp/model_list.html', {'objects': objects})
```

```html
<!-- model_list.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>Model List</h1>
  <ul>
    {% for object in objects %}
      <li><a href="{% url 'model_detail' object.id %}">{{ object.name }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
```

### Detail View

```python
# views.py
from django.shortcuts import get_object_or_404, render
from .models import YourModel

def model_detail(request, pk):
    object = get_object_or_404(YourModel, pk=pk)
    return render(request, 'yourapp/model_detail.html', {'object': object})
```

```html
<!-- model_detail.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>{{ object.name }}</h1>
  <p>{{ object.description }}</p>
  <a href="{% url 'model_update' object.id %}">Edit</a>
  <a href="{% url 'model_delete' object.id %}">Delete</a>
{% endblock %}
```

### Create View

```python
# views.py
from django.shortcuts import render, redirect
from .forms import YourModelForm

def model_create(request):
    if request.method == 'POST':
        form = YourModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model_list')
    else:
        form = YourModelForm()
    return render(request, 'yourapp/model_form.html', {'form': form})
```

```html
<!-- model_form.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>Create Model</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
  </form>
{% endblock %}
```

### Update View

```python
# views.py
from django.shortcuts import get_object_or_404, render, redirect
from .forms import YourModelForm
from .models import YourModel

def model_update(request, pk):
    object = get_object_or_404(YourModel, pk=pk)
    if request.method == 'POST':
        form = YourModelForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('model_detail', pk=object.pk)
    else:
        form = YourModelForm(instance=object)
    return render(request, 'yourapp/model_form.html', {'form': form})
```

### Delete View

```python
# views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import YourModel

def model_delete(request, pk):
    object = get_object_or_404(YourModel, pk=pk)
    if request.method == 'POST':
        object.delete()
        messages.success(request, 'The object was deleted successfully.')
        return redirect('model_list')
    return render(request, 'yourapp/model_confirm_delete.html', {'object': object})
```

```html
<!-- model_confirm_delete.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>Confirm Delete</h1>
  <p>Are you sure you want to delete "{{ object.name }}"?</p>
  <form method="post">
    {% csrf_token %}
    <button type="submit">Confirm</button>
    <a href="{% url 'model_detail' object.id %}">Cancel</a>
  </form>
{% endblock %}
```

### URLs Configuration

Make sure to map these views in your `urls.py`:

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_list, name='model_list'),
    path('<int:pk>/', views.model_detail, name='model_detail'),
    path('create/', views.model_create, name='model_create'),
    path('<int:pk>/update/', views.model_update, name='model_update'),
    path('<int:pk>/delete/', views.model_delete, name='model_delete'),
]
```

These examples provide a basic setup for function-based views handling common operations. Adjust the models, forms, and templates according to your specific requirements.
