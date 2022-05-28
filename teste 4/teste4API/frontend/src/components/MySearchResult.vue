<template>
    
    <div class="container mt-5"><ol>
        <div v-if="!operadoras.length">Nenhum resultado</div>
      <div v-for="operadora in operadoras" :key="operadora.registro_ans"><li>
        <h3>Registro ANS: {{operadora.registro_ans}}</h3>
        <h4>CNPJ: {{operadora.cnpj}}</h4>
        <p>Razão Social: {{operadora.razao_social}}
        Nome Fantasia: {{operadora.nome_Fantasia}} 
        Modalidade: {{operadora.modalidade }} 
        Logradouro: {{operadora.logradouro }} 
        Número: {{operadora.numero }} 
        Complemento: {{operadora.complemento }} 
        Bairro: {{operadora.bairro }} 
        Cidade: {{operadora.cidade }} 
        UF: {{operadora.uf }} 
        CEP: {{operadora.cep }} 
        DDD: {{operadora.ddd }} 
        Telefone: {{operadora.telefone }}
        Fax: {{operadora.fax }} 
        Endereço de e-mail: {{operadora.endereco_eletronico }} 
        Representante: {{operadora.representante }} 
        Cargo do representante: {{operadora.cargo_representante }} 
        Data de registro: {{operadora.data_registro_ans }} </p>
      </li>
      </div>
    </ol>
    </div></template>

<script>
export default {
                
         data(){
            return {
                    search: this.$route.params.search,
                    searchType: this.$route.params.searchType,
                    operadoras:[],
                 }
            },

        

            methods: {
                    searchOperadoras(){
                                 console.log(  );
                                 console.log(  );
                        fetch('http://localhost:5000/Search/'+this.$route.params.search+'/'+this.$route.params.searchType+'/',{
                        method:"GET",
                        headers: {
                        "Content-Type": "application/json"
                            }
                             })
                             .then(resp => resp.json())
                             .then(data => {
                                    this.operadoras.push(...data)
                                        })
                                    .catch(error => {
                                    console.log(error)
                                   })
    
                          }



            },
            created() {
        
                this.searchOperadoras()

            }


 }

</script>

<style>

</style>