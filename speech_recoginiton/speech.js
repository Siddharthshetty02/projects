let element = document.getElementById("text")
const recognition = new(window.SpeechRecognition || window.webkitSpeechRecognition)
recognition.lang="en-GB"
recognition.continious=true

document.onclick = recognition.start()
recognition.onresult = (event)=>{
    for (const result of event.result){
        element.innerText = result[0].transcript
    }
}