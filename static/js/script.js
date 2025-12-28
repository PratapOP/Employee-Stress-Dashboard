// -------------------------------
// Main Stress Prediction Handler
// -------------------------------
function predictStress() {
    const data = {
        sleep_hours: Number(document.getElementById("sleep_hours").value),
        work_hours: Number(document.getElementById("work_hours").value),
        screen_time: Number(document.getElementById("screen_time").value),
        physical_activity: Number(document.getElementById("physical_activity").value),
        social_interaction: Number(document.getElementById("social_interaction").value),
        caffeine_intake: Number(document.getElementById("caffeine_intake").value)
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        renderResult(result);
        renderHistoryTable(result.history);
        revealOnScroll();
    })
    .catch(error => {
        console.error("Prediction error:", error);
        alert("Something went wrong. Please try again.");
    });
}

// -------------------------------
// Render Prediction Result
// -------------------------------
function renderResult(result) {
    const resultDiv = document.getElementById("result");

    // Reset classes
    resultDiv.className = "result reveal";

    if (result.stress_level === "Low Stress") {
        resultDiv.classList.add("low");
    } else if (result.stress_level === "Medium Stress") {
        resultDiv.classList.add("medium");
    } else {
        resultDiv.classList.add("high");
    }

    const importanceList = result.feature_importance
        .map(item => `<li>${item.feature}: ${item.importance}%</li>`)
        .join("");

    const recommendationList = result.recommendations
        .map(rec => `<li>${rec}</li>`)
        .join("");

    resultDiv.innerHTML = `
        <h2>Predicted Stress Level</h2>
        <p>
            <strong>${result.stress_level}</strong><br>
            Confidence: <strong>${result.confidence}%</strong>
        </p>

        <h3>Key Stress Contributors</h3>
        <ul>${importanceList}</ul>

        <h3>Personalized Recommendations</h3>
        <ul>${recommendationList}</ul>
    `;

    resultDiv.classList.remove("hidden");
}

// -------------------------------
// Render Stress History Table
// -------------------------------
function renderHistoryTable(history) {
    const tableBody = document.getElementById("history-table-body");

    if (!tableBody || !history || history.length === 0) {
        return;
    }

    tableBody.innerHTML = "";

    // Show latest entry on top
    history.slice().reverse().forEach(item => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${item.timestamp}</td>
            <td>${item.stress_level}</td>
            <td>${item.confidence}%</td>
        `;

        tableBody.appendChild(row);
    });
}

// -------------------------------
// Scroll Reveal Effect
// -------------------------------
function revealOnScroll() {
    const reveals = document.querySelectorAll(".reveal");

    reveals.forEach(element => {
        const windowHeight = window.innerHeight;
        const elementTop = element.getBoundingClientRect().top;
        const revealPoint = 100;

        if (elementTop < windowHeight - revealPoint) {
            element.classList.add("active");
        }
    });
}

// Initial reveal
window.addEventListener("scroll", revealOnScroll);
window.addEventListener("load", revealOnScroll);
