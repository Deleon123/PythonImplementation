<template>
  <h1> é o Home </h1>
</template>

<script>
export default {

  methods: {
    getOperadoras(){
      fetch('http://localhost:5000/get',{
          method:"GET",
          headers: {
            "Content-Type": "application/json"
          }
      })
      .then(resp => resp.json())
      .then(data => {
        console.log(data);
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created(){
    this.getOperadoras()
  }
}
</script>

<style>

</style>