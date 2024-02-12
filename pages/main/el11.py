import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode, ColumnsAutoSizeMode
import streamlit_antd_components as sac
#from modulo.mesa import mesa
import streamlit_antd_components as sac
from utils.components.html import h2,spacer, title, h4
#from pages.main.mods.mod11 import resultados_generales11,from utils.components.,comparacion11,datosextra11
from utils.components.mod11comp import resultados_paso11,resultados_generales11,datosextra11,comparacion11
def paneo_general(**kwargs):
    divider_html_resultados = """
        <style>
            .divider-container {
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                width: 100%;
                margin: 1rem 0;
            }
            .divider-line {
                height: 2px;
                width: 100%;
                background-color: #31333f; /* Adjust the color to match your design */
                position: absolute;
            }
            .divider-text-container {
                position: relative;
                padding: 0 1rem;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .divider-text {
                background-color: #ffffff; /* Adjust the background to match your app's background */
                color: #31333f; /* Adjust the text color as needed */
                font-size: 35px; /* Adjust the size as needed */
                font-weight: bold;
                z-index: 1;
            }
        </style>
        <div class="divider-container">
            <div class="divider-line"></div>
            <div class="divider-text-container">
                <span class="divider-text">&nbsp; &nbsp;    RESULTADOS  &nbsp; &nbsp; </span>
            </div>
        </div>
    """
    divider_html_candidatos = """
        <style>
            .divider-container {
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                width: 100%;
                margin: 1rem 0;
            }
            .divider-line {
                height: 2px;
                width: 100%;
                background-color: #31333f; /* Adjust the color to match your design */
                position: absolute;
            }
            .divider-text-container {
                position: relative;
                padding: 0 1rem;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .divider-text {
                background-color: #ffffff; /* Adjust the background to match your app's background */
                color: #31333f; /* Adjust the text color as needed */
                font-size: 35px; /* Adjust the size as needed */
                font-weight: bold;
                z-index: 1;
            }
        </style>
        <div class="divider-container">
            <div class="divider-line"></div>
            <div class="divider-text-container">
                <span class="divider-text">&nbsp; &nbsp; CANDIDATOS  &nbsp; &nbsp; </span>
            </div>
        </div>
    """
    divider_html_participacion = """
        <style>
            .divider-container {
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                width: 100%;
                margin: 1rem 0;
            }
            .divider-line {
                height: 2px;
                width: 100%;
                background-color: #31333f; /* Adjust the color to match your design */
                position: absolute;
            }
            .divider-text-container {
                position: relative;
                padding: 0 1rem;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .divider-text {
                background-color: #ffffff; /* Adjust the background to match your app's background */
                color: #31333f; /* Adjust the text color as needed */
                font-size: 35px; /* Adjust the size as needed */
                font-weight: bold;
                z-index: 1;
            }
        </style>
        <div class="divider-container">
            <div class="divider-line"></div>
            <div class="divider-text-container">
                <span class="divider-text">&nbsp; &nbsp; PARTICIPACION &nbsp; &nbsp; </span>
            </div>
        </div>
    """
    st.markdown("""
    <style>
        div.stButton > button:first-child {
            display: block;
            margin: 0 auto;
        }
    </style>
""", unsafe_allow_html=True)
    spacer(2)
    # Render the HTML in the Streamlit app
    col1,colmed, col2 = st.columns([0.45,0.1,0.45])
    #st.markdown("<h2 style='text-align: center;'>Filtrá según el año y la elección<br></h2>", unsafe_allow_html=True)
    
    with col1:
        title(st,1," Resultados generales", 'how_to_vote')
        h4(st,text='Consulte los resultados por provincia y por sección para cualquiera de las elecciones presidenciales entre 2011 y 2023',icon_name='south_america')
        h4(st,text='También puede conocer quiénes fueron los candidatos en cada elección y cuáles fueron sus propuestas!',icon_name='people_alt')
        h4(st,text='Filtre por participación para poder conocer los niveles de participación y voto en blanco.',icon_name='poll')

    with col2:
        spacer(1)
        with st.form(key='elections_form'):
            anio_elecciones = st.selectbox(
                'Selecciona el año de la elección:',
                ('2011', '2015', '2019', '2023')
            )
            tipos = []
            if anio_elecciones == '2011' or anio_elecciones == '2019':
                tipos = ['PASO', 'GENERALES']
            elif anio_elecciones == '2015' or anio_elecciones == '2023':
                tipos = ['PASO', 'GENERALES', 'BALLOTAGE']
            tipo_elecciones = st.selectbox('Selecciona el tipo de elección:',tipos)
            third_options = ['RESULTADOS', 'CANDIDATOS', 'PARTICIPACION']
            selected_subcategory = st.selectbox('Seleccione la categoría', third_options)
            spacer(0.5)
            submit_button = st.form_submit_button(label='Visualiza')

    # When the user hits the submit button, the form data is processed
    if submit_button:
        # Store selections in session state
        st.session_state['anio_elecciones'] = anio_elecciones
        st.session_state['tipo_elecciones'] = tipo_elecciones
        st.session_state['selected_subcategory'] = selected_subcategory

    # Check if selections have been made and stored in session state
    if 'anio_elecciones' in st.session_state and 'tipo_elecciones' in st.session_state and 'selected_subcategory' in st.session_state:
        # Use the stored selections to determine which functions to execute
        if st.session_state['anio_elecciones'] == '2011' and st.session_state['tipo_elecciones'] == 'PASO' and st.session_state['selected_subcategory'] == 'RESULTADOS':
            st.markdown(divider_html_resultados, unsafe_allow_html=True)
            spacer(2)
            resultados_paso11()
            comparacion11()
    #     with st.form(key='elections_form'):
    #     # First selectbox for the year
    #         anio_elecciones = st.selectbox(
    #             'Selecciona el año de la elección:',
    #             ('2011', '2015', '2019', '2023'),
    #             index=3  # default to the last option, adjust the index as needed
    #         )

    #         # Initialize an empty list for the types
    #         tipos = []

    #         # Update the tipos list based on the year selected
    #         if anio_elecciones == '2011' or anio_elecciones == '2019':
    #             tipos = ['PASO', 'GENERALES']
    #         elif anio_elecciones == '2015' or anio_elecciones == '2023':
    #             tipos = ['PASO', 'GENERALES', 'BALLOTAGE']

    #         # Second selectbox for the type, which is dependent on the year selected
    #         tipo_eleccion = st.selectbox(
    #             'Selecciona el tipo de elección:',
    #             tipos
    #         )
    #         third_options = ['RESULTADOS', 'CANDIDATOS', 'PARTICIPACION']
    #         selected_subcategory = st.selectbox('Seleccione la categoría', third_options)
    #         # Submit button for the form
    #         submit_button = st.form_submit_button(label='Visualiza')

    # # When the user hits the submit button, the form data is processed
    # if submit_button:
        
    #     # spacer(1)
    #     # years = ['2011', '2015', '2019', '2023']

    #     # selected_year = st.selectbox('Seleccione el año', years)

    #     # if selected_year in ['2015', '2023']:
    #     #     options = ['PASO', 'GENERALES', 'BALLOTAGE']
    #     # else:
    #     #     options = ['PASO', 'GENERALES']

    #     # selected_category = st.selectbox('Seleccione la elección', options)
    #     # third_options = ['RESULTADOS', 'CANDIDATOS', 'PARTICIPACION']
    #     # selected_subcategory = st.selectbox('Seleccione la categoría', third_options)

    # #spacer(2)

    #     if anio_elecciones == '2011' and tipo_eleccion == 'PASO' and selected_subcategory == 'RESULTADOS':
    #         st.markdown(divider_html_resultados, unsafe_allow_html=True)
    #         spacer(2)
    #         resultados_paso11()
    #         sac.divider(align='center', size='sm', color='dark',key=901)
    #         comparacion11 ()

    #     if anio_elecciones == '2011' and tipo_eleccion == 'GENERALES' and selected_subcategory == 'RESULTADOS':
    #         st.markdown(divider_html_resultados, unsafe_allow_html=True)
    #         spacer(2)
    #         resultados_generales11()
    #         sac.divider(align='center', size='sm', color='dark',key=2319)
    #         comparacion11()

    #     if anio_elecciones == '2011' and selected_subcategory == 'PARTICIPACION':
    #         st.markdown(divider_html_participacion, unsafe_allow_html=True)
    #         spacer(2)
    #         datosextra11()

    # spacer(1)
    # botones_anio_elecciones = sac.buttons([
    #     sac.ButtonsItem(label='2011'),
    #     sac.ButtonsItem(label='2015'),
    #     sac.ButtonsItem(label='2019'),
    #     sac.ButtonsItem(label='2023')
    # ], align='center', size=25, radius='xl')

    # if botones_anio_elecciones == '2011':
    #     botones_tipos =  sac.buttons([
    #     sac.ButtonsItem(label='PASO'),
    #     sac.ButtonsItem(label='GENERALES')
    # ], align='center', size='lg', radius='lg')
    
    # if botones_anio_elecciones == '2015':
    #     botones_tipos =  sac.buttons([
    #     sac.ButtonsItem(label='PASO'),
    #     sac.ButtonsItem(label='GENERALES'),
    #     sac.ButtonsItem(label='BALLOTAGE')
    # ], align='center', size='lg', radius='lg')
        
    # if botones_anio_elecciones == '2019':
    #     botones_tipos =  sac.buttons([
    #     sac.ButtonsItem(label='PASO'),
    #     sac.ButtonsItem(label='GENERALES')
    # ], align='center', size='lg', radius='lg')
        
    # if botones_anio_elecciones == '2023':
    #     botones_tipos =  sac.buttons([
    #     sac.ButtonsItem(label='PASO'),
    #     sac.ButtonsItem(label='GENERALES'),
    #     sac.ButtonsItem(label='BALLOTAGE')
    # ], align='center', size='lg', radius='lg')

    # # spacer(2)
    # st.markdown("""
    #     <style>
    #     :root {
    #         --main-dark: #31333f; /* or any other color value you want */
    #         --text-font-family: 'YourSansSerifFontName', sans-serif;
    #     }
    #     .custom-label {
    #         color: var(--main-dark);
    #         font-family: var(--text-font-family);
    #         font-weight: 100; /* Light font weight */
    #     }
    #     </style>
    # """, unsafe_allow_html=True)

    # # Use the 'custom-label' class for your sac.divider label
    # label_html = '<span class="custom-label" style="font-size: 20px;">Categorias</span>'
    # sac.divider(label=label_html, align='center', size='sm', color='dark')
    # # spacer(2)
    # botones_categorias = sac.buttons([
    #     sac.ButtonsItem(label='RESULTADOS'),
    #     sac.ButtonsItem(label='CANDIDATOS'),
    #     sac.ButtonsItem(label='PARTICIPACION')
    # ], align='center', size='lg', radius='lg')
    # # spacer(2)
    # if botones_anio_elecciones == '2011' and botones_tipos == 'PASO' and botones_categorias == 'RESULTADOS':
    #      resultados_paso11()

    # divi1, divi2, divi3 = st.columns(3)
    # with divi1:
    #     sac.divider(align='center', size='sm', color='dark', key=12)
    # with divi2: 
    #     st.markdown("<h2 style='text-align: center;'>Categorias<br></h2>", unsafe_allow_html=True)
    # with divi3:
    #     sac.divider(align='center', size='sm', color='dark', key=13)
    # st.markdown("""
    # <style>
    # div.stButton {text-align:center}
    # </style>""", unsafe_allow_html=True)
    
    # if 'last_clicked' not in st.session_state:
    #     st.session_state['last_clicked'] = None

    # cont1, cont2, cont3, cont4 = st.columns(3)

    # with cont1:
    #     with st.container(border=True):
    #         st.markdown("<h2 style='text-align: center;'>ELECCIONES 2011<br></h2>", unsafe_allow_html=True)
    #         st.markdown('<p style="text-align: justify;">Conoce los resultados de las elecciones presidenciales.</p>', unsafe_allow_html=True)
    #         if st.button('Conocer resultados'):
    #             st.session_state['last_clicked'] = 'resultados'

    # with cont2:
    #     with st.container(border=True):
    #         st.markdown("<h2 style='text-align: center;'>CANDIDATOS<br></h2>", unsafe_allow_html=True)
    #         st.markdown('<p style="text-align: justify;">Conoce quienes fueron los candidatos principales y cuales fueron sus propuestas.</p>', unsafe_allow_html=True)
    #         if st.button('Conocer candidatos'):
    #             st.session_state['last_clicked'] = 'candidatos'

    # with cont3:
    #     with st.container(border=True):
    #         st.markdown("<h2 style='text-align: center;'>PARTICIPACION<br></h2>", unsafe_allow_html=True)
    #         st.markdown('<p style="text-align: justify;">Conoce los niveles de partipacion, voto en blanco y voto nulo.</p>', unsafe_allow_html=True)
    #         if st.button('Conocer participacion'):
    #             st.session_state['last_clicked'] = 'participacion'

    # # Now display content based on st.session_state['last_clicked']
    # if st.session_state['last_clicked'] == 'resultados':
    #     st.write('Mostrando resultados de las elecciones presidenciales.')

    # elif st.session_state['last_clicked'] == 'candidatos':
    #     st.write('Mostrando candidatos principales y sus propuestas.')

    # elif st.session_state['last_clicked'] == 'participacion':
    #     st.write('Mostrando niveles de participación, voto en blanco y voto nulo.')
    # st.markdown("""
    #     <style>
    #     .card {
    #         border: 1px solid #eee;
    #         border-radius: 10px;
    #         box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.1);
    #         padding: 20px;
    #         margin: 10px;
    #         transition: transform 0.3s ease, box-shadow 0.3s ease;
    #     }
    #     .card:hover {
    #         transform: translateY(-5px);
    #         box-shadow: 5px 5px 25px rgba(0, 0, 0, 0.2);
    #     }
    #     .markdown-button {
    #         background-color: transparent;
    #         border: none;
    #         padding: 0;
    #         margin: 0;
    #         text-align: left;
    #     }
    #     .stButton > button {
    #         width: 100%;
    #         border-radius: 5px;
    #     }
    #     </style>
    # """, unsafe_allow_html=True)

    # # Initialize session state
    # if 'last_clicked' not in st.session_state:
    #     st.session_state['last_clicked'] = None

    # def resultados_button():
    #     st.session_state['last_clicked'] = 'resultados'

    # def candidatos_button():
    #     st.session_state['last_clicked'] = 'candidatos'

    # def participacion_button():
    #     st.session_state['last_clicked'] = 'participacion'

    # # Layout
    # cont1, cont2, cont3 = st.columns(3)

    # with cont1:
    #     with st.container():
    #         st.markdown("<div class='card'>", unsafe_allow_html=True)
    #         # Use a button with markdown-like style
    #         if st.button("RESULTADOS\nConoce los resultados de las elecciones presidenciales.", on_click=resultados_button, key='resultados'):
    #             pass
    #         st.markdown("</div>", unsafe_allow_html=True)

    # with cont2:
    #     with st.container():
    #         st.markdown("<div class='card'>", unsafe_allow_html=True)
    #         if st.button("CANDIDATOS\nConoce quienes fueron los candidatos principales y cuales fueron sus propuestas.", on_click=candidatos_button, key='candidatos'):
    #             pass
    #         st.markdown("</div>", unsafe_allow_html=True)

    # with cont3:
    #     with st.container():
    #         st.markdown("<div class='card'>", unsafe_allow_html=True)
    #         if st.button("PARTICIPACION\nConoce los niveles de partipacion, voto en blanco y voto nulo.", on_click=participacion_button, key='participacion'):
    #             pass
    #         st.markdown("</div>", unsafe_allow_html=True)

    # # Now display content based on st.session_state['last_clicked']
    # if st.session_state['last_clicked'] == 'resultados':
    #     st.write('Mostrando resultados de las elecciones presidenciales.')

    # elif st.session_state['last_clicked'] == 'candidatos':
    #     st.write('Mostrando candidatos principales y sus propuestas.')

    # elif st.session_state['last_clicked'] == 'participacion':
    #     st.write('Mostrando niveles de participación, voto en blanco y voto nulo.')