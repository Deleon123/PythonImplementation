<template>
 <div id="App">
    <MyNavbar/>
    <MySearch/>
  <router-view/>
  
  </div>
</template>

<script>
import MyNavbar from './components/MyNavbar.vue'
import MySearch from './components/MySearch.vue'
export default {
  name: 'App',
  components: {
    MyNavbar,
    MySearch
}
}
</script>

<style>


</style>
