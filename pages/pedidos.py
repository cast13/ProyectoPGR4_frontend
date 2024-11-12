import streamlit as st
import requests
import uuid  # Para generar IDs únicos

# Initialize the simulated database in session state
if 'pedidos_db' not in st.session_state:
    st.session_state.pedidos_db = {}

def crear_pedido():
    st.title("Crear Pedido")
    
    # Seleccionar cliente
    cliente_id = st.text_input("ID del Cliente")
    
    # Seleccionar productos
    productos = st.text_area("IDs de Productos (separados por comas)").split(',')
    productos = [producto.strip() for producto in productos if producto.strip()]  # Limpiar espacios

    # Calcular total (puedes implementar lógica para obtener precios de productos)
    total = st.number_input("Total del Pedido", min_value=0.0)

    # Estado del pedido
    estado = st.selectbox("Estado del Pedido", ["Pendiente", "En Proceso", "Completado"])

    if st.button("Crear Pedido"):
        pedido = {
            "cliente_id": cliente_id,
            "productos": productos,
            "total": total,
            "estado": estado
        }
        response = requests.post("http://127.0.0.1:8000/pedidos/", json=pedido)
        if response.status_code == 200:  # Suponiendo que 201 es el código de éxito para creación
            st.success("Pedido creado exitosamente.")
            st.session_state.pedidos_db[pedido['cliente_id']] = pedido  # Guardar en la base de datos simulada
        else:
            st.error("Error al crear el pedido.")

def ver_pedidos():
    st.title("Ver Pedidos")
    
    # Obtener la lista de pedidos desde el endpoint
    response = requests.get("http://127.0.0.1:8000/pedidos/")
    
    if response.status_code == 200:
        pedidos = response.json()  # Suponiendo que la respuesta es una lista de pedidos
        if pedidos:
            for pedido in pedidos:
                st.subheader(f"Cliente ID: {pedido.get('cliente_id', 'No disponible')}")
                st.write(f"Productos: {', '.join(pedido.get('productos', []))}")
                
                # Manejo de errores para la clave 'total'
                total = pedido.get('total', 'No disponible')
                st.write(f"Total: ${total}")
                
                st.write(f"Estado: {pedido.get('estado', 'No disponible')}")
                st.write("---")
        else:
            st.write("No se encontraron pedidos.")
    else:
        st.error("Error al obtener la lista de pedidos.")

# Main function to handle the page
def main():
    st.title("Gestión de Pedidos")
    opcion = st.selectbox("Selecciona una opción:", ["Crear Pedido", "Ver Pedidos"])

    if opcion == "Crear Pedido":
        crear_pedido()
    elif opcion == "Ver Pedidos":
        ver_pedidos()

if __name__ == "__main__":
    main()
