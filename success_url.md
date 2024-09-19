# Success URL

### 1. Success URL View

```python
# views.py
from django.views.generic import TemplateView

class SuccessView(TemplateView):
    template_name = 'success.html'
```

### 2. Template for the Success View

```html
<!-- templates/success.html -->
{% extends 'base.html' %}

{% block content %}
  <div class="alert alert-success" role="alert">
    MyModel deleted successfully!
  </div>
  <a href="{% url 'mymodel_list' %}">Back to MyModel List</a>
{% endblock %}
```

### 3. URL Configuration

Update your URL configuration to include the success view:

```python
# urls.py
from django.urls import path
from .views import SuccessView

urlpatterns = [
    # ... other URL patterns ...
    path('success-url/', SuccessView.as_view(), name='success')
]
```

Make sure to replace `'mymodel_list'` in the `href` attribute of the `success.html` 
template with the actual name of the URL pattern that lists your `MyModel` objects.
