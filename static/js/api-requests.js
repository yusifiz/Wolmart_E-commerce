let subscribeForm = document.getElementById("subscribe-section");

console.log('form ==>>',subscribeForm)

subscribeForm.addEventListener('submit', function(e){
    e.preventDefault();
    console.log('Email', subscribeForm.email.value)
    let formData = {email: subscribeForm.email.value, };

const url = "subscribe/"
let response = fetch(url,{
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify(formData),
});

response.then((response) =>{
    console.log('json >> ', response.json())
    return response.json()
})
}) 