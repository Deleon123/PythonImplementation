<template>
 <div id="App">
    <MyNavbar/>
  <router-view/>
  
  </div>
</template>

<script>
import MyNavbar from './components/MyNavbar.vue'

export default {
  name: 'App',
  components: {
    MyNavbar
    
}
}
</script>

<style>


</style>
