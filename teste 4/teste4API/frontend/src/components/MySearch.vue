<template>
    <div class="container mt-5">
  <form @submit="searchOperadoras">
  <div class="form-group">
    <label for="exampleFormControlInput1">Digite a pesquisa aqui (texto, registro ans, representante e etc)</label>
    <input type="text" class="form-control" v-model="search" placeholder="Exemplo: Unimed">
  </div>
  <div class="form-group">
    <label for="exampleFormControlSelect1">A partir de qual informação você deseja pesquisar?</label>
    <select class="form-control" v-model="searchType">
      <option>Registro ANS</option>
      <option>CNPJ</option>
      <option>Razão Social</option>
      <option>Nome Fantasia</option>
      <option>Modalidade</option>
      <option>Logradouro</option>
      <option>Número</option>
      <option>Complemento</option>
      <option>Bairro</option>
      <option>Cidade</option>
      <option>UF</option>
      <option>CEP</option>
      <option>DDD</option>
      <option>Telefone</option>
      <option>Fax</option>
      <option>Endereço de e-mail</option>
      <option>Representante</option>
      <option>Cargo do representante</option>
      <option>Data de registro</option>
    </select>
  </div>
  <button type="submit" class="btn btn-primary mb-2" style="margin: 20px;">Pesquisar</button>
</form>
<div v-if="error" class="alert alert-warning alert-dismissible fade show mt-5" role="alert">
<strong>{{error}}</strong>
</div> 
</div>

</template>

<script>

export default {
    data(){
      return {
        error: null,
        search: null,
        searchType: null
        
      }
    },
    methods: {
      searchOperadoras() {
          
               
            if((this.search == null || this.searchType == null || this.search == '')) {
              this.error = " Por favor escolha o tipo ou o texto de pesquisa"
            } else {
              this.$router.push({name:'MySearchResult', params: {search: this.search, searchType: this.searchType}})  
            } 

      }
    }
}
</script>

<style>

</style>