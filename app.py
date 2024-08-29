import streamlit as st
from textblob import TextBlob
from googletrans import Translator

translator = Translator()
st.title('Uso de textblob')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
               st.subheader("Polaridad y Subjetividad")
               ("""
                Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
                Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
                
               Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.

                 """
               ) 


with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:

        initialText = TextBlob(text1)

        

        translation = translator.translate(initialText, src="es", dest="en")

        blobText = TextBlob(translation.text)

        st.write("El texto original es :", text1)
        st.write("El texto de la traducción es: ", translation.text)
        st.write('Polarity: ', round(blobText.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blobText.sentiment.subjectivity,2))
        x=round(blobText.sentiment.polarity,2)
        if x >= 0.3:
            st.write( 'Es un sentimiento Positivo 😊')
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTJ2eWRoajJ1dXU0NGUzaGk4NHE5enB3bjFwa3YweWFudGw2bGh1eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/TdfyKrN7HGTIY/giphy.gif")
        elif x <= -0.3:
            st.write( 'Es un sentimiento Negativo 😔')
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3BpYmV1aWRidHYzcWZoMGJsajhyZ3N5dXFyeGtveHNqeG1saTVxdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/OPU6wzx8JrHna/giphy.gif")
        else:
            st.write( 'Es un sentimiento Neutral 😐')
            st.image("https://media.giphy.com/media/H47VxJRkvQU3a7FOPf/giphy.gif?cid=ecf05e47x51tyhyw5sb3yo2z6wevk7lingayv1j106dh9aw2&ep=v1_gifs_search&rid=giphy.gif")
with st.expander('Corrección en inglés'):
       text2 = st.text_area('Escribe por favor: ',key='4')
       if text2:
          blob2=TextBlob(text2)
          st.write((blob2.correct())) 
