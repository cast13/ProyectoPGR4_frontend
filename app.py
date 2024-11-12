import streamlit as st
from pages.clientes import mostrar_clientes  # Importa la función para mostrar clientes
from pages.productos import mostrar_productos  # Importa la función para mostrar productos
from pages.pedidos import ver_pedidos  # Importa la función para ver pedidos

# Cambiar el fondo de la página y la fuente usando CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap');

    .reportview-container {
        background: url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDF8fGJhY2tncm91bmR8ZW58MHx8fHwxNjYyMjY0MjY0&ixlib=rb-1.2.1&q=80&w=1080');  /* Nueva imagen de fondo */
        background-size: cover;
        background-position: center;
        font-family: 'Open Sans', sans-serif;  /* Cambia la fuente a Open Sans */
    }

    /* Estilo para la barra de navegación */
    .navbar {
        background-color: rgba(255, 255, 255, 0.8);  /* Fondo blanco con transparencia */
        padding: 10px;
        border-radius: 10px;
    }

    /* Estilo para los títulos */
    h1 {
        font-size: 5em;  /* Tamaño de letra más grande para h1 */
    }

    h2 {
        font-size: 2em;  /* Tamaño de letra más grande para h2 */
    }

    h3 {
        font-size: 1.5em;  /* Tamaño de letra más grande para h3 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Tienda Virtual")

# Menú de navegación
st.sidebar.title("MENU")
opcion = st.sidebar.selectbox("Selecciona una opción:", ["Inicio", "Gestionar Clientes", "Gestionar Productos", "Gestionar Pedidos"])

if opcion == "Inicio":
    st.markdown("""
    ## Bienvenido a la Tienda Virtual
    
    Nuestra tienda virtual está diseñada específicamente para empresas dedicadas a sistemas de drywall, ofreciendo una plataforma eficiente para la gestión de clientes, productos y pedidos. Esta herramienta permite automatizar y centralizar el proceso de ventas, facilitando la experiencia tanto para la empresa como para sus clientes.

    Los clientes pueden navegar y comprar una amplia gama de productos esenciales para la construcción en drywall: placas de yeso, perfiles de acero, herramientas especializadas, accesorios de instalación, entre otros. La plataforma incluye detalles de inventario en tiempo real, opciones de pago seguras y seguimiento de pedidos.

    Además, el sistema ayuda a la empresa a gestionar fácilmente los datos de sus clientes, desde el historial de compras hasta las preferencias de productos, lo que permite ofrecer recomendaciones personalizadas y promociones exclusivas. Con esta herramienta, se busca optimizar el flujo de trabajo en la cadena de suministro y aumentar la satisfacción del cliente a través de un proceso de compra ágil y moderno. 
    
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
    ver_pedidos()  # Llama a la función para ver pedidos
