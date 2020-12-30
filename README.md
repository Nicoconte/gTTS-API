# gTTS-API 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**gTTS-API (Google Text To Speech) es un porteo de la libreria de Python provista por google. Crea un archivo mp3 y gestionalo como quieras, ya sea bajandolo o reproduciendolo en el momento.**

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#URL: "https://gttsapi.herokuapp.com/gtts/api/text-to-speech/blob/"

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Uso: 

```javascript

const ejemplo = () => {
    let body = {
      "text" : "Hola, mundo", 
      "language" : "es", // Indicamos el idioma en el que va a decirlo. Ojo, No traduce el texto!
      "should_be_slow" : false //Indicamos si el audio se reproduce de forma rapida(false) o lenta(true)
    }

    $.ajax({
        type: "POST",
        dataType: "native",
        crossDomain: true,
        cache: false,
        url: "https://gttsapi.herokuapp.com/gtts/api/text-to-speech/blob/",
        data: JSON.stringify(body),
        xhrFields : {
            responseType : "blob"
        },
        success: (res) => {
            var link = document.createElement("a"); 
            link.href = window.URL.createObjectURL(res); // Creamos un enlace
            
            let audio = new Audio(link.href); // Lo reproducimos en el momento
            audio.play();
        }
    })
}
```
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Cliente de ejemplo: 
**Sitio: https://nicoconte.github.io/gTTS-API-Client-Example/**
**Repo: https://github.com/Nicoconte/gTTS-API-Client-Example**


