 <template>
 <div class="product_detail">
 <div class="right-side-cart-area">

        <!-- Cart Button -->
        <div class="cart-button">
            <a href="#" id="rightSideCart"><img src="img/core-img/bag.svg" alt=""> <span>3</span></a>
        </div>
    </div>
     <section class="single_product_details_area d-flex align-items-center">

        <!-- Single Product Thumb -->
        <div class="single_product_thumb clearfix">
            <div class="product_thumbnail_slides">
                <img :src="product.img" style="width: 500px;  alt="">
            </div>
        </div>

        <!-- Single Product Description -->
        <div class="single_product_desc clearfix">
            <a href="cart.html">
                <h2>{{product.name}}</h2>
            </a>
            <p class="product-price">{{product.price}} грн.</p>
            <p class="product-desc">{{product.description}}.</p>

            <!-- Form -->
            <form class="cart-form clearfix" method="post">
            	<p><input v-model="quantity" class="input100" type="number" value="1" name="quantity"><span> количество</span></p><br>
                <div class="cart-fav-box d-flex align-items-center">
                    <!-- Cart -->
                    <p><button type="button" name="addtocart" class="btn essence-btn" @click="addCard(product.id)">Add to cart</button></p>
                    <!-- Favourite -->
                    <div class="product-favourite ml-4">
                        <a href="#" class="favme fa fa-heart"></a>
                    </div>
                </div>
                <p><span>телефон:</span> 095 452 4437</p>

            </form>
            <Coments/>

        </div>
    </section>
    </div>
 </template>


<script>
import Coments from '@/components/Coments.vue'

export default {
  name: 'ProductDetail',
  components: {

  },
  data() {
    return {
      url: "http://127.0.0.1:8000",
      product: {},
      quantity: 1
    }
  },
  created() {
    fetch('http://127.0.0.1:8000/'+ this.$route.params.id, {
        method: "GET",
        mode: "cors",
    }).then(response => {
        return response.json()
    }).then(json => {
        this.product = json
        console.log("product" + this.product.name)
    })
  },
 methods:{
        addCard(id){
             fetch("http://127.0.0.1:8000/add-item/", {
                method: "POST",
                headers: {
                    'Authorization': "Token " + sessionStorage.getItem('auth_token'),
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    product: id,
                    quantity: this.quantity
                })
            })
            .then(response => response.json())
            .then(response => {
                alert("Add")
            })
            .catch(error => alert(error.statusText))
        },
  }}
</script>