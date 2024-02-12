import streamlit as st
import streamlit.components.v1 as components
import streamlit_antd_components as sac

def participacion(**kwargs):

        #st.subheader("Pocas personas fueron a votar", anchor=False)
        st.markdown("<h2 style='text-align: center;'>PARTICIPACIÓN HISTÓRICA EN LAS ELECCIONES<br></h2>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>• Conocé la participación histórica en cada elección desde 2011.<br>• Consultá los datos a nivel nacional o por provincia o por cada sección electoral de cada provincia. <br>• Descargá los datos en formato .csv para poder usarlos para investigaciones propias!<br></h5>", unsafe_allow_html=True)
        #tabs = sac.buttons(['Nacional','Por provincia','Por sección'], label=None, index=0, format_func=None, align='center', position='top', size='large', direction='horizontal', shape='round', compact=False, return_index=False)
        tabs = sac.buttons([
        sac.ButtonsItem(label='Nacional'),
        sac.ButtonsItem(label='Por provincia'),
        sac.ButtonsItem(label='Por sección')
            ], align='center', size=25, radius='xl')
        if tabs == 'Nacional':
            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/14842806" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
        if tabs == 'Por provincia':
            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15780584" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
        if tabs == 'Por sección':
            culopo1, culopo2, culopo3 = st.columns(3)
            
            with culopo2:
                distritos_participacion = st.selectbox("Seleccioná la provincia:", ['Buenos Aires', 'CABA', 'Catamarca', 'Chaco', 'Chubut', 'Córdoba', 'Corrientes', 'Entre Ríos', 
                                                                                'Formosa', 'Jujuy', 'La Pampa', 'La Rioja', 'Mendoza', 'Misiones', 
                                                                                'Neuquén', 'Río Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 
                                                                                'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego', 'Tucumán'], placeholder="")

            if distritos_participacion == 'Buenos Aires':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15783323" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'CABA':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15789184" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Catamarca':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15789262" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Chaco':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15789695" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Chubut':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15789763" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Córdoba':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15789818" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Corrientes':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15789864" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Entre Ríos':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15790024" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Formosa':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15790086" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Jujuy':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15790153" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'La Pampa':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15790241" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'La Rioja':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15790321" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Mendoza':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15790540" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Misiones':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15790602" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Neuquén':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15790680" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Río Negro':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15790749" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Salta':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15790864" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'San Juan':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15790934" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'San Luis':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15791101" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Santa Cruz':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15791157" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Santa Fe':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15791201" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Santiago del Estero':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15791271" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Tierra del Fuego':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15791337" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            if distritos_participacion == 'Tucumán':
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15791372" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
        #sac.divider(label='', icon=None, align='center', key='6283')
        particol1, particol2 = st.columns(2)

        with particol1:

            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15788886" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            
        with particol2:

            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15783812" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
        #sac.divider(label='', icon=None, align='center', key='6179')
        st.markdown(f"<h3 style='text-align: center;'>DESCARGÁ LOS DATOS EN FORMATO .CSV<br><br></h3>", unsafe_allow_html=True)
        pp21,col1parti, col2parti, col3parti,pp909 = st.columns(5)

        with col1parti:
            #st.markdown(f"<h3 style='text-align: center;'><br>DESCARGÁ EL .CSV A NIVEL NACIONAL<br></h3>", unsafe_allow_html=True)
            sac.buttons([ sac.ButtonsItem(label='A nivel nacional', icon='download', href='https://drive.google.com/drive/folders/11fGy3la1qhDWYE3hiVeW88jKotd-txCy?usp=sharing')], align='center', shape='round', index=None)
        with col2parti:
            #st.markdown(f"<h3 style='text-align: center;'><br>DESCARGÁ EL .CSV A NIVEL PROVINCIAL<br></h3>", unsafe_allow_html=True)
            sac.buttons([ sac.ButtonsItem(label='A nivel provincial', icon='download', href='https://drive.google.com/drive/folders/1924hCUNVY-4cMZ06TUSqgMY48Gco6IHP?usp=sharing')], align='center', shape='round', index=None)
        with col3parti:
            #st.markdown(f"<h3 style='text-align: center;'><br>DESCARGÁ EL .CSV A NIVEL SECCIÓN<br></h3>", unsafe_allow_html=True)
            sac.buttons([ sac.ButtonsItem(label='A nivel sección', icon='download', href='https://drive.google.com/drive/folders/1ACmLTtpwSoE9i0UfeNK1jlm3_w8Q0dm8?usp=sharing')], align='center', shape='round', index=None)