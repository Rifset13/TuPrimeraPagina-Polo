from django.shortcuts import render
from stock.models import Insumo, Productos
from django.template import loader
from django.http import HttpResponse
from stock.forms import InsumoFormulario


# Create your views here.

def crear_insumo(request): 
    
    insumo = Insumo(nombre="Tornillo", descripcion="tipo alen", cantidad_en_stock=567)
    
    insumo.save()
    
    template = loader.get_template("creacion_insumo.html")
    
    doc = template.render({"nombre": insumo.nombre})
    
    return HttpResponse(doc)

def crear_producto(request): 
    
    print("mostrar request.py:")
    print(request.POST)
    
    if request.method == "POST": 
        nuevo_producto = Productos(
            tipo = request.POST["nombre"], 
            descripcion = request.POST["descripcion"], 
            cantidad_en_stock = request.POST["cantidad_en_stock"]
        )
        nuevo_producto.save()
        return render(request, "index.html")
        
    return render(request, 'producto_formulario.html')

def crear_insumo(request): 
    
    if request.method == "POST": 
        nuevo_formulario = InsumoFormulario(request.POST)
        
        if nuevo_formulario.is_valid(): 
            informacion = nuevo_formulario.cleaned_data 
            nuevo_insumo = Insumo(
                nombre=informacion["nombre"], 
                descripcion=informacion["descripcion"], 
                cantidad_en_stock=informacion["cantidad_en_stock"]
            )
            
            nuevo_insumo.save()
            return render(request, 'index.html')
        else: 
            return render(request, 'insumo_formulario.html', {"formulario": nuevo_formulario})
    else:
        nuevo_formulario = InsumoFormulario()
        return render(request, 'insumo_formulario.html', {"formulario": nuevo_formulario})

   