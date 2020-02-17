<template>
  <div class="home">
    <div class="cart-bg-overlay"></div>


    <!-- ##### Breadcumb Area Start ##### -->
    <div class="breadcumb_area bg-img" style="background-image: url(../assets/img/bg-img/breadcumb.jpg);">
        <div class="container h-100">
            <div class="row h-100 align-items-center">
                <div class="col-12">
                    <div class="page-title text-center">
                        <h2>Шмотки</h2>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- ##### Breadcumb Area End ##### -->

    <!-- ##### Shop Grid Area Start ##### -->
    <section class="shop_grid_area section-padding-80">
        <div class="container">
            <div class="row">
                <div class="col-12 col-md-4 col-lg-3">
                    <div class="shop_sidebar_area">

                        <!-- ##### Single Widget ##### -->
                        <div class="widget catagory mb-50">
                         <Category @getProducts="getProducts"/>
                        </div>
                    </div>
                </div>

                <div class="col-12 col-md-8 col-lg-9">
                    <div class="shop_grid_product_area">


                        <div class="row">

                            <!-- Single Product -->
                            <div v-for="item in productList" :key="item.id" class="col-12 col-sm-6 col-lg-4">
                                <div class="single-product-wrapper">
                                    <!-- Product Image -->
                                    <div class="product-img">
                                        <img :src="url + item.img" style="width: 150px; height: 175px;"  alt="">
                                        <!-- Hover Thumb -->
                                        <img class="hover-img" src="" alt="">

                                        <!-- Product Badge -->
                                        <!-- Favourite -->
                                        <div class="product-favourite">
                                            <a href="#" class="favme fa fa-heart"></a>
                                        </div>
                                    </div>

                                    <!-- Product Description -->
                                    <div class="product-description">
                                        <span>{{item.description }}</span>
                                        <a :href="item.id">
                                            <h6>{{item.name}}</h6>
                                        </a>
                                        <p class="product-price"><span class="old-price"></span> {{item.price}} грн.</p>

                                        <!-- Hover Content -->
                                        <div class="hover-content">
                                            <!-- Add to Cart -->
                                            <div class="add-to-cart-btn">
                                                <a :href="item.id" class="btn essence-btn">Подробнее</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>


                        </div>
                    </div>
                    <!-- Pagination -->
                    <nav aria-label="navigation">
                        <ul class="pagination mt-50 mb-70">
                            <li class="page-item"><a class="page-link" href="#"><i class="fa fa-angle-left"></i></a></li>
                            <li class="page-item"><a class="page-link" href="#">1</a></li>
                            <li class="page-item"><a class="page-link" href="#">2</a></li>
                            <li class="page-item"><a class="page-link" href="#">3</a></li>
                            <li class="page-item"><a class="page-link" href="#">...</a></li>
                            <li class="page-item"><a class="page-link" href="#">21</a></li>
                            <li class="page-item"><a class="page-link" href="#"><i class="fa fa-angle-right"></i></a></li>
                        </ul>
                    </nav>
                </div>
            </div>
        </div>
    </section>
  </div>
</template>

<script>

//import $ from 'jquery';
import Category from "../components/Category.vue"
export default {
  name: 'home',
  components: {
    Category
  },
  data() {
    return {
      url: "http://127.0.0.1:8000",
      productList: [],
    }
  },
  created() {
    fetch('http://127.0.0.1:8000', {
        method: "GET",
        mode: "cors",
    }).then(response => {
        return response.json()
    }).then(json => {
        this.productList = json
    })
  },
    methods:{
        getProducts(slug){
            fetch(`http://127.0.0.1:8000/category/${slug}`, {
            method: "GET",
            mode: "cors",
        }).then(response => {
            return response.json()
        }).then(json => {
            this.productList = json,
            this.url=""
        })
      },
    }
}

</script>
