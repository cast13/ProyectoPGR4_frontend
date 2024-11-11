import streamlit as st
import requests

def mostrar_clientes():
    st.title("Listado de Clientes")

    # Obtener la información de los clientes desde el endpoint
    response = requests.get("http://127.0.0.1:8000/clientes/")
    
    # Verifica si la respuesta fue exitosa
    if response.status_code == 200:
        clientes = response.json()

        # Mostrar la información de los clientes
        if clientes:
            for cliente in clientes:
                st.subheader(f"ID: {cliente['id']}")
                st.write(f"Nombre: {cliente['nombre']}")
                st.write(f"Correo: {cliente['correo']}")
                st.write(f"Dirección: {cliente['direccion']}")
                st.write(f"Teléfono: {cliente['telefono']}")
                st.write("---")
        else:
            st.write("No se encontraron clientes.")
    else:
        st.write("Error al obtener los clientes.")