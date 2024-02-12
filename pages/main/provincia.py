import streamlit as st
import streamlit.components.v1 as components
import streamlit_antd_components as sac

def provincia(**kwargs):
        st.markdown("<h2 style='text-align: center;'>¿CÓMO VOTÓ MI PROVINCIA?<br></h2>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>También podés filtrar para ver cómo le fue a Unión por la Patria y Juntos por el Cambio en tu provincia en las últimas cuatro elecciones presidenciales.<br></h5>", unsafe_allow_html=True)

        cum,cum1, cum2,cum3 = st.columns(4)

        with cum1:
            mi_provincia = st.selectbox("Seleccioná provincia:", ['BUENOS AIRES', 'CABA', 'CATAMARCA','CHACO','CHUBUT','CORDOBA','CORRIENTES','ENTRE RIOS','FORMOSA','JUJUY','LA PAMPA','LA RIOJA', 'MENDOZA','MISIONES','NEUQUEN','RIO NEGRO','SALTA','SAN JUAN', 'SAN LUIS','SANTA CRUZ', 'SANTA FE', 'SANTIAGO DEL ESTERO', 'TIERRA DEL FUEGO', 'TUCUMAN'],index=None, placeholder="")
        
        with cum2:
            mi_alianza = st.selectbox("Seleccioná alianza (opcional):", ['FPV', 'JUNTOS POR EL CAMBIO'],index=None, placeholder="Opcional")

            #mis_resultados = st.button("Graficá los resultados", use_container_width=True, key='23')

        #if mis_resultados:

        if mi_provincia == 'CATAMARCA' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578303" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15580365" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584409" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15495566" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673398" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673581" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673749" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674503" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'CATAMARCA' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675450" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675452" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675451" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675454" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'CATAMARCA' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675537" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675541" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675539" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
#############################################################################################
        if mi_provincia == 'CHACO' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578336" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15580376" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584414" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15495595" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673422" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673595" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673760" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674512" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'CHACO' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675658" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675660" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675659" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675661" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'CHACO' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675720" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675722" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675721" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################

        if mi_provincia == 'CHUBUT' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578354" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15580386" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584423" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15495649" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673428" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673611" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673763" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674514" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'CHUBUT' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675843" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675845" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675844" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675847" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'CHUBUT' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675877" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675881" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15675880" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################

        if mi_provincia == 'CORDOBA' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397568" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396189" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395891" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15495661" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673248" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673619" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673775" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674518" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'CORDOBA' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397610" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395957" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396222" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15691092" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'CORDOBA' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396200" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397738" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15691103" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


########################################################################

        if mi_provincia == 'CORRIENTES' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578423" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15581103" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584435" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15495695" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673445" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673618" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673771" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674526" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'CORRIENTES' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682538" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682540" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682539" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682543" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'CORRIENTES' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682605" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682609" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682608" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################


        if mi_provincia == 'ENTRE RIOS' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578448" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15581115" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584445" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15495738" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673452" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673623" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673777" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674530" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'ENTRE RIOS' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682762" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682769" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682764" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682765" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'ENTRE RIOS' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682816" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682818" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15682817" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################


        if mi_provincia == 'FORMOSA' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578468" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15581130" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584449" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15495761" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673476" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673626" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673781" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674535" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'FORMOSA' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15683487" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15683489" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15683488" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15683491" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'FORMOSA' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15683581" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15683586" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15683583" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################



        if mi_provincia == 'JUJUY' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578569" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15581141" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584457" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15495800" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673482" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673631" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673785" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674543" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'JUJUY' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15684893" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15684895" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15684894" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15684896" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'JUJUY' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15684984" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15684986" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15684985" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################


        if mi_provincia == 'LA PAMPA' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578702" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15581158" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584462" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15495852" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673485" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673636" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674358" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674549" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'LA PAMPA' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15685056" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15685060" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15685058" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15685063" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'LA PAMPA' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15685147" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15685149" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15685148" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################


        if mi_provincia == 'LA RIOJA' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578713" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15581169" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584468" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15496293" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673489" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673641" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674362" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674552" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'LA RIOJA' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686719" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686721" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686720" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686722" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'LA RIOJA' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686778" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686782" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686779" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################


        if mi_provincia == 'MISIONES' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578754" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15581196" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584489" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15496335" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673493" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673669" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674371" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674559" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'MISIONES' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686855" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686858" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686856" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686860" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'MISIONES' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686914" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686916" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15686915" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################


        if mi_provincia == 'NEUQUEN' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578764" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15582804" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584503" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15496359" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673497" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673677" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674373" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674561" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'NEUQUEN' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689247" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689253" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689250" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689257" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'NEUQUEN' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689297" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689299" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689298" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################


        if mi_provincia == 'RIO NEGRO' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578783" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15582810" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584514" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15496404" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673502" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673683" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674375" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674566" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'RIO NEGRO' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689787" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689789" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689788" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689790" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'RIO NEGRO' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689826" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689828" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689827" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################



        if mi_provincia == 'SALTA' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578810" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15582821" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584518" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15496427" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673517" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673691" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674378" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674569" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'SALTA' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689881" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689884" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689883" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689885" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'SALTA' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689939" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689941" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15689940" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################



        if mi_provincia == 'SAN JUAN' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578865" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15582835" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584530" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15496439" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673523" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673706" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674379" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674574" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'SAN JUAN' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690123" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690125" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690124" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690126" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'SAN JUAN' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690357" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690360" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690358" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################



        if mi_provincia == 'SAN LUIS' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578881" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15582839" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584534" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15496457" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673529" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673712" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674386" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674577" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'SAN LUIS' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690420" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690422" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690421" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690423" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'SAN LUIS' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690587" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690590" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690588" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################



        if mi_provincia == 'SANTA CRUZ' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578915" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15582851" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584544" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15496473" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673537" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673715" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674396" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674580" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'SANTA CRUZ' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690618" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690621" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690620" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690622" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'SANTA CRUZ' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690638" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690641" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690639" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################



        if mi_provincia == 'SANTIAGO DEL ESTERO' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578956" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15582881" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584567" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15520095" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673540" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673720" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674470" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674583" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'SANTIAGO DEL ESTERO' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690786" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690788" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690787" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690790" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'SANTIAGO DEL ESTERO' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690808" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690811" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690809" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################


        if mi_provincia == 'TIERRA DEL FUEGO' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15578971" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15582899" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584590" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15520126" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673543" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673723" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674483" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674586" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'TIERRA DEL FUEGO' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690838" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690842" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690840" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690843" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'TIERRA DEL FUEGO' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690867" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690869" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690868" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################


        if mi_provincia == 'TUCUMAN' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15579011" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15582893" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15584579" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15520177" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673549" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9093')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673726" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9094')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674486" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                 sac.divider(label='', icon=None, align='center', key='9095')
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674587" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'TUCUMAN' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690914" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690916" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690915" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690917" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'TUCUMAN' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690985" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690988" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15690987" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

########################################################################
        ############ MENDOZA ################## 
        
        if mi_provincia == 'MENDOZA' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396307" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396017" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395819" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15496316" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673333" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9093')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673663" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9094')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674365" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9095')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674556" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            

        if mi_provincia == 'MENDOZA' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397457" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395875" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396049" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397831" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'MENDOZA' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396033" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397811" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395861" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

        ############ SANTA FE ################## 
        
        if mi_provincia == 'SANTA FE' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397654" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395969" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396245" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15496489" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673354" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9093')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673718" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9094')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674461" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9095')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674581" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            

        if mi_provincia == 'SANTA FE' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397671" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395999" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396274" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397898" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'SANTA FE' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396265" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397869" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395991" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

        ############ BUENOS AIRES ################## 
        
        if mi_provincia == 'BUENOS AIRES' and mi_alianza == None:
            c111, c222 = st.columns([0.5,0.5])

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397497" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)            
                    sac.divider(label='', icon=None, align='center', key='9090')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396060" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9091')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395615" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    sac.divider(label='', icon=None, align='center', key='9092')
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15495488" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

            with c222:
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15618799" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                sac.divider(label='', icon=None, align='center', key='9093')
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15643645" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                sac.divider(label='', icon=None, align='center', key='9094')
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15643759" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                sac.divider(label='', icon=None, align='center', key='9095')
                components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/15643801" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)


        if mi_provincia == 'BUENOS AIRES' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397517" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395696" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396096" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15691126" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'BUENOS AIRES' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396077" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15691134" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395649" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)

        ############ BUENOS AIRES ################## 
        
        if mi_provincia == 'CABA' and mi_alianza == None:
            c111, c222 = st.columns(2)

            #st.write('Aca iria algun line chart o bar chart donde se pueda filtrar por provincia con un dropdown como le fue desde 2011 o 2015, depende la agrupacion')

            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397536" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396135" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395707" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15495535" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673372" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673615" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15673767" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15674516" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            

        if mi_provincia == 'CABA' and mi_alianza == 'FPV':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15397549" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395756" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396181" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15401051" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        if mi_provincia == 'CABA' and mi_alianza == 'JUNTOS POR EL CAMBIO':
            c111, c222 = st.columns(2)
            with c111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15396077" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15400997" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
            with c222:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15395649" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
        sac.divider(label='', icon=None, align='center', key='99021')