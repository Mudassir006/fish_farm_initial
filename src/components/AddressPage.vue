<template>
  <div>
    <h2 style="text-align: center">Add Address</h2>
  </div>

  <h4 style="text-align: center">Delivery Address</h4>
  <div>
    <form v-on:submit.prevent="submitForm" style="text-align: center;">
      <div class="form-group">
        <label for="address">Address</label>
        <input id="address" v-model="form.address" class="form-control" style="width: 100%;" placeholder="Address" type="text">
      </div>
      <div class="form-group">
        <label for="phone">Phone</label>
        <input id="phone" v-model="form.phone" class="form-control" style="width: 100%;" placeholder="+92 ----" type="tel">
      </div>
      <div class="form-group">
        <label for="coordinates">Location</label>
        <input id="coordinates" v-model="form.coordinates" class="form-control" style="width: 100%;" type="text">
      </div>
      <div>
        <input class="btn btn-outline-success p-2 m-2" type="button" @click="getLocation" value="Click to get location">
      </div>
      <div class="form-group">
        <button class="btn btn-primary" @click="getformData">Submit</button>
      </div>
    </form>
  </div>


  <div v-for="any in cart.items.user_relation.delivery_addresses" :key ="any" class="review-tile m-4">
    <div><h1 style="text-align: center">Saved Addresses</h1></div>
    <p>Address :
     {{any.address}}


    </p>
    <p>Phone#  {{any.phone}}</p>
    <p> Deliver Coordinates:  {{any.coordinates}}</p>

    <router-link to="/cart/address/summary"><button @click="chosenaddress(any)" class="btn btn-outline-danger">Proceed With this Address</button></router-link>
  </div>
</template>

<script>

import axios from "axios";
import {cartItems, getAddress, getUser} from "@/productstore";

export default {
  name: "AddressPage",
  setup(){

    const cart = cartItems();
    const address = getAddress();
    const user = getUser()

    return {
      cart,
      address,
      user,
    }


  },
  props:['data'],

  created() {
    const cart = cartItems();

    const id = 1

    axios
        .get("http://127.0.0.1:8000/cart/id/" + id)
        .then((response) => {
          cart.setOne(response.data);
          this.calculateCartGrandTotal();
        })
        .catch((error) => {
          console.error("An error occurred:", error);
        });
    axios.get('http://127.0.0.1:8000/user/id/'+1)
        .then(res => {
          this.user.setOne(res.data)

        }).catch(e => {
          alert(e)
    })
  },
  data() {
    return {
      form: {
        user_id: this.user.user.user_id,
        city_id: 1,
        address: "",
        phone: "",
        coordinates: ""
      },
      locationText: ""
    };
  },
  methods: {
    chosenaddress(item){

      this.address.setOne(item)

    },

    showPosition(position) {
      this.locationText =
        position.coords.latitude + "," + position.coords.longitude;
      this.form.coordinates = this.locationText; // Set coordinates field
    },
    getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.showPosition);

      } else {
        this.locationText = "Geolocation is not supported by this browser.";
      }
    },

    getformData() {
      axios
        .post("http://127.0.0.1:8000/delivery_address", this.form)
        .then((response) => {
          if (response.status === 200) {
            alert("Address added successfully");

          }
        })
        .catch((error) => {
          alert(error);
        });
    }
  }
};
</script>

<style scoped>
</style>
