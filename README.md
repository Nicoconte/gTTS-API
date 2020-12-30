# gTTS-API 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**gTTS-API (Google Text To Speech) es un porteo de la libreria de Python provista por google. Crea un archivo mp3 y gestionalo como quieras, ya sea bajandolo o reproduciendolo en el momento.**

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Uso: 

```javascript

const ejemplo = () => {
    let body = {
      "text" : "Hola, mundo",
      "language" : "es",
      "should_be_slow" : false
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
            link.href = window.URL.createObjectURL(res);
            
            let audio = new Audio(link.href);
            audio.play();
        }
    })
}
```
