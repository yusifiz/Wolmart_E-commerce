let subscribeForm = document.getElementById("subscribe-section");

console.log('form ==>>',subscribeForm)

subscribeForm.addEventListener('submit', function(e){
    e.preventDefault();
    console.log('Email', subscribeForm.email.value)
    let formData = {email: subscribeForm.email.value, };

const url = "http://127.0.0.1:8000/subscribe/"
let response = fetch(url,{
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify(formData),
});
let responseData = response.json();
console.log('json>>',responseData)
}) 