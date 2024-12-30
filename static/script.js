const micButtons = document.querySelectorAll('.mic-btn');

micButtons.forEach(button => {
    button.addEventListener('click', function() {
        const fieldId = this.getAttribute('data-field'); 
        startVoiceRecognition(fieldId); 
    });
});

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

recognition.continuous = false;
recognition.interimResults = true;
recognition.lang = 'en-US';

function startVoiceRecognition(fieldId) {
    recognition.start();

    recognition.onresult = function(event) {
        let transcript = event.results[0][0].transcript;

        // Handle email field differently to replace 'at' with '@'
        if (fieldId === 'email') {
            transcript = transcript.replace(/\bat\b/g, '@').replace(/\s+/g, '').toLowerCase();
        }

        document.getElementById(fieldId).value = transcript;
    };

    recognition.onerror = function(event) {
        console.log('Error occurred in speech recognition: ' + event.error);
    };
}

recognition.onend = function() {
    console.log('Speech recognition ended');
};
