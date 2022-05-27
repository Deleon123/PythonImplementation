<template>
  <nav class="navbar navbar-expand-lg bg-dark">
  <div class="container">
    <router-link class="navbar-brand text-style" to="/">Teste 4 usando Flask e Vue3</router-link>     
     <ul class="navbar-nav">
        <li class="nav-item" style="padding-right:20px;">
          <router-link class="btn btn-primary" aria-current="page" to="/">Home</router-link>
        </li>
        <li class="nav-item">
          <router-link class="btn btn-success" to="/MyCreate">Create</router-link>
        </li>
      </ul>
  </div>
</nav>
</template>

<script>
export default {

}
</script>

<style>
.text-style {
    font-size: 45px !important; 
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif !important;
    color: goldenrod !important;

}
</style>