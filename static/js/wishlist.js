let updatebtns = document.getElementsByClassName('wishlistjs')

for(let i = 0; i < updatebtns.length; i++ ){
    updatebtns[i].addEventListener('click', function(e){
        e.preventDefault; 
        let p = this.dataset.product
        let a = this.dataset.action
        console.log('p:', p, 'a:', a) 

        console.log('USER', user)

        if (user === 'AnonymousUser'){
            console.log('Not logged in')

        }else{
            updateUserWishlist(p, a)
        }
    })
}

function updateUserWishlist(p, a){
    console.log('User logged in, sending data...')

    var url = 'wishlist/'; 
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body: JSON.stringify({'p': p, 'a': a})
    })

    .then((response) =>{
        return response.json()
    })
    .then((datas) =>{
        console.log('datas:', datas)
        location.reload()
    })
}