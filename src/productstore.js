// store.js
import { defineStore } from 'pinia';
import {createPinia} from "pinia/dist/pinia";
import {createApp} from "vue";
import App from "@/App";
const app = createApp(App)


const pinia = createPinia()
app.use(pinia)

export const useFishStore = defineStore('fish', {
  state: () => ({
    products: [],
  }),
  actions: {
    setProducts(products) {
      this.products = products;
    },
  },
});
export const singleStore = defineStore('single',{
  state: () => ({
    product:[],
  }),
  actions :{
    setOne(product) {
    this.product =product;
},
  },
});

export const cartItems = defineStore('cart',{
  state: () => ({
    items:[],
  }),
  actions :{
    setOne(items) {
    this.items =items;
},
  },
});

export const singleItem = defineStore('single',{
  state: () => ({
    item:Object
  }),
  actions :{
    setOne(item) {
    this.item =item;
},
  },
});

export const selectedItem = defineStore('selected',{
  state: () => ({
    items:[]
  }),
  actions :{
    setOne(item) {
    this.item =item;
},
  },
});
export const getAddress = defineStore('address',{
  state: () => ({
    address:Object
  }),
  actions :{
    setOne(address) {
    this.address =address;
},
  },
});

export const getUser = defineStore('user',{
  state: () => ({
    user:Object
  }),
  actions :{
    setOne(user) {
    this.user = user;
},
  },
});





