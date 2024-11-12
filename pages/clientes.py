import streamlit as st
import requests
import uuid

# Initialize the simulated database in session state
if 'clientes_db' not in st.session_state:
    st.session_state.clientes_db = {}

def crear_cliente():
    st.header("Crear Cliente")
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo")
    direccion = st.text_input("Dirección")
    telefono = st.text_input("Teléfono")

    if st.button("Crear Cliente"):
        cliente_id = str(uuid.uuid4())  # Generate a unique ID
        cliente = {
            "id": cliente_id,
            "nombre": nombre,
            "correo": correo,
            "direccion": direccion,
            "telefono": telefono,
            "pedidos": []
        }
        
        # Send a POST request to create the client
        response = requests.post("http://127.0.0.1:8000/clientes/", json=cliente)
        
        if response.status_code == 200:  # Assuming 201 is the success status code for creation
            st.success(f"Cliente creado con ID: {cliente_id}")
        else:
            st.error("Error al crear el cliente.")

def editar_cliente():
    st.header("Editar Cliente")
    cliente_id = st.text_input("ID del Cliente a Editar")

    if cliente_id:
        # Fetch the existing client data
        response = requests.get(f"http://127.0.0.1:8000/clientes/{cliente_id}")
        
        if response.status_code == 200:
            cliente = response.json()
            nombre = st.text_input("Nombre", value=cliente["nombre"])
            correo = st.text_input("Correo", value=cliente["correo"])
            direccion = st.text_input("Dirección", value=cliente["direccion"])
            telefono = st.text_input("Teléfono", value=cliente["telefono"])

            if st.button("Actualizar Cliente"):
                updated_cliente = {
                    "id": cliente_id,
                    "nombre": nombre,
                    "correo": correo,
                    "direccion": direccion,
                    "telefono": telefono,
                    "pedidos": cliente["pedidos"]  # Keep existing pedidos
                }
                
                # Send a PUT request to update the client
                response = requests.put(f"http://127.0.0.1:8000/clientes/{cliente_id}", json=updated_cliente)
                
                if response.status_code == 200:  # Assuming 200 is the success status code for updates
                    st.success(f"Cliente {cliente_id} actualizado.")
                else:
                    st.error("Error al actualizar el cliente.")
        else:
            st.error("Cliente no encontrado.")

def eliminar_cliente():
    st.header("Eliminar Cliente")
    cliente_id = st.text_input("ID del Cliente a Eliminar")

    if st.button("Eliminar Cliente"):
        # Send a DELETE request to remove the client
        response = requests.delete(f"http://127.0.0.1:8000/clientes/{cliente_id}")
        
        if response.status_code == 200:  # Assuming 204 is the success status code for deletion
            st.success(f"Cliente {cliente_id} eliminado.")
        else:
            st.error("Error al eliminar el cliente. Cliente no encontrado o error en el servidor.")

def mostrar_clientes():
    st.header("Lista de Clientes")
    
    # Send a GET request to fetch the list of clients
    response = requests.get("http://127.0.0.1:8000/clientes/")
    
    if response.status_code == 200:
        clientes = response.json()  # Assuming the response is a list of clients
        for cliente in clientes:
            st.json(cliente)  # Display each client in JSON format
    else:
        st.error("Error al obtener la lista de clientes.")

def ver_cliente():
    st.header("Ver Cliente")
    cliente_id = st.text_input("ID del Cliente a Ver")

    if st.button("Ver Cliente"):
        # Send a GET request to fetch the client data
        response = requests.get(f"http://127.0.0.1:8000/clientes/{cliente_id}")
        
        if response.status_code == 200:
            cliente = response.json()
            st.json(cliente)  # Display the client data in JSON format
        else:
            st.error("Cliente no encontrado.")

def ver_cantidad_pedidos():
    st.header("Cantidad de Pedidos del Cliente")
    cliente_id = st.text_input("ID del Cliente")

    if st.button("Ver Cantidad de Pedidos"):
        # Send a GET request to fetch the number of orders for the client
        response = requests.get(f"http://127.0.0.1:8000/clientes/{cliente_id}/cantidad_pedidos")
        
        if response.status_code == 200:
            cantidad_pedidos = response.json()  # Assuming the response is just an integer
            st.write(f"El cliente con ID {cliente_id} ha realizado {cantidad_pedidos} pedidos.")
        else:
            st.error("Error al obtener la cantidad de pedidos. Cliente no encontrado.")

# Main function to handle the page
def main():
    st.title("Gestión de Clientes")
    opcion = st.selectbox("Selecciona una opción:", 
                          ["Crear Cliente", "Editar Cliente", "Eliminar Cliente", "Ver Cliente", "Mostrar Clientes", "Ver Cantidad de Pedidos"])

    if opcion == "Crear Cliente":
        crear_cliente()
    elif opcion == "Editar Cliente":
        editar_cliente()
    elif opcion == "Eliminar Cliente":
        eliminar_cliente()  # Call the function to delete a client
    elif opcion == "Ver Cliente":
        ver_cliente()  # Call the function to view a client
    elif opcion == "Mostrar Clientes":
        mostrar_clientes()  # Call the function to display clients
    elif opcion == "Ver Cantidad de Pedidos":
        ver_cantidad_pedidos()  # Call the function to view the number of orders

if __name__ == "__main__":
    main()

