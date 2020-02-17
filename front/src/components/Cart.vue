<template>
 <div class="right-side-cart-area show" >

        <!-- Cart Button -->
        <div class="cart-button">
            <a href="#" @click="close" id="rightSideCart"><img src="../assets/img/core-img/bag.svg" alt=""> <span>3</span></a>
        </div>

        <div class="cart-content d-flex">

            <!-- Cart List Area -->
            <div class="cart-list">
                <!-- Single Cart Item -->
                <div v-for="item in products" :key="item.id" class="single-cart-item">
                    <a href="#" class="product-image">
                        <img :src="item.product.img" class="cart-thumb" alt="">
                        <!-- Cart Item Desc -->
                        <div class="cart-item-desc">
                          <span @click="deleteCard(item.id)" class="product-remove"><i class="fa fa-close" aria-hidden="true"></i></span>
                            <span class="badge">{{item.product.name}}</span>
                            <span class="badge">{{item.quantity}} шт.</span>
                            <span class="badge">{{item.price_sum}} грн.</span>
                        </div>
                    </a>
                </div>
                <!-- Single Cart Item -->
            </div>

            <!-- Cart Summary -->
            <div class="cart-amount-summary">

                <h2>Корзина</h2>
                <span>В корзине вы можете смотреть заказы, та удалять </span>
                <p>Что б скрыть корзину повторно нажмите на значок</p>

            </div>
        </div>
    </div>
 </template>
<script>
    export default {
        name: 'Cart',
        data() {
            return {
                products: [],
            }
        },
        created() {
            this.getProducts()
          },
        methods:{
            getProducts() {
                fetch('http://127.0.0.1:8000/cart', {
                    method: "GET",
                    mode: "cors",
                    headers: {
                        'Authorization': "Token " + sessionStorage.getItem('auth_token'),
                        'Accept': 'application/json, text/plain, */*',
                        'Content-Type': 'application/json',
                    },
                }).then(response => {
                    return response.json()
                }).then(json => {
                    this.products = json
                    console.log(this.products)
                })
            },
            close(){
                console.log("click открыое cart")
                return this.$emit('cartClick')
            },
             deleteCard(id){
                 fetch(`http://127.0.0.1:8000/delete/${id}`, {
                    method: "DELETE",
                    headers: {
                        'Authorization': "Token " + localStorage.getItem('auth_token'),
                        'Accept': 'application/json, text/plain, */*',
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        product: id,
                    })
                })
                .then(response => response.json())
                .then(response => {
                    alert("Delete")

                })
                .catch(error => alert(error.statusText))
                this.getProducts()
            }
        },

   };
</script>
 <style scoped>
    .show {
        right: 0;
    }
 </style>
