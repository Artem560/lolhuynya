document.getElementById("autoForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    const auto = {
        marke: document.getElementById("marke").value,
        ps: parseInt(document.getElementById("ps").value),
        verbrauch: parseFloat(document.getElementById("verbrauch").value)
    };

    try {
        const response = await fetch("/auto", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(auto)
        });

        const data = await response.json();

        document.getElementById("serverAntwort").textContent = JSON.stringify(data, null, 2);

    } catch (error) {
        document.getElementById("serverAntwort").textContent = "Fehler: " + error;
        console.error("Fehler beim Senden:", error);
    }
});
