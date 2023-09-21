<template>


  <div class="container-fluid" style="background-color: #fefdf8">
    <nav class="navbar  navbar-expand-lg b ">
      <a class="navbar-brand" href="#" style="margin-left: 10%">
        <img alt="Farm" height="40" src="/image.png" width="max">
      </a>
      <button aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"
              class="navbar-toggler" data-target="#navbarNav" data-toggle="collapse" type="button">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div id="navbarNav" class="collapse navbar-collapse ">
        <ul class="navbar-nav custom-align">


          <li class="nav-item">
            <a class="nav-link" href="#blog" style="font-weight: bold;color: black">Blog</a>
          </li>

          <li class="nav-item" v-if="!isAuthenticated"   >
            <button

                class="nav-link"
                style="font-weight: bold; color: black; background: inherit; border: none"
                type="submit"
                @click="signin"
            >
              Sign in
            </button>


          </li>


          <li class="nav-item">
            <a class="nav-link" href="#footer" style="font-weight: bold;color: black">Contact Us</a>

          </li>


          <li class="nav-item">
            <div class="dropdown">
              <button aria-expanded="true" class="btn btn-primary dropdown-toggle"
                      data-bs-toggle="dropdown"
                      style="background-color: inherit; color: black; border: none; font-weight: bold"
                      type="button">
                Rick
              </button>
              <ul class="dropdown-menu" style="border-radius: 20px">
                <li>
                  <button class="dropdown-item"
                          type="button"><small>alphahorder@beta.com</small></button>
                </li>
                <li>
                  <button class="dropdown-item" type="button"><small>My Account</small></button>
                </li>
                <li>
                  <button class="dropdown-item" type="submit" @click="logout"><small
                      style="color:#fb585e;">Logout</small>
                  </button>
                </li>

              </ul>
            </div>


          </li>
          <li class="nav-item">
            <router-link to="/cart"><i class="fa" style="font-size:24px ;color: #f33644">&#xf07a;</i>
<span class='badge badge-warning' id='lblCartCount' style="font-size: 12px;
    background: whitesmoke;
    color: black;
    padding: 0 5px;
    vertical-align: top;
    margin-left: -10px;"> 2 </span>
            </router-link>


          </li>
        </ul>
      </div>
    </nav>

    <div class="row col-md-12" style="padding-top: 5%">
      <br>
      <br>
      <br>

      <div class="col-md-6 mb-4" style="padding-left: 40px ">
        <div class="row">
          <div class="twobuttons" style="margin-left: 50px ;  width: 440px; padding-left: 40px">

            <div
                style="; border: none;  width:400px;  margin-top: 40px ; margin-left: 10%; padding-bottom: 40px; height: 100px ">


              <select aria-label="Default select example" class="form-select"
                      style="margin: 10px;width: 90%; height: 50px; border-radius: 20px; ">
                <option v-for="s in cities" :key="s">{{ s.name }}</option>


              </select>


            </div>
            <div class="container mt-5 ">
              <div class="input-group " style="position: relative;">
                <input class="form-control" placeholder="Search product"
                       style="padding-left: 10px; background-color: inherit; border-radius: 20px; height: 45px ; border: 1px solid gray; width: 150px"
                       type="text">
                <span class="input-group-prepend"
                      style="position: absolute; top: 50%; transform: translateY(-50%); right: 1px; z-index: 1;">
                                    <a href=""><i class="fa fa-search" style="padding-right: 10px; color: grey"></i></a>
                                </span>

              </div>
            </div>


          </div>
        </div>
        <div
            style="background-color: white; border: 1px solid darkgrey; box-shadow: black; display: flex; flex-direction: column; width:400px; border-radius: 10px; margin-top: 40px ; margin-left: 10%; padding-bottom: 40px; ">


          <select aria-label="Default select example" class="form-select"
                  style="margin: 10px;width: 90%; height: 50px;border-radius: 15px">
            <option v-for="f in products " :key="f">{{ f.name }}
            </option>


          </select>


          <input id="quantity" name="quantity" placeholder="Quantity"
                 style="margin: 10px;width: 90%; height: 50px; border-radius: 10px;border: 1px solid gray;text-align: inherit"
                 type="number">


          <button class="btn" style="border-radius: 10px; margin: 15px;background-color: #fb585e;color: white ">
            Add to cart
          </button>


        </div>


      </div>
      <div class="col-md-6 mb-2" style="border-radius: 50%">

        <img alt="" class="base" src="/admin.jpg"
             style="border-radius: 50%; width: 80%; margin-bottom: 50px;padding-bottom: 50px;">
      </div>
    </div>

  </div>
  <div>

  </div>

</template>

<script>
import keycloak from "../main";


import CartPage from "@/components/CartPage";
import axios from "axios";
import {ref, watch} from "vue";

import {getUser} from "@/productstore"; // Import the router instance from your main.js


export default {


  name: "NavBar",
  components: CartPage,
  setup() {
    const user = getUser()
    const isAuthenticated = ref(
        keycloak.authenticated
    );


    watch(isAuthenticated, (newValue) => {

      keycloak.onAuthLogout.isAuthenticated.value = newValue
      keycloak.onAuthSuccess.isAuthenticated.value = newValue
    });

    const signin = () => {
      console.log("user is sign in")
      keycloak.login();
    };

    const logout = () => {
      console.log("user sign out")
      keycloak.logout();
      localStorage.clear()
    };


    return {
      isAuthenticated,
      signin, logout,

      user,
    };
  },
  computed() {


    return {
      keycloak
    }
  },





  blogs: {}, products: {},

  data() {
    return {
      products: null,
      cities: null,
      name: '',
      count: 0


    }
  },
  mounted() {
    //  axios.get('http://127.0.0.1:8000/user/id/' + 1 )
    //     .then(res => {
    //       this.user.setOne(res.data)
    //
    //     }).catch(e => {
    //   console.log(e)
    // })
    axios.get('http://127.0.0.1:8000/all_cities')
        .then(response => {
          this.cities = response.data; // Store the response data in the responseData property
        })
        .catch(error => {
          console.error('An error occurred:', error);
        });
    axios.get('http://127.0.0.1:8000/all_products')
        .then(response => {
          this.products = response.data; // Store the response data in the responseData property
        })
        .catch(error => {
          console.error('An error occurred:', error);
        });

  },
  methods: {},


}
</script>
<style>

@media (max-width: 1409px) {
}

@media (max-width: 950px) {


}

@media (max-width: 1265px) {
  .base {
    padding-top: 70px;
  }

}

@media (min-width: 1500px) {
}

.navbar-nav.custom-align {
  margin-left: 60%;
}

.twobuttons {
  display: flex;
@media (max-width: 768 px)
}


.row:after {
  content: "";
  display: table;
  clear: both;
}

@media (max-width: 984px) {
  .base {
    max-width: 100%;
    max-height: 100%;
    margin-left: 30%;
    margin-top: 20px;
    border-radius: 50%;
    padding: 10px;

  }
}


</style>

