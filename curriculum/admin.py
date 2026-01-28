from django.contrib import admin
from .models import (
    ConfiguracionPagina, DatosPersonales, ExperienciaLaboral, 
    EstudioRealizado, ProductoAcademico, CategoriaTag, 
    CursoCapacitacion, Reconocimiento, VentaGarage
)

class BaseAdmin(admin.ModelAdmin):
    """
    Clase base para centralizar la inyección de estilos CSS y configuraciones comunes.
    """
    class Media:
        css = {
            'all': ('curriculum/admin_custom.css',)
        }

@admin.register(CategoriaTag)
class CategoriaTagAdmin(BaseAdmin):
    search_fields = ('nombre',)

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(BaseAdmin):
    list_display = ('nombres', 'apellidos', 'mostrar_seccion')
    list_editable = ('mostrar_seccion',)

@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(BaseAdmin):
    list_display = ('cargo', 'empresa', 'fecha_inicio', 'activo')
    list_editable = ('activo',)
    list_filter = ('activo', 'empresa')

@admin.register(EstudioRealizado)
class EstudioRealizadoAdmin(BaseAdmin):
    list_display = ('titulo', 'institucion', 'fecha_fin', 'activo')
    list_editable = ('activo',)
    list_filter = ('activo',)

@admin.register(ProductoAcademico)
class ProductoAcademicoAdmin(BaseAdmin):
    list_display = ('nombre', 'fecha_publicacion', 'get_tags', 'activo')
    list_filter = ('categorias', 'activo')
    filter_horizontal = ('categorias',)
    list_editable = ('activo',)
    search_fields = ('nombre', 'descripcion')

    def get_tags(self, obj):
        return ", ".join([t.nombre for t in obj.categorias.all()])
    get_tags.short_description = 'Etiquetas'

@admin.register(CursoCapacitacion)
class CursoCapacitacionAdmin(BaseAdmin):
    list_display = ('nombre_curso', 'fecha_realizacion', 'activo')
    list_editable = ('activo',)

@admin.register(Reconocimiento)
class ReconocimientoAdmin(BaseAdmin):
    list_display = ('nombre', 'fecha_obtencion', 'activo')
    list_editable = ('activo',)

@admin.register(VentaGarage)
class VentaGarageAdmin(BaseAdmin):
    list_display = ('nombre_producto', 'precio', 'estado', 'activo')
    list_filter = ('estado', 'activo')
    list_editable = ('activo',)
    search_fields = ('nombre_producto',)

@admin.register(ConfiguracionPagina)
class ConfiguracionPaginaAdmin(BaseAdmin):
    list_display = ('__str__', 'mostrar_perfil', 'mostrar_experiencia', 'mostrar_contacto')
    
    def has_add_permission(self, request):
        # Evita crear más de una configuración global
        return not ConfiguracionPagina.objects.exists()