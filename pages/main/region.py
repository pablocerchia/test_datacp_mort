import streamlit as st
import streamlit.components.v1 as components
import streamlit_antd_components as sac

def region(**kwargs):

        st.markdown("<h2 style='text-align: center;'>¿CÓMO VOTÓ CADA REGIÓN?<br></h2>", unsafe_allow_html=True)
        

        st.markdown("<h5 style='text-align: center;'>• Consultá los resultados presidenciales entre 2011 y 2023 para cada región: Metropolitana, Pampeana, NOA, NEA, Cuyo, y Patagonia .<br> • Compará cómo le fue a las principales fuerzas en cada elección y consultá los datos de participación, voto en blanco y voto nulo. <br></h5>", unsafe_allow_html=True)

        components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122858" data-height="550px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=600)
        #select_anio = st.columns([0.3,0.4,0.3])
        select_anio22,select_anio1,select_anio2,select_anio3 = st.columns(4)
        
        with select_anio1:
            region = st.selectbox("Seleccionar región:", ['METROPOLITANA', 'PAMPEANA', 'NEA', 'NOA', 'CUYO', 'PATAGONIA'], placeholder="Elegir región")
        
        with select_anio2:
            elecciones = st.selectbox("Seleccionar elección:", ['2011', '2015', '2019', '2023', '2011-2023 (Histórico)'],index=None, placeholder="Elegir año")

################################################# PAMPENAAAAAAAAAAAAAAAAAAAA ############################################

        if region == 'METROPOLITANA' and elecciones == '2023':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122724" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122702" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122619" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119182" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119163" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119142" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            # st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16121660" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115623" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #
        if region == 'METROPOLITANA' and elecciones == '2019':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122750" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122740" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119243" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119213" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16121728" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115614" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'METROPOLITANA' and elecciones == '2015':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122799" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122785" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122763" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119288" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119273" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119259" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            # st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122500" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115534" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'METROPOLITANA' and elecciones == '2011':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122836" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122813" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119310" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119297" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122533" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115521" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'METROPOLITANA' and elecciones == '2011-2023 (Histórico)':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122813" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122785" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122740" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122702" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                                    
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119297" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119273" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119213" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119163" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16122558" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115497" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

    
################################################# PAMPENAAAAAAAAAAAAAAAAAAAA ############################################

        if region == 'PAMPEANA' and elecciones == '2023':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041989" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041960" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041497" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119023" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119002" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118988" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            # st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119329" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16105105" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #
        if region == 'PAMPEANA' and elecciones == '2019':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16042011" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041998" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119051" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119034" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16121555" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16105099" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'PAMPEANA' and elecciones == '2015':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16042214" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16042197" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16042024" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119085" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119075" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119063" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            # st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16121568" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16105093" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'PAMPEANA' and elecciones == '2011':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16042287" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16042236" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119120" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119109" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16121584" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16105089" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'PAMPEANA' and elecciones == '2011-2023 (Histórico)':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16042236" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16042197" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041998" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041960" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                                    
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119109" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119075" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119034" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16119002" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16121623" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16105077" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

############################################################## NEAAAAAAAAAAAAAAAAAAA ############################################

        if region == 'NEA' and elecciones == '2023':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037659" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037643" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037268" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115882" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115859" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115818" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            # st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116143" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104756" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #
        if region == 'NEA' and elecciones == '2019':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037726" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037704" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115938" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115910" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116194" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104748" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'NEA' and elecciones == '2015':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037893" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037868" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037746" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116013" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115989" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115973" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            # st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116228" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104730" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'NEA' and elecciones == '2011':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037958" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037932" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116088" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116066" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116278" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104718" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'NEA' and elecciones == '2011-2023 (Histórico)':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037932" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037868" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037704" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037643" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                                    
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116066" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115989" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115910" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16115818" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116317" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104692" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #
############################################################## NOAAAAAAAAAAAAAAAAAAA ############################################

        if region == 'NOA' and elecciones == '2023':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16036633" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16036594" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15984983" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058407" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058402" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16052325" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            # st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058870" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104523" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #
        if region == 'NOA' and elecciones == '2019':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16036693" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16036670" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058493" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058425" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058982" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104538" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'NOA' and elecciones == '2015':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16036950" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16036905" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16036804" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058734" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058523" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058503" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            # st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16059014" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104546" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'NOA' and elecciones == '2011':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037060" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16036962" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058801" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058767" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16059043" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104557" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'NOA' and elecciones == '2011-2023 (Histórico)':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16036962" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16036905" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16036670" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16036594" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                                    
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058767" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058523" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058425" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16058402" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16059069" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104248" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

############################################################## CUYOOOOOOOOOOOOO ############################################

        if region == 'CUYO' and elecciones == '2023':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15982938" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15982899" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15982647" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116674" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116653" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116628" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            # st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118260" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104899" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #
        if region == 'CUYO' and elecciones == '2019':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15982993" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15982983" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116753" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116722" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118225" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104896" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'CUYO' and elecciones == '2015':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15983103" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15983094" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15983004" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118065" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118043" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116778" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            # st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118187" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104886" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'CUYO' and elecciones == '2011':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15984975" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15984958" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118103" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118091" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118118" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104876" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'CUYO' and elecciones == '2011-2023 (Histórico)':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15984958" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15983094" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15982983" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/15982899" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                                    
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118091" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118043" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116722" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16116653" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118322" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104867" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

                    #

############################################################## CUYOOOOOOOOOOOOO ############################################

        if region == 'PATAGONIA' and elecciones == '2023':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16038285" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16038244" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16037980" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118544" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118503" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118483" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            # st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118712" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104957" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #
        if region == 'PATAGONIA' and elecciones == '2019':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041359" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041331" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118599" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118568" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118850" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104947" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'PATAGONIA' and elecciones == '2015':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041413" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041391" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041372" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118644" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118629" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118615" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            # st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118868" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104942" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'PATAGONIA' and elecciones == '2011':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041480" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041421" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118680" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118665" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)


            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='64822')
            #st.markdown("<h2 style='text-align: center;'>PERFORMANCE DE LOS PRINCIPALES PARTIDOS<br></h2>", unsafe_allow_html=True)

            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118888" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='67332')
                
            components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16104934" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

                    #

        if region == 'PATAGONIA' and elecciones == '2011-2023 (Histórico)':
                
            region1, region2 = st.columns([0.6,0.4])

            with region1:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041421" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041391" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16041331" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16038244" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                                    
            with region2:
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118665" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118629" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118568" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
                components.html("""<div class="flourish-embed flourish-table" data-src="visualisation/16118503" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)

