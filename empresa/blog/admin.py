from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #Permite ver los campos especiales
    list_display = ('title', 'published', 'author', 'post_categories') #Muestra todo en una lista de 4 columnas
    ordering = ('author',) #Ordena Alfabeticamente por autor
    search_fields = ('title', 'author__username', 'categories__name') #Barra de busqueda, podes buscar por titulo, autor y categorias
    date_hierarchy = 'published' #Calendario de fechas en que se subio el post
    list_filter = ('author__username', 'categories__name') #Filtros por autor y categorias

    #Esta configuracion nos permite mostrar las categorias en el list_display
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")]) 

    #Se configura el nombre, porque está en ingles
    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)