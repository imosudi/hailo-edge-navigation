const ws = new WebSocket(`ws://${location.host}/ws`);

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);

    document.getElementById("metrics").innerHTML = `
        FPS: ${data.fps}<br>
        CPU: ${data.cpu}%<br>
        RAM: ${data.memory}%<br>
        TEMP: ${data.temp}°C
    `;
};