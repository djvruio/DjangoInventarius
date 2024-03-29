import tablib
from django.db.models import Model
from .models import Equipment
from django.db.models.fields.files import FieldFile
from django.core.exceptions import PermissionDenied
from django.contrib.admin.util import lookup_field
from django.http import HttpResponse
from datetime import datetime, date

def export_as_excel(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta    
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % unicode(opts).replace('.', '_')
    
    try:
        field_names = ['model', 'brand', 'ip_conf', 'mask_conf', 
                'ip_swi', 'mask_swi', 'is_active']
        extras = ['admin_user']
        field_names.extend(extras)
        v_field_names = field_names
    except:
        field_names = [field.name for field in opts.fields]
        v_field_names = [getattr(field, 'verbose_name') or field.name for field in opts.fields]

    v_field_names = map(lambda x: x.encode('utf-8') if x != 'ID' else 'Id', v_field_names)

    ax = []
    headers = v_field_names

    data = []
    data = tablib.Dataset(*data, headers=headers)
    for obj in queryset:
        acc = []
        for field in field_names:
            try:
                uf = getattr(obj, field)()
            except:
                try:
                    uf = getattr(obj, field)
                except:
                    uf = 'error obteniendo el dato'
            if uf is None:
                uf = ''
            elif isinstance(uf, datetime):
                uf = unicode(uf)
                #uf = datetime.datetime.strptime(uf,"%Y-%m-%d")
            elif isinstance(uf, Model):
                uf = unicode(uf)
            elif isinstance(uf, FieldFile):
                uf = uf.url
            acc.append(uf)
        data.append(acc)
    response.write(data.xls)
    return response

export_as_excel.short_description = "Export as Excel"

