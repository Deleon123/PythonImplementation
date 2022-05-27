<template>
    <div class="container mt-5">
  <form>
  <div class="form-group">
    <label for="exampleFormControlInput1">Digite a pesquisa aqui (texto, registro ans, representante e etc)</label>
    <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Exemplo: Unimed">
  </div>
  <div class="form-group">
    <label for="exampleFormControlSelect1">A partir de qual informação você deseja pesquisar?</label>
    <select class="form-control" id="exampleFormControlSelect1">
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
</div>

</template>

<script>
export default {

}
</script>

<style>

</style>