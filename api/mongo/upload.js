async function uploadData(jsonFile) {
    jsonFile = {"data" : jsonFile}
    const data = jsonFile;
    let api = await fetch(`https://us-east-2.aws.data.mongodb-api.com/app/data-iewax/endpoint/Upload`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    })
    let response = await api.json()
    console.log(response);
    return response
}

async function uploadGPTResult(jsonFile){
    jsonFile = {"data" : jsonFile}
    const data = jsonFile;
    let api = await fetch(`https://us-east-2.aws.data.mongodb-api.com/app/data-iewax/endpoint/GPTUpload`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    })
    let response = await api.json()
    console.log(response);
    return response
}

/* uploadGPTResult("THESE aaa DATA"); */