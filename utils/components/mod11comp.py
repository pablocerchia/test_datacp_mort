import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import streamlit_antd_components as sac
from utils.components.html import h2,spacer, title, h4

def resultados_paso11():
        tabs_sac = sac.buttons(['Por provincia','Por sección'], label=None, index=0, format_func=None, align='center', size='default', direction='horizontal',  return_index=False, key=888)

        st.markdown("""<style>.css-zt5igj svg{display:none}</style>""", unsafe_allow_html=True)


        if tabs_sac == 'Por provincia':


                c1, c2, c3 = st.columns([0.1,0.8,0.1])

                with c2:

                        cmap, charts =st.columns([0.60,0.4])
                        
                        with cmap:
                            
                            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/16372191" data-height="700px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=750)
                        with charts:
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16372502" data-height="400px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=430)
                            components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/59V2t/embed.js?v=1" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/59V2t/full.png" alt="" /></noscript></div>""",height=380)  
                        #sac.divider(label='', icon=None, align='center', key='1')
        if tabs_sac == 'Por sección':
                c1, c2, c3 = st.columns([0.1,0.8,0.1])

                with c2:

                        #components.html("""<div class="flourish-embed flourish-cards" data-src="visualisation/14837408"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=500)
                
                        cmap, charts =st.columns([0.60,0.4])
                        #st.write("Si posas el mouse sobre la provincia podrás ver los resultados en ese distrito. Si clickeas sobre la provincia podrás ver los resultados de las PASO 2019.")
                        with cmap:
                            #st.write('Mapa en construcción')
                            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/16372265" data-height="700px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=750)
                            #components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14909169" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
                            #components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14732854" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
                        with charts:
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16372502" data-height="300px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=350)
                            components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/59V2t/embed.js?v=1" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/59V2t/full.png" alt="" /></noscript></div>""",height=400)  
                        #sac.divider(label='', align='center', key='1')

def resultados_generales11():
        tabs_sac = sac.buttons(['Por provincia','Por sección'], label=None, index=0, format_func=None, align='center',  size='default', direction='horizontal',  return_index=False, key=888)

        #tabs2 = st.tabs(tabs_sac)
        st.markdown("""<style>.css-zt5igj svg{display:none}</style>""", unsafe_allow_html=True)


        if tabs_sac == 'Por provincia':


                c1, c2, c3 = st.columns([0.1,0.8,0.1])

                with c2:

                        #components.html("""<div class="flourish-embed flourish-cards" data-src="visualisation/14837408"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=500)
                
                        cmap, charts =st.columns([0.60,0.4])
                        #st.write("Si posas el mouse sobre la provincia podrás ver los resultados en ese distrito. Si clickeas sobre la provincia podrás ver los resultados de las PASO 2019.")
                        with cmap:
                            #components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14909169" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
                            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/16372472" data-height="700px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=750)
                        with charts:
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16387418" data-height="300px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=350)
                            components.html("""<div style="min-height:322px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/sQZ3x/embed.js?v=1" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/sQZ3x/full.png" alt="" /></noscript></div>""",height=400)  
                        sac.divider(label='', icon=None, align='center', key='1')
        if tabs_sac == 'Por sección':
                c1, c2, c3 = st.columns([0.1,0.8,0.1])

                with c2:

                        #components.html("""<div class="flourish-embed flourish-cards" data-src="visualisation/14837408"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=500)
                
                        cmap, charts =st.columns([0.60,0.4])
                        #st.write("Si posas el mouse sobre la provincia podrás ver los resultados en ese distrito. Si clickeas sobre la provincia podrás ver los resultados de las PASO 2019.")
                        with cmap:
                            #st.write('Mapa en construcción')
                            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/16372462" data-height="700px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=750)
                        with charts:
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16387418" data-height="300px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=350)
                            components.html("""<div style="min-height:322px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/PaLm2/embed.js?v=1" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/PaLm2/full.png" alt="" /></noscript></div>""",height=400)  
                        sac.divider(label='', align='center', key='1')
    
    
def comparacion11():



            #sac.divider(label='', icon=None, align='center', key='67532')
            divider_html_paso_generales = """
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
                <span class="divider-text">&nbsp; &nbsp; PASO VS. GENERALES &nbsp; &nbsp; </span>
            </div>
        </div>
    """
            st.markdown(divider_html_paso_generales, unsafe_allow_html=True)

            distritos = {
                        'Argentina (por provincia)':0,'Argentina (por seccion)':25,'Ciudad Autónoma Bs.As.': 1,
                    'Santa Cruz': 20,
                    'San Luis': 19,
                    'San Juan': 18,
                    'Misiones': 14,
                    'La Rioja': 12,
                    'Jujuy': 10,
                    'Formosa': 9,
                    'Buenos Aires': 2,
                    'Corrientes': 5,
                    'Tucumán': 23,
                    'Tierra del Fuego': 24,
                    'Santa Fe': 21,
                    'Salta': 17,
                    'Córdoba': 4,
                    'Catamarca': 3,
                    'Chaco': 6,
                    'Entre Ríos': 8,
                    'Chubut': 7,
                    'La Pampa': 11,
                    'Mendoza': 13,
                    'Río Negro': 16,
                    'Neuquén': 15,
                    'Santiago del Estero': 22}
            distritos = {k: v for k, v in sorted(distritos.items())}
            col11, col12, col13 = st.columns(3)

            with col12:
                

                    distritos_id = st.selectbox("Seleccioná el distrito:", list(distritos.keys()), index=0, placeholder="")
                    #spacer(1)
                    

        # Dictionary mapping each region to its corresponding Flourish visualization URLs
            flourish_urls = {
                'Argentina (por provincia)': ["visualisation/16372191", "visualisation/16372472", "visualisation/zzzzz"],
                'Argentina (por seccion)': ["visualisation/16372265", "visualisation/16372462", "visualisation/zzzzz"],
                'Buenos Aires': ["visualisation/16475932", "visualisation/16489499", "visualisation/16592399"],
                'Ciudad Autónoma Bs.As.': ["visualisation/16476004", "visualisation/16509238", "visualisation/16592565"],
                'Catamarca': ["visualisation/16476026", "visualisation/16509418", "visualisation/16592622"],
                'Chaco': ["visualisation/16476034", "visualisation/16509427", "visualisation/16592630"],
                'Chubut': ["visualisation/16476040", "visualisation/16509447", "visualisation/16592642"],
                'Córdoba': ["visualisation/16476045", "visualisation/16509460", "visualisation/16592648"],
                'Corrientes': ["visualisation/16476062", "visualisation/16509469", "visualisation/16592661"],
                'Entre Ríos': ["visualisation/16476072", "visualisation/16509477", "visualisation/16592681"],
                'Formosa': ["visualisation/16476078", "visualisation/16509486", "visualisation/16592693"],
                'Jujuy': ["visualisation/16489350", "visualisation/16510414", "visualisation/16592710"],
                'La Pampa': ["visualisation/16489354", "visualisation/16510483", "visualisation/16592726"],
                'La Rioja': ["visualisation/16489368", "visualisation/16510495", "visualisation/16592735"],
                'Mendoza': ["visualisation/16489375", "visualisation/16510508", "visualisation/16592748"],
                'Misiones': ["visualisation/16489378", "visualisation/16510516", "visualisation/16592761"],
                'Neuquén': ["visualisation/16489389", "visualisation/16510522", "visualisation/16592779"],
                'Río Negro': ["visualisation/16489395", "visualisation/16510536", "visualisation/16592798"],
                'Salta': ["visualisation/16489402", "visualisation/16510545", "visualisation/16592808"],
                'San Juan': ["visualisation/16489429", "visualisation/16510555", "visualisation/16592844"],
                'San Luis': ["visualisation/16489433", "visualisation/16510570", "visualisation/16592855"],
                'Santa Cruz': ["visualisation/16489443", "visualisation/16510578", "visualisation/16592865"],
                'Santa Fe': ["visualisation/16489455", "visualisation/16510587", "visualisation/16592877"],
                'Santiago del Estero': ["visualisation/16489467", "visualisation/16510596", "visualisation/16592893"],
                'Tierra del Fuego': ["visualisation/16489474", "visualisation/16510603", "visualisation/16592911"],
                'Tucumán': ["visualisation/16489480", "visualisation/16510613", "visualisation/16592927"],
            }
            
            if distritos_id in flourish_urls:
                    c1, c2 = st.columns(2)

                    with c1:
                        components.html(f"""<div class="flourish-embed flourish-map" data-src="{flourish_urls[distritos_id][0]}" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=650)
                    with c2:
                        components.html(f"""<div class="flourish-embed flourish-map" data-src="{flourish_urls[distritos_id][1]}" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=650)

                    components.html(f"""<div class="flourish-embed flourish-map" data-src="{flourish_urls[distritos_id][2]}" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=650)

def datosextra11():

                    sac.divider(label='', icon=None, align='center', key='67332')
                    st.markdown("<h2 style='text-align: center;'>PARTICIPACIÓN ELECTORAL<br></h2>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: center;'>• Conocé el nivel de participación histórica en cada elección de 2011.<br>• Consultá los datos a nivel nacional o por provincia o por cada sección electoral de cada provincia.<br></h5>", unsafe_allow_html=True)
                    tabs_parti = sac.buttons(['Nacional','Por provincia','Por sección'], label=None, index=0, format_func=None, align='center',  size='large', direction='horizontal',  return_index=False)

                    if tabs_parti == 'Nacional':
                        components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16297260" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                    if tabs_parti == 'Por provincia':
                        components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16248233" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                    if tabs_parti == 'Por sección':
                        culopo1, culopo2, culopo3 = st.columns(3)
                        
                        with culopo2:
                            distritos_participacion = st.selectbox("Seleccioná la provincia:", ['Buenos Aires', 'CABA', 'Catamarca', 'Chaco', 'Chubut', 'Córdoba', 'Corrientes', 'Entre Ríos', 
                                                                                            'Formosa', 'Jujuy', 'La Pampa', 'La Rioja', 'Mendoza', 'Misiones', 
                                                                                            'Neuquén', 'Río Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 
                                                                                            'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego', 'Tucumán'], placeholder="")

                        if distritos_participacion == 'Buenos Aires':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16287206" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'CABA':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288182" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Catamarca':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288202" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Chaco':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288205" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Chubut':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288207" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Córdoba':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288212" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Corrientes':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288216" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Entre Ríos':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288221" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Formosa':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288225" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Jujuy':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288230" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'La Pampa':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288235" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'La Rioja':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288236" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Mendoza':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288238" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Misiones':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288241" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Neuquén':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288249" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Río Negro':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288256" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Salta':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288260" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'San Juan':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288263" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'San Luis':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288264" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Santa Cruz':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288266" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Santa Fe':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288271" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Santiago del Estero':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288281" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Tierra del Fuego':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288286" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion == 'Tucumán':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16288288" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                    #sac.divider(label='', icon=None, align='center', key='6283')
                    
                    st.markdown("<h2 style='text-align: center;'>VOTO EN BLANCO<br></h2>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: center;'>• Conocé el nivel de voto en blanco en cada elección de 2011.<br>• Consultá los datos a nivel nacional, por provincia o por cada sección electoral.<br></h5>", unsafe_allow_html=True)
                    tabs_parti2 = sac.buttons(['Nacional','Por provincia','Por sección'], label=None, index=0, format_func=None, align='center', position='top', size='large', direction='horizontal', shape='round', compact=False, return_index=False)

                    if tabs_parti2 == 'Nacional':
                        components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16287133" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                    if tabs_parti2 == 'Por provincia':
                        components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16279785" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                    if tabs_parti2 == 'Por sección':
                        culopo12, culopo22, culopo32 = st.columns(3)
                        
                        with culopo2:
                            distritos_participacion2 = st.selectbox("Seleccioná la provincia:", ['Buenos Aires', 'CABA', 'Catamarca', 'Chaco', 'Chubut', 'Córdoba', 'Corrientes', 'Entre Ríos', 
                                                                                            'Formosa', 'Jujuy', 'La Pampa', 'La Rioja', 'Mendoza', 'Misiones', 
                                                                                            'Neuquén', 'Río Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 
                                                                                            'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego', 'Tucumán'], placeholder="")

                        if distritos_participacion2 == 'Buenos Aires':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286260" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'CABA':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286271" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Catamarca':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286280" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Chaco':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286284" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Chubut':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286292" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Córdoba':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286296" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Corrientes':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286298" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Entre Ríos':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286302" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Formosa':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286332" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Jujuy':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286337" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'La Pampa':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286346" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'La Rioja':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286356" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Mendoza':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286361" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Misiones':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286366" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Neuquén':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286369" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Río Negro':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286376" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Salta':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286380" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'San Juan':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286386" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'San Luis':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286390" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Santa Cruz':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286395" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Santa Fe':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286401" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Santiago del Estero':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286404" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Tierra del Fuego':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286411" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                        if distritos_participacion2 == 'Tucumán':
                            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16286418" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
                    #sac.divider(label='', icon=None, align='center', key='6283')       