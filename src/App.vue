<template>
  <div>

    <h1>Teste de API</h1>

    <!-- Usei dois métodos para busca com o CNPJ e o Registro Ans-->

    Registo ANS: <input type="radio" 
    v-model="doSearch.method" 
    name="radio_search" 
    value="Ans" 
    checked>  
     
    CNPJ: <input type="radio" 
    v-model="doSearch.method" 
    name="radio_search" 
    value="Cnpj"> 
    
    <br/><br/>

    <input type="number" v-model="doSearch.info" required placeholder="Digite aqui"/>

  </div>

  <br/>

  <button @click="onSearch">Buscar</button>

  <div>

    <br/>

    <h1>{{ message }}</h1>

    <div v-if="message == 'Registro encontrado!'">

      <p>Registro ANS: {{found_data['Registro_ANS']}}</p>
      <p>CNPJ: {{found_data['CNPJ']}}</p>
      <p>Razão Social: {{found_data['Razão Social']}}</p>
      <p>Modalidade: {{found_data['Modalidade']}}</p>
      <p>CEP: {{found_data['CEP']}}</p>
      <p>Telefone: {{found_data['Telefone']}}</p>
      <p>Email: {{found_data['Email']}}</p>
      <p>Representante: {{found_data['Representante']}}</p>
      <p>Região de Comercialização: {{found_data['Regiao_de_Comercializacao']}}</p>
      <p>Data Registro ANS: {{found_data['Data_Registro_ANS']}}</p>

    </div>
    
  </div>
</template>

<script>

// Usando o axios para fazer as requisições
import axios from 'axios';

export default {

  data() {
    return {

      message:'',

      found_data: [],

      doSearch: {
        info: '',
        method: 'Ans',
      },
    };
  },

  methods: {

    // Método para buscar os dados da API
    fetchData() {

      axios.get('http://localhost:5000')
      .then(response => {

        this.found_data = response.data.data;
        this.message = response.data.message;

      })
      .catch(error => {
        console.error(error);
      });
    },

    // Método para postar os dados para o backend
    search_API(payload){

      axios.post('http://localhost:5000', payload)
      .then(()=> {

        this.fetchData();
      
      })
      .catch(error => {

        this.fetchData();
        console.error(error);
      });

    },

    initForm(){
      this.doSearch.info = '';
      this.doSearch.method = 'Ans';
    },

    // Método para coletar os dados do input e enviar para o backend
    onSearch(e){

      e.preventDefault();
      
      const payload = {
        info: this.doSearch.info,
        method: this.doSearch.method
      }

      this.search_API(payload);
      this.initForm();
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
