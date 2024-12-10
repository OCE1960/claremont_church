from django.forms.renderers import TemplatesSetting

class CustomFormRenderer(TemplatesSetting):
    form_template_name = 'cms/forms/form_template.html'
    

FORM_RENDERER = "claremont_church.settings.CustomFormRenderer"