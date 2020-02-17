<template>
<div>
    <header class="header_area">
     <!-- <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link> -->
        <div class="classy-nav-container breakpoint-off d-flex align-items-center justify-content-between">
            <!-- Classy Menu -->
            <nav class="classy-navbar" id="essenceNav">
                <!-- Logo -->
                <a class="nav-brand" href="/"><img src="../../assets/img/core-img/lilia.jpg" alt=""></a>
                <!-- Navbar Toggler -->
                <div class="classy-navbar-toggler">
                    <span class="navbarToggler"><span></span><span></span><span></span></span>
                </div>
                <!-- Menu -->
                <div class="classy-menu">
                    <!-- close btn -->
                    <div class="classycloseIcon">
                        <div class="cross-wrap"><span class="top"></span><span class="bottom"></span></div>
                    </div>
                    <!-- Nav Start -->
                    <div class="classynav">
                        <ul>
                            <li><a href="/">Главная</a>
                                <div class="megamenu">
                                    <ul class="single-mega cn-col-4">
                                        <li class="title">Women's Collection</li>
                                    </ul>
                                    <ul class="single-mega cn-col-4">
                                        <li class="title">Men's Collection</li>
                                    </ul>
                                    <ul class="single-mega cn-col-4">
                                        <li><a href="shop.html">Trench</a></li>
                                    </ul>
                                    <div class="single-mega cn-col-4">
                                        <img src="img/bg-img/bg-6.jpg" alt="">
                                    </div>
                                </div>
                            </li>
                            <li><a href="contact">Контакты</a></li>
                        </ul>
                    </div>
                    <!-- Nav End -->
                </div>
            </nav>

            <!-- Header Meta Data -->
            <div class="header-meta d-flex clearfix justify-content-end">
                <!-- Search Area -->
                <div class="search-area">
                    <form action="#" method="post">
                        <input type="search" name="search" id="headerSearch" placeholder="Type for search">
                        <button type="submit"><i class="fa fa-search" aria-hidden="true"></i></button>
                    </form>
                </div>
                <!-- Favourite Area -->
                <div class="favourite-area">
                    <a href="#"><img src="../../assets/img/core-img/heart.svg" alt=""></a>
                </div>
                <!-- User Login Info -->
                <div  class="user-login-info">
                    <a v-if="login" href="#"><button type="button" class="btn btn-outline-dark">Выйти</button></a>
                    <a v-if="!login" href="/login"><img src="../../assets/img/core-img/user.svg" alt=""></a>
                </div>
                <!-- Cart Area -->
                <div class="cart-area">
                    <a href="#" @click="showCart" id="essenceCartBtn"><img src="../../assets/img/core-img/bag.svg" alt=""> <span>3</span></a>
                </div>
            </div>
        </div>
    </header>
 <div class="cart-bg-overlay"></div>
    </div>
</template>

<script>
import Login from '@/views/Login.vue'

    export default {
        name: 'Nav',
        components: {
            Login,
        },
        data() {
            return {
                login: false,
            }
        },
        created() {
            if (localStorage.getItem("auth_token")) {
               this.login = true
            } else {
                this.login = false
            }
        },
        methods:{
            showCart(){
                console.log("click cart")
                return this.$emit('cartClick')
            },
            setLogin(value) {
                this.login = value
            }
        }
    };
</script>

