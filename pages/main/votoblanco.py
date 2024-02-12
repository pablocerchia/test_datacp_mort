import streamlit as st
import streamlit.components.v1 as components
import streamlit_antd_components as sac


def votoblanco(**kwargs):
        st.markdown("<h2 style='text-align: center;'>EVOLUCIÓN DEL VOTO EN BLANCO<br></h2>", unsafe_allow_html=True)
        st.markdown(
                    """<h5 style='text-align: center; font-weight: normal;'>
                    A continuación podrás ver cómo evolucionó el voto en blanco desde 1983.  <br></h5>
                    """,unsafe_allow_html=True,
                )
        #st.write("El descontento del pueblo con la situación económica y social actual parece haber sido canalizado principalmente mediante la victoria de Javier Milei en las PASO 2023. Sin embargo, otras vías de canalización institucionalizada del descontento también puede manifestarse a través del voto en blanco o mediante el ausentismo (el cuál llegó a un 30,38%, convirtiéndose así la elección en una batalla de cuatro cuartos y no tres tercios como planteó hace unos meses la vicepresidenta Cristina Kirchner, si se sigue el marco teórico planteado por la nota de arriba).")
        components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/14843088"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
    #