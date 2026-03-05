// Add subtle hover sound or haptic feedback logic here
console.log("German Camp Interaction Engine Loaded...");

// Double-click to copy German words
document.addEventListener('dblclick', function(e) {
    if (e.target.closest('.glass-card')) {
        const text = window.getSelection().toString();
        if (text) {
            navigator.clipboard.writeText(text);
            console.log("Copied to clipboard: " + text);
        }
    }
});
