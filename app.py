import streamlit as st
from pages.clientes import mostrar_clientes  # Importa la función para clientes
from pages.productos import mostrar_productos  # Importa la función para productos

# Cambiar el fondo de la página usando CSS
st.markdown(
    """
    <style>
    .reportview-container {
        background: url('https://image.freepik.com/vector-gratis/fondo-de-tienda-en-linea_1302-806.jpg');  /* Cambia la URL por la de tu imagen de fondo */
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Gestión de Tienda Virtual")

# Menú de navegación
st.sidebar.title("Navegación")
opcion = st.sidebar.selectbox("Selecciona una opción:", ["Inicio", "Gestionar Clientes", "Gestionar Productos", "Gestionar Pedidos"])

if opcion == "Inicio":
    st.markdown("""
    ## Bienvenido a la Tienda Virtual
    En nuestra tienda virtual, puedes gestionar clientes, productos y pedidos de manera eficiente y sencilla. 
    Utiliza el menú de navegación para acceder a las diferentes secciones de la aplicación.
    """)
    
    # Agregar imágenes interactivas
    if st.button("Ver Clientes"):
        mostrar_clientes()  # Llama a la función para mostrar clientes
    st.image("https://www.sistemaimpulsa.com/blog/wp-content/uploads/2019/03/servicio-clientes-2.jpg", caption="Clientes", use_container_width=True)  # Cambia la URL por la de tu imagen
    if st.button("Ver Productos"):
        mostrar_productos()  # Llama a la función para mostrar productos
    st.image("https://pinguinodigital.com/wp-content/uploads/2020/07/marca-de-un-producto-en-marketing-1.jpg", caption="Productos", use_container_width=True)  # Cambia la URL por la de tu imagen

elif opcion == "Gestionar Clientes":
    mostrar_clientes()  # Llama a la función para mostrar clientes
elif opcion == "Gestionar Productos":
    mostrar_productos()  # Llama a la función para mostrar productos
elif opcion == "Gestionar Pedidos":
    st.write("Aquí puedes gestionar los pedidos.")
    # Aquí puedes agregar más funcionalidades para gestionar pedidos
