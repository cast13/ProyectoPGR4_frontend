import streamlit as st
import requests

def mostrar_productos():
    st.title("Listado de Productos")

    # Obtener la información de los productos desde el endpoint
    response = requests.get("http://127.0.0.1:8000/productos/")
    
    # Verifica si la respuesta fue exitosa
    if response.status_code == 200:
        productos = response.json()

        # Mostrar la información de los productos
        if productos:
            for producto in productos:
                st.subheader(f"ID: {producto['id']}")
                st.write(f"Nombre: {producto['nombre']}")
                st.write(f"Precio: ${producto['precio']}")
                st.write(f"Cantidad: {producto['cantidad']}")
                st.write("---")
        else:
            st.write("No se encontraron productos.")
    else:
        st.write("Error al obtener los productos.") 