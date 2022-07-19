console.log('Ishlayabdi')


var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId,"action:", action)		
 	
 		console.log('User:', user)
 		if(user == 'AnonymousUser'){
 			console.log('Not logging in')
 	 	}else{
 	 		updateUserOrder(productID, action)
 	 	}
   })
}


function updateUserOrder(productId, action){
	console.log('User is loggon')

	var url = '/update_item/'
	fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',

		},
		body:JSON.stringify({'productID': producID, 'action':action})
	})
	.then((response) =>{
		return response.json()
		})
	.then((data) => {
		console.log('data:', data)
		location.reload()
	})
}