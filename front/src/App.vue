<template>
  <div id="app">
    <Nav @cartClick="cartClick"/>
    <Cart  @cartClick="cartClick" v-if="cartShow"/>
    <router-view/>
    <Footer/>
  </div>
</template>


<script>
    import $ from 'jquery';  // подключаем jQuery
    //import 'owl'; // подключаем сам плагин
    import Nav from '@/components/nav/Nav.vue'
    import Footer from '@/components/Footer.vue'
    import Cart from '@/components/Cart.vue'


    export default {
    data () {
        return {
            cartShow: false,
        };
    },
        components: {
            Nav,
            Footer,
            Cart,

        },
  mounted () {
    $('#plugin-container').whateverplugin({

       // передаем в плагин данные из свойства Vue
       options: this.options

    });
  },
  methods:{
    cartClick(){
        this.cartShow = !this.cartShow
    }
  }
}
</script>

<style>
    @import './assets/css/bootstrap.min.css';
    @import './assets/css/classy-nav.min.css';
    @import './assets/css/core-style.css';
    @import './assets/css/font-awesome.min.css';
    @import './assets/css/jquery-ui.min.css';
    @import './assets/css/magnific-popup.css';
    @import './assets/css/nice-select.css';
    @import './assets/css/owl.carousel.css';
</style>
