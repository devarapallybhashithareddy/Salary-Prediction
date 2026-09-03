const salaryForm = document.getElementById("salaryForm");
const result = document.getElementById("result");
const predictButton = document.querySelector('button[type="submit"]');

salaryForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const data = {
        work_year: Number(document.getElementById("work_year").value),
        experience_level: document.getElementById("experience_level").value,
        employment_type: document.getElementById("employment_type").value,
        job_title: document.getElementById("job_title").value,
        employee_residence: document
            .getElementById("employee_residence")
            .value
            .toUpperCase(),
        remote_ratio: Number(document.getElementById("remote_ratio").value),
        company_location: document
            .getElementById("company_location")
            .value
            .toUpperCase(),
        company_size: document.getElementById("company_size").value
    };

    try {
        // Show loading state
        predictButton.disabled = true;
        predictButton.innerHTML = "⏳ Predicting...";
        result.innerHTML = "🤖 Our model is analyzing your information...";

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
        );

        if (!response.ok) {
            throw new Error("Prediction failed");
        }

        const prediction = await response.json();

result.innerHTML = `
    💰 Predicted Salary: $${prediction.predicted_salary_usd.toLocaleString("en-US", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    })}
`;

    } catch (error) {
        result.innerHTML = "❌ Error connecting to the server.";
        console.error(error);

    } finally {
        // Restore button
        predictButton.disabled = false;
        predictButton.innerHTML = "Predict Salary";
    }
});