<template>
  <div class="bg-white">
   <Selector @clicked="groupBy" v-bind:options="options" /> 
    <div v-if="canAddClient">
      <button v-on:click ='newOne = !newOne' class="fixed z-50 bottom-10 right-10 w-12 h-12 bg-red-600 rounded-full hover:bg-red-700 active:shadow-lg mouse shadow transition ease-in duration-200 focus:outline-none">
        <div v-if="newOne">
          <XIcon class="text-white" aria-hidden="true" />
        </div>
        <div v-else>
          <PlusIcon class="text-white" aria-hidden="true" />
        </div>
      </button>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-7 lg:px-8">
        <dl class="space-y-10 md:space-y-0 md:grid md:grid-cols-2 md:gap-x-8 md:gap-y-10">
          <div v-for="client in clientsSorted" :key="client" class="relative">
             <Disclosure v-bind:title="client.person.name">
              <div class="grid relative md:grid-cols-2 sm:grid-cols-1">
                <div>
                  <span class="font-extrabold">Nombre: </span>
                  <input class="sm:w-10 md:w-52" :disabled="!isBeingChange(client.get_absolute_url)" type="text" v-model="client.person.name" placeholder="Nombre..." aria-label="Full name">
                  <span class="font-extrabold">Identificacion: </span>
                  <input class="sm:w-10 md:w-52" :disabled="!isBeingChange(client.get_absolute_url)" type="number" v-model="client.person.identification" placeholder="Identificacion" aria-label="Full name">
                </div>
                
                <div>
                  <span class="font-extrabold">Email : </span>
                  <br>
                  <textarea class="sm:w-10 md:w-44" :disabled="!isBeingChange(client.get_absolute_url)" type="text" v-model="client.person.mail" placeholder="Email" aria-label="Full name">
                  </textarea>
                </div>
                <div>
                  <span class="font-extrabold">Telefono: </span>
                  <input class="sm:w-10 md:w-52" :disabled="!isBeingChange(client.get_absolute_url)" type="number" v-model="client.person.phone" placeholder="Telefono" aria-label="Full name">
                </div>
                <div>
                  <span class="font-extrabold">Balance: </span>
                  <input class="sm:w-10 md:w-40" :disabled="!isBeingChange(client.get_absolute_url)" type="number" v-model="client.balance" placeholder="Balance" aria-label="Full name">
                </div>
                <div> 
                  <button  v-if="canDeleteClient" v-on:click ='deleteClient(client.person.id)' type="button" class="absolute top-0 right-8 -mr-1 p-2 rounded-md transition hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-white sm:-mr-2">
                    <i class="fa fa-trash fa-lg"></i>
                  </button> 
                  <div v-if="canChangeClient">
                    <button v-if="!(changing === client.get_absolute_url)" @click="changing = client.get_absolute_url" type="button" class="absolute top-0 right-0 -mr-1 p-2 rounded-md transition hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-white sm:-mr-2">
                      <i class="fas fa-pencil-alt fa-lg"></i>
                    </button> 
                    <div v-else>
                      <button  type="button"  v-on:click ="modifyClient(client)"  class="absolute top-8 right-0 -mr-1 p-2 rounded-md transition hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-white sm:-mr-2">
                        <i class="fas fa-save fa-lg"></i>
                      </button>
                      <button v-on:click ='changing = ""' type="button" class="absolute top-0 right-0 -mr-1 p-2 rounded-md transition hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-white sm:-mr-2">
                        <i class="fas fa-times-circle fa-lg"></i>
                      </button>
                    </div>
                  </div> 
                </div>
              </div>
            </Disclosure>
          </div>
           <Disclosure v-bind:title="'Nuevo Cliente'" v-if="newOne">
            <div class="relative">
              <form class="w-full max-w-sm">
                <div class="flex items-center border-b border-teal-500 py-2">
                  <input v-model="name" class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" placeholder="Nombre del cliente" aria-label="Full name">
                </div>
                <div class="flex items-center border-b border-teal-500 py-2">
                  <input v-model="identification" class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="number" placeholder="Identificacion" aria-label="Full name">
                </div>
                <div class="flex items-center border-b border-teal-500 py-2">
                  <input v-model="phone" class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="number" placeholder="Número telefónico" aria-label="Full name">
                </div>
                <div class="flex items-center border-b border-teal-500 py-2">
                  <textarea v-model="mail" class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" placeholder="Correo electrónico" aria-label="Full name">
                  </textarea>
                </div>
              </form>
              <button type="button" v-on:click ="addClient" class="absolute top-0 right-0 -mr-1 p-2 rounded-md transition hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-white sm:-mr-2">
                <i class="far fa-save fa-lg"></i>
              </button>   
            </div>
          </Disclosure>
        </dl>
      </div>
    </div>
</template>

<script>
import axios from "axios";
import { toast } from 'bulma-toast'
import Selector from "../components/Selector";
import Multiselect from '@vueform/multiselect';
import Disclosure from "../components/Disclosure";
import { PlusIcon, CheckCircleIcon,XIcon } from "@heroicons/vue/outline";

export default {
  name: "Clients",
  components: {
    Selector,
    PlusIcon,
    Disclosure,
    Multiselect,
    CheckCircleIcon,
    XIcon,
  },
  data() {
    return {
      // Objetos internos
      clients: [],
      clientsSorted:[],
      options:[
        {
          name:"Todos",
          get_absolute_url:"All" 
        },
        {
          name:"Activos",
          get_absolute_url:"Activo" 
        },
        {
          name:"Morosos",
          get_absolute_url:"Moroso" 
        }
      ],

      // Banderas
      newOne:false,
      is_loaded:false,
      changing:String,

      // Permisos
      permissions: this.$store.state.permissions,
      
      // Parametros para AddClient
      name:"",
      mail:"",
      phone:"",
      balance:"",
      clientstate:"",
      identification:"",
    };
  },
  mounted() {
    this.getClients().then(()=>{
        this.clientsSorted = this.clients
    });
  },
  computed:{
    canAddClient() {
      return this.permissions.includes("gymClients.add_client")
    },
    canDeleteClient() {
      return this.permissions.includes("gymClients.delete_client")
    },
    canChangeClient() {
      return this.permissions.includes("gymClients.change_client")
    },
  },
  methods: {
    async addClient(){
      this.$store.commit("setIsLoading", true);
      let formAux ={
        person:{
        id:0,
        name: this.name,
        identification: this.identification,
        mail: this.mail,
        phone: this.phone
        },
        balance:0,
        clientstate:"Activo",
        get_absolute_url: ""
      }

      const formData = {
        name: this.name,
        identification: this.identification,
        mail: this.mail,
        phone: this.phone,
      }
      await axios
      .post("/api/v1/clients/", formData)
      .then(response => {
          formAux.get_absolute_url = "/"+response.data.toString()+ "/"
          formAux.person.id = response.data
          this.clients.push(formAux);
          toast({
            message: "Cliente matriculado exitosamente. Para modificar refresque la página", type: "is-success",
            dismissible: true, pauseOnHover: true,
            duration: 3000, position: "bottom-right",
          });
      })
      .catch(error => {
          toast({
            message: "Ocurrio un problema insertando al servicio", type: "is-danger",
            dismissible: true, pauseOnHover: true,
            duration: 3000, position: "bottom-right",
          });
      })

      this.name="",
      this.mail="",
      this.phone="",
      this.balance="",
      this.clientstate="",
      this.newOne = false;
      this.$store.commit("setIsLoading", false);
    },
    isBeingChange(id){
      if(id == this.changing) return true
      return false
    },
     async deleteClient(client_id){
      this.$store.commit("setIsLoading", true);
      await axios
      .delete("/api/v1/clients/"+client_id)
      .then((response) =>{
         this.clients.forEach(element => {
            if(element.person.id == client_id){
              const index = this.clients.indexOf(element);
              this.clients.splice(index, 1);
            }
        });
        toast({
            message: "Cliente eliminado exitosamente", type: "is-success",
            dismissible: true, pauseOnHover: true,
            duration: 3000, position: "bottom-right",
          });
      })
      .catch((error) => {
          toast({
            message: "Ocurrio un problema con los datos de: Cliente", type: "is-danger",
            dismissible: true, pauseOnHover: true,
            duration: 3000, position: "bottom-right",
          });
        });
      this.$store.commit("setIsLoading", false);

    },
    async modifyClient(client){
      this.$store.commit("setIsLoading", true);
      const  formData ={
        person:{
          name: client.person.name,
          identification: client.person.identification,
          mail: client.person.mail,
          phone: client.person.phone
        },
        balance:client.balance,
        clientstate:client.clientstate
      }
      await axios
      .put("/api/v1/clients"+client.get_absolute_url, formData)
      .then(response => {
          toast({
            message: "Servicio editado exitosamente", type: "is-success",
            dismissible: true, pauseOnHover: true,
            duration: 3000, position: "bottom-right",
          });
          this.changing =  ""
      })
      .catch(error => {
          toast({
            message: "Ocurrio un problema al editar el instructor", type: "is-danger",
            dismissible: true, pauseOnHover: true,
            duration: 3000, position: "bottom-right",
          });
      })
      this.$store.commit("setIsLoading", false);
    },
    async getClients() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get("/api/v1/clients/")
        .then((response) => {
          this.clients = response.data;
        })
        .catch((error) => {
          toast({
            message: "Ocurrio un problema cargando los clientes", type: "is-danger",
            dismissible: true, pauseOnHover: true,
            duration: 3000, position: "bottom-right",
          });
        });
      this.$store.commit("setIsLoading", false);
    },
    isBeingChange(id){
      if(id == this.changing) return true
      return false
    },
    groupBy(id) {
      if (id == "All") return this.clientsSorted = this.clients
      this.clientsSorted = []

      // Filter them 
      let clientsAux 
      for(let i=0; i <this.clients.length; i++ ){
        clientsAux = this.clients[i]
        if(clientsAux.clientstate == id) this.clientsSorted.push(this.clients[i])
      }
      console.log(this.clientsSorted)
    },
  },
};
</script>