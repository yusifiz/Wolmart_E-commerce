// let updateBtns = document.getElementsByClassName('update-cart')

// for(let i = 0; i < updateBtns.length; i++ ){
//     updateBtns[i].addEventListener('click', function(e){
//         e.preventDefault;   
//         let productID = this.dataset.product
//         let action = this.dataset.action
//         console.log('productID:', productID, 'action:', action) 

//         console.log('USER', user)

//         if (user === 'AnonymousUser'){
//             console.log('Not logged in')

//         }else{
//             updateUserOrder(productID, action)
//         }
//     })
// }

// function updateUserOrder(productID, action){
//     console.log('User logged in, sending data...')

//     var url = 'update_item/'
//     fetch(url, {
//         method: 'POST',
//         headers:{
//             'Content-Type': 'application/json',
//             'X-CSRFToken' : csrftoken,
//         },
//         body: JSON.stringify({'productID': productID, 'action': action})
//     })

//     .then((response) =>{
//         return response.json()
//     })
//     .then((data) =>{
//         console.log('data:', data)
//         location.reload()
//     })
// }



$(document).ready(function(){
        $(document).on('click',".update-cart",function(){
            var _vm=$(this);
            var _index=_vm.attr('data-product');
            var _qty=$(".product-qty-"+_index).val();
            var _productId=$(".product-id-"+_index).val();
            // var _productImage=$(".product-image-"+_index).val();
            var _productTitle=$(".product-title-"+_index).val();
            // var _productPrice=$(".product-price-"+_index).text();
            // Ajax
            $.ajax({
                url:'update_item/',
                data:{
                    'id':_productId,
                    // 'image':_productImage,
                    'qty':_qty,
                    'title':_productTitle,
                    // 'price':_productPrice
                },
                dataType:'json',
                beforeSend:function(){
                    _vm.attr('disabled',true);
                },
                success:function(res){
                    $(".cart-list").text(res.totalitems);
                    _vm.attr('disabled',false);
                }
            });
            // End
        });
        e.preventDefault()
    });