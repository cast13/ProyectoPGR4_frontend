import streamlit as st
import requests
import uuid  # Para generar IDs únicos

# Initialize the simulated database in session state
if 'productos_db' not in st.session_state:
    st.session_state.productos_db = {}

def mostrar_productos():
    st.title("Listado de Productos")
    response = requests.get("http://127.0.0.1:8000/productos/")
    
    if response.status_code == 200:
        productos = response.json()
        st.session_state.productos_db = {producto['id']: producto for producto in productos}

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

def crear_producto():
    st.title("Crear Producto")
    nombre = st.text_input("Nombre del Producto")
    precio = st.number_input("Precio del Producto", min_value=0.0)
    cantidad = st.number_input("Cantidad del Producto", min_value=0)

    if st.button("Crear Producto"):
        producto = {
            "id": str(uuid.uuid4()),
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        response = requests.post("http://127.0.0.1:8000/productos/", json=producto)
        if response.status_code == 200:
            st.success("Producto creado exitosamente.")
            st.session_state.productos_db[producto['id']] = producto
        else:
            st.error("Error al crear el producto.")

def modificar_producto():
    st.title("Modificar Producto")
    producto_id = st.text_input("ID del Producto a Modificar")

    if producto_id in st.session_state.productos_db:
        producto = st.session_state.productos_db[producto_id]
        nombre = st.text_input("Nombre del Producto", value=producto["nombre"])
        precio = st.number_input("Precio del Producto", value=producto["precio"], min_value=0.0)
        cantidad = st.number_input("Cantidad del Producto", value=producto["cantidad"], min_value=0)

        if st.button("Modificar Producto"):
            producto_actualizado = {
                "id": producto_id,
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            response = requests.put(f"http://127.0.0.1:8000/productos/{producto_id}", json=producto_actualizado)
            if response.status_code == 200:
                st.success("Producto modificado exitosamente.")
                st.session_state.productos_db[producto_id] = producto_actualizado
            else:
                st.error("Error al modificar el producto.")
    else:
        st.error("Producto no encontrado.")

def eliminar_producto():
    st.title("Eliminar Producto")
    producto_id = st.text_input("ID del Producto a Borrar")
    
    if st.button("Eliminar Producto"):
        response = requests.delete(f"http://127.0.0.1:8000/productos/{producto_id}")
        if response.status_code == 200:
            st.success("Producto eliminado exitosamente.")
            if producto_id in st.session_state.productos_db:
                del st.session_state.productos_db[producto_id]
        else:
            st.error("Error al eliminar el producto.")

def obtener_producto():
    st.title("Obtener Producto")
    producto_id = st.text_input("ID del Producto a Ver")

    if producto_id in st.session_state.productos_db:
        producto = st.session_state.productos_db[producto_id]
        st.write(f"ID: {producto['id']}")
        st.write(f"Nombre: {producto['nombre']}")
        st.write(f"Precio: ${producto['precio']}")
        st.write(f"Cantidad: {producto['cantidad']}")
    else:
        st.error("Error al obtener el producto.")

# Main function to handle the page
def main():
    st.title("Gestión de Productos")
    opcion = st.selectbox("Selecciona una opción:", 
                          ["Crear Producto", "Modificar Producto", "Borrar Producto", "Obtener Producto", "Mostrar Productos"])

    if opcion == "Crear Producto":
        crear_producto()
    elif opcion == "Modificar Producto":
        modificar_producto()
    elif opcion == "Borrar Producto":
        eliminar_producto()  
    elif opcion == "Obtener Producto":
        obtener_producto()  
    elif opcion == "Mostrar Productos":
        mostrar_productos()  

if __name__ == "__main__":
    main()
