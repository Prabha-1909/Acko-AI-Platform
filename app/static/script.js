function toggleForm() {


const type =
    document.getElementById(
        "insuranceType"
    ).value;

document.getElementById(
    "bike-form"
).style.display = "none";

document.getElementById(
    "car-form"
).style.display = "none";

document.getElementById(
    "health-form"
).style.display = "none";

if(type === "bike") {

    document.getElementById(
        "bike-form"
    ).style.display = "block";
}

if(type === "car") {

    document.getElementById(
        "car-form"
    ).style.display = "block";
}

if(type === "health") {

    document.getElementById(
        "health-form"
    ).style.display = "block";
}


}

async function sendQuestion() {


console.log("Ask button clicked");

const question =
    document.getElementById(
        "question"
    ).value;

if(question.trim() === "") {

    alert("Enter a question");

    return;
}

try {

    const response =
        await fetch("/ask", {

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                question:question
            })
        });

    const data =
        await response.json();

    const chatBox =
        document.getElementById(
            "chat-box"
        );

    chatBox.innerHTML +=
        "<div class='user-msg'>" +
        question +
        "</div>";

    chatBox.innerHTML +=
    "<div class='bot-msg'>" +
    (data.answer || data.response || data.error || "No response received") +
    "</div>";

    const data =
    await response.json();

    console.log("Ask response:", data);

    document.getElementById(
        "question"
    ).value = "";

    chatBox.scrollTop =
        chatBox.scrollHeight;
}

catch(error){

    console.log(error);

    alert(
        "Ask API Error. Check Flask terminal."
    );
}


}

async function predictBikePremium() {

    const payload = {

        customer_age:
        document.getElementById(
            "bike_customer_age"
        ).value,

        city_risk_score:
        document.getElementById(
            "bike_city_risk_score"
        ).value,

        vehicle_age_years:
        document.getElementById(
            "bike_vehicle_age"
        ).value,

        engine_cc:
        "125",

        idv:
        document.getElementById(
            "bike_idv"
        ).value,

        ncb_percent:
        document.getElementById(
            "bike_ncb"
        ).value,

        claim_history_count:
        document.getElementById(
            "bike_previous_claims"
        ).value,

        num_addons:
        "1"
    };

    try {

        const response =
            await fetch(
                "/predict_bike_premium",
                {
                    method:"POST",

                    headers:{
                        "Content-Type":"application/json"
                    },

                    body:JSON.stringify(payload)
                }
            );

        const data =
            await response.json();

        console.log(
            "Bike premium response:",
            data
        );

        if(!response.ok){

            alert(
                "Server Error. Check Flask terminal."
            );

            return;
        }

        if(data.predicted_premium === undefined){

            alert(
                "Prediction value missing. Check console."
            );

            return;
        }

        document.getElementById(
            "bike-result"
        ).innerHTML =

        "<div class='result-card'>" +

        "<h3>Estimated Premium</h3>" +

        "<h2>₹" +
        Math.round(
            data.predicted_premium
        ) +
        "</h2>" +

        "</div>";
    }

    catch(error){

        console.log(error);

        alert(
            "Bike Premium API Error"
        );
    }
}

async function predictCarPremium() {


const payload = {

    customer_age:
    document.getElementById(
        "car_customer_age"
    ).value,

    city_risk_score:
    document.getElementById(
        "car_city_risk_score"
    ).value,

    vehicle_age_years:
    document.getElementById(
        "car_vehicle_age"
    ).value,

    engine_cc:
    "1200",

    idv:
    document.getElementById(
        "car_idv"
    ).value,

    ncb_percent:
    document.getElementById(
        "car_ncb"
    ).value,

    claim_history_count:
    document.getElementById(
        "car_previous_claims"
    ).value,

    num_addons:
    "1"
};

try {

    const response =
        await fetch(
            "/predict_car_premium",
            {
                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify(payload)
            }
        );

    const data =
        await response.json();

    document.getElementById(
        "car-result"
    ).innerHTML =

    "<div class='result-card'>" +

    "<h3>Estimated Premium</h3>" +

    "<h2>₹" +
    Math.round(
        data.predicted_premium
    ) +
    "</h2>" +

    "</div>";
}

catch(error){

    console.log(error);

    alert(
        "Car Premium API Error"
    );
}


}

async function predictHealthPremium() {


const payload = {
    age: document.getElementById("health_age").value,
    gender: document.getElementById("health_gender").value,
    num_members: document.getElementById("health_members").value,
    city_tier: document.getElementById("health_city_tier").value,
    bmi_category: document.getElementById("health_bmi").value,
    smoke: document.getElementById("health_smoke").value,
    has_pre_existing: document.getElementById("health_pre_existing").value,
    ncb_years: document.getElementById("health_ncb").value,
    sum_insured: document.getElementById("health_sum_insured").value,
    deductible: document.getElementById("health_deductible").value,
    num_addons: document.getElementById("health_addons").value,
    has_maternity: document.getElementById("health_maternity").value,
    has_opd: document.getElementById("health_opd").value,
    policy_tenure: document.getElementById("health_tenure").value
};

try {

    const response =
        await fetch(
            "/predict_health_premium",
            {
                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify(payload)
            }
        );

    const data =
        await response.json();

    document.getElementById(
        "health-result"
    ).innerHTML =

    "<div class='result-card'>" +

    "<h3>Estimated Premium</h3>" +

    "<h2>₹" +
    Math.round(
        data.predicted_premium
    ) +
    "</h2>" +

    "</div>";
}

catch(error){

    console.log(error);

    alert(
        "Health Premium API Error"
    );
}


}

async function submitClaim() {

    const imageFile =
        document.getElementById(
            "damage_image"
        ).files[0];

    if(!imageFile){

        alert(
            "Please upload an image"
        );

        return;
    }

    const formData = new FormData();

    formData.append(
        "vehicle_type",
        document.getElementById(
            "claim_vehicle_type"
        ).value
    );

    formData.append(
        "damage_image",
        imageFile
    );

    formData.append(
        "vehicle_age_years",
        document.getElementById(
            "claim_vehicle_age"
        ).value
    );

    formData.append(
        "idv",
        document.getElementById(
            "claim_idv"
        ).value
    );

    formData.append(
        "city_risk_score",
        document.getElementById(
            "claim_city_risk"
        ).value
    );

    formData.append(
        "previous_claims_count",
        document.getElementById(
            "claim_previous_claims"
        ).value
    );

    formData.append(
        "policy_age_months",
        document.getElementById(
            "claim_policy_age"
        ).value
    );

    formData.append(
        "num_parts_affected",
        document.getElementById(
            "claim_parts"
        ).value
    );

    try {

        const response =
            await fetch(
                "/submit_claim",
                {
                    method: "POST",
                    body: formData
                }
            );

        const data =
            await response.json();

        console.log(
            "Claim response:",
            data
        );

        if(!response.ok){

            alert(
                data.error || "Claim API Server Error"
            );

            return;
        }

        document.getElementById(
            "claim-result"
        ).innerHTML = `

        <div class="result-card">

            <h3>Claim Analysis</h3>

            <p>
            Damage:
            ${data.damage_type}
            </p>

            <p>
            Severity:
            ${data.severity}
            </p>

            <p>
            Claim Amount:
            ₹${Math.round(
                data.predicted_claim_amount
            )}
            </p>

            <p>
            Approval Chance:
            ${data.approval_probability}%
            </p>

        </div>
        `;
    }

    catch(error){

        console.log(error);

        alert(
            "Claim API Error. Check browser console and Flask terminal."
        );
    }

}