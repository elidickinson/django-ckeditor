from django.db import models
from django import forms

from ckeditor.widgets import CKEditorWidget

# borrowed from https://github.com/theatlantic/django-ckeditor/commit/0d6f26b6f79b295df8dca1e662644e17ea3c20b5
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^ckeditor\.fields\.RichTextField", "^ckeditor\.fields\.RichTextFormField"])

class RichTextField(models.TextField):
    def __init__(self, config_name='default', *args, **kwargs):
        self.config_name = config_name
        super(RichTextField, self).__init__(*args, **kwargs)
    
    def formfield(self, **kwargs):
        defaults = {
            'form_class': RichTextFormField,
            'config_name': self.config_name,
        }
        defaults.update(kwargs)
        return super(RichTextField, self).formfield(**defaults)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^ckeditor\.fields\.RichTextField"])
except:
    pass
        
class RichTextFormField(forms.fields.Field):
    def __init__(self, config_name='default', *args, **kwargs):
        kwargs.update({'widget': CKEditorWidget(config_name=config_name)})
        super(RichTextFormField, self).__init__(*args, **kwargs)
