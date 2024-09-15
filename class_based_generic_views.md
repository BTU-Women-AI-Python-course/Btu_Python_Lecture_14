# Class based generic views 

### 1. **List View**

The `ListView` class-based view displays a list of objects.

**Example:**

```python
# views.py
from django.views.generic import ListView
from .models import MyModel

class MyModelListView(ListView):
    model = MyModel
    template_name = 'mymodel_list.html'
    context_object_name = 'objects'
```

**Template:**

```html
<!-- mymodel_list.html -->
{% extends "base.html" %}

{% block content %}
  <h1>MyModel List</h1>
  <ul>
    {% for obj in objects %}
      <li>{{ obj.name }}</li>
    {% endfor %}
  </ul>
{% endblock %}
```

make object name link to object detail
```html
<!-- mymodel_list.html -->
{% extends "base.html" %}

{% block content %}
  <h1>MyModel List</h1>
  <ul>
    {% for obj in objects %}
      <li><a href="{% url 'mymodel_detail' obj.id %}">{{ obj.name }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
```

**URL Configuration:**

```python
# urls.py
from django.urls import path
from .views import MyModelListView

urlpatterns = [
    path('', MyModelListView.as_view(), name='mymodel_list'),
]
```

### 2. **Detail View**

The `DetailView` class-based view displays a detailed view of a single object.

**Example:**

```python
# views.py
from django.views.generic import DetailView
from .models import MyModel

class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'mymodel_detail.html'
    context_object_name = 'object'
```

**Template:**

```html
<!-- mymodel_detail.html -->
{% extends "base.html" %}

{% block content %}
  <h1>{{ object.name }}</h1>
  <p>{{ object.description }}</p>
{% endblock %}
```

**URL Configuration:**

```python
# urls.py
from django.urls import path
from .views import MyModelDetailView

urlpatterns = [
    path('<int:pk>/', MyModelDetailView.as_view(), name='mymodel_detail'),
]
```

### 3. **Create View**

The `CreateView` class-based view displays a form for creating a new object.

**Example:**

```python
# views.py
from django.views.generic.edit import CreateView
from .models import MyModel

class MyModelCreateView(CreateView):
    model = MyModel
    template_name = 'mymodel_form.html'
    fields = ['name', 'description']
```

**Template:**

```html
<!-- mymodel_form.html -->
{% extends "base.html" %}

{% block content %}
  <h1>Create MyModel</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
  </form>
{% endblock %}
```

**URL Configuration:**

```python
# urls.py
from django.urls import path
from .views import MyModelCreateView

urlpatterns = [
    path('create/', MyModelCreateView.as_view(), name='mymodel_create'),
]
```

### 4. **Update View**

The `UpdateView` class-based view displays a form for updating an existing object.

**Example:**

```python
# views.py
from django.views.generic.edit import UpdateView
from .models import MyModel

class MyModelUpdateView(UpdateView):
    model = MyModel
    template_name = 'mymodel_form.html'
    fields = ['name', 'description']
```

**Template:**

```html
<!-- mymodel_form.html -->
{% extends "base.html" %}

{% block content %}
  <h1>Update MyModel</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
  </form>
{% endblock %}
```

**URL Configuration:**

```python
# urls.py
from django.urls import path
from .views import MyModelUpdateView

urlpatterns = [
    path('<int:pk>/update/', MyModelUpdateView.as_view(), name='mymodel_update'),
]
```

### 5. **Delete View**

The `DeleteView` class-based view displays a confirmation page for deleting an object.

**Example:**

```python
# views.py
from django.views.generic.edit import DeleteView
from .models import MyModel

class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'mymodel_confirm_delete.html'
    success_url = '/success-url/'  # Redirect to a success page after deletion
```

**Template:**

```html
<!-- mymodel_confirm_delete.html -->
{% extends "base.html" %}

{% block content %}
  <h1>Confirm Delete</h1>
  <p>Are you sure you want to delete "{{ object.name }}"?</p>
  <form method="post">
    {% csrf_token %}
    <button type="submit">Confirm</button>
  </form>
  <a href="{% url 'mymodel_list' %}">Cancel</a>
{% endblock %}
```

**URL Configuration:**

```python
# urls.py
from django.urls import path
from .views import MyModelDeleteView

urlpatterns = [
    path('<int:pk>/delete/', MyModelDeleteView.as_view(), name='mymodel_delete'),
]
```

### Summary

1. **List View:** Use `ListView` to display a list of objects.
2. **Detail View:** Use `DetailView` to display details of a single object.
3. **Create View:** Use `CreateView` to create a new object.
4. **Update View:** Use `UpdateView` to update an existing object.
5. **Delete View:** Use `DeleteView` to delete an object with confirmation.

Each view typically uses a corresponding template and should be registered in the `urls.py` file.
Make sure to adjust the templates and URLs according to your project’s structure.
