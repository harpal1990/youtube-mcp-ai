async function summarize() {

    const url = document.getElementById("videoUrl").value;

    const response = await fetch("/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url })
    });

    const data = await response.json();

    document.getElementById("output").value = data.result;
}


async function getTranscript() {

    const url = document.getElementById("videoUrl").value;

    const response = await fetch("/get_transcript", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url })
    });

    const data = await response.json();

    document.getElementById("output").value = data.result;
}


async function askQuestion() {

    const url = document.getElementById("videoUrl").value;
    const question = document.getElementById("question").value;

    const response = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url,
            question
        })
    });

    const data = await response.json();

    document.getElementById("output").value = data.result;
}