<template>
<div class="Category">
    <h6 class="widget-title mb-30">Catagories</h6>
    <div class="catagories-menu">
        <ul id="menu-content2" class="menu-content collapse show">
            <!-- Single Item -->
            <li>
                <a href="/" @click="getCategory(item.url)">Все</a>
            </li>
            <li v-for="item in productList" :key="item.id" data-toggle="collapse" data-target="#clothing">
                <a href="#" @click="getCategory(item.url)">{{item.name}}</a>
            </li>
            <!-- Single Item -->
        </ul>
    </div>
</div>
</template>
<script>
export default {
  name: 'Category',

data() {
    return {
      productList: [],
    }
  },
  created() {
    fetch('http://127.0.0.1:8000/category', {
        method: "GET",
        mode: "cors",
    }).then(response => {
        return response.json()
    }).then(json => {
        this.productList = json
    })
  },
  methods:{
    getCategory(slug){
        console.log(slug)
        return this.$emit('getProducts', slug)
    }
  }
  }
</script>