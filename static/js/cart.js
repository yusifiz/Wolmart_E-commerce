let updateBtns = document.getElementsByClassName('update-cart')

for(let i = 0; i < updateBtns.length; i++ ){
    updateBtns[i].addEventListener('click', function(){
        let productID = this.dataset.product
        let action = this.dataset.action
        console.log('productID:', productID, 'action:', action) 

        console.log('USER', user)

        if (user === 'AnonymousUser'){
            console.log('Not logged in')

        }else{
            updateUserOrder(productID, action)
        }
    })
}

function updateUserOrder(productID, action){
    console.log('User logged in, sending data...')

    var url = 'update_item/'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body: JSON.stringify({'productID': productID, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}