
let addBtn = document.querySelector('#plus-cart');
let subBtn = document.querySelector('#minus-cart');
let qty = document.querySelector('#quantity');
addBtn.addEventListener('click',() =>{
	qty.value = parseInt(qty.value) + 1;
})

