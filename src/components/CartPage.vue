<template>
  <section  style="background-color: inherit; margin-bottom: 20px" >
    <div class="container" style="background-color: whitesmoke;  box-shadow: 0 7px 9px rgba(0, 0, 0, 0.2);">
      <h2 style="text-align: center;">Your Cart</h2>
      <div v-for="item in cart.items.cart_items" :key="item.cart_id" class="cart-item card mb-3"
           style="background-color: lavender">

        <div class="row g-0 p-2 m-2">
          <div class="col-md-1 d-flex align-items-center">
            <input
                id="check"
                v-model="item.isSelected"
                :value="item"
                class="form-check-input"
                name="cartItemCheckbox"
                style="text-align: center ; margin-left: 10px; position: absolute; color: red"
                type="checkbox"
                @click="handleCheckboxChange(item)"
            />
            <label :for="'itemCheckbox-' + item.cart_item_id"></label>
          </div>

          <!-- Checkbox -->


          <!-- Product Image -->
          <div class="col-md-2" style="text-align: center">
            <img
                v-for="image in item.business_product_relation.product_relation.product_images"
                :key="image.file_id"
                :src="image.file_id"
                alt="Product Image"
                class="img"
                style="width: 170px;height:175px;border-radius: 50%"
            >

            <h5>{{ item.business_product_relation.product_relation.name }}</h5>
            <p>{{ item.business_product_relation.business_relation.name }}</p>

          </div>


          <div class="col-md-2 d-flex flex-column justify-content-center" style="text-align: center;">
            <p class="mb-0">Rs. {{ item.unit_price }} KG</p>
          </div>


          <div class="col-md-2 d-flex flex-column justify-content-center p-2  ">
            <div v-for="processingOption in item.business_product_relation.processing_options"
                 :key="processingOption.processing_option_id">
              <input id="radio" :value="processingOption.processing_option_relation.product_processing" name="radio"
                     type="radio"/>
              <label class="mb-0 p-2"> {{ processingOption.processing_option_relation.product_processing }}</label>
            </div>
          </div>


          <div class="col-md-2 d-flex flex-column justify-content-center">
            <div class="quantity">
              Quantity
              <button class="btn btn-outline-danger " @click="decrement(item)" style=" font-size: 20px ; border-radius: 70%;width: 40px">-</button>
              <span class="mx-2">{{ item.quantity }}</span>
              <button class="btn btn-outline-danger" @click="incrementQuantity(item)" style=" font-size: 20px ; border-radius: 70% ; width: 40px" >+</button>
            </div>
          </div>


          <div class="col-md-1 d-flex flex-column justify-content-center">
            <p class="mb-0">Total Price: Rs. {{ item.quantity * item.unit_price }}</p>
          </div>


          <div class="col-md-1 d-flex align-items-center">
            <a @click="del(item)"><i class="fa-regular fa-trash-can" style="font-size: 20px;color: red"></i>
            </a>
          </div>
        </div>
      </div>


      <div class="row p-4">
        <div class="col-md-5"></div>
        <div class="col-md-3 d-flex justify-content-end align-items-center">
          <h4 id="alpha" class="mb-0">Grand Total: Rs. {{ cartGrandTotal }}</h4>
        </div>
        <div class="col-md-2 float-end">
          <button class="btn btn-outline-success" :disabled="isNextButtonDisabled">
            <router-link to="/cart/address" style="color: black;text-decoration: none">
              Next</router-link>
          </button>

        </div>
      </div>
    </div>
    <p>{{x}}</p>
  </section>
 </template>

<script>
import {cartItems, selectedItem, singleItem, singleStore} from "@/productstore";
import axiosInstance from "@/auth";
import keycloak from "@/main";

export default {
  name: "CartPage",
  mounted() {

    const cart = cartItems();

  if(keycloak.authenticated){
    axiosInstance
        .get("/cart/id/" + this.id)
        .then((response) => {
          cart.setOne(response.data);
          this.calculateCartGrandTotal();

        })
        .catch((error) => {
          console.error("An error occurred:", error);
        });}else {
    document.getElementById('alpha').innerHTML='Please Sign up or Login'
  }
  },

  setup() {
    const cart = cartItems();
    const single = singleStore();
    const item = singleItem();
    const select =selectedItem()

    return {
      single,
      cart,
      item,
      select,
      selectedItems: [],
      cartGrandTotal: 0,
    };
  },

  data() {
    return {
      id: 1,
      x:this.select.items,
      isNextButtonDisabled: true
    };
  },
  computed: {
  isAnyItemSelected() {
    return this.select.items.length > 0;
  }
},


  methods: {

    axis(xor) {
      axiosInstance
          .patch("/update_cart_item/" + xor.cart_item_id, {
            quantity: xor.quantity,

          })
          .then(function (response) {
            console.log(response);
          });
    },
    calculateCartGrandTotal() {
      this.cartGrandTotal = this.cart.items.cart_items.reduce((total, item) => {
        if (item.isSelected) {
          total += item.quantity * item.unit_price;
        }
        return total;
      }, 0);
    },

    handleCheckboxChange(item) {
      if (item.isSelected) {
        this.select.items.pop(item)


        this.cartGrandTotal -= item.quantity * item.unit_price;
      } else {
        this.select.items.push(item)


        this.cartGrandTotal += item.quantity * item.unit_price;
      }
      this.isNextButtonDisabled = !this.isAnyItemSelected;
    },

    async del(obj) {
      try {
        const response = await axiosInstance.delete("http://127.0.0.1:8000/delete_citem/" + obj.cart_item_id);
        if (response.status === 204) {
          alert("Item Deleted");

          const index = this.cart.items.cart_items.findIndex(item => item.cart_item_id === obj.cart_item_id);
          if (index !== -1) {
            this.cart.items.cart_items.splice(index, 1);

            this.calculateCartGrandTotal();
          }
        }
      } catch (error) {
        alert("Something went wrong")
      }
    },

    incrementQuantity(item) {


      if (item.isSelected) {
        item.quantity++;
        this.axis(item)
        this.cartGrandTotal += item.unit_price;

      } else {
        item.quantity++
        this.axis(item)
      }
    },

    decrement(item) {

      if (item.quantity > 1 && item.isSelected) {
        item.quantity--;
        this.axis(item)
        this.cartGrandTotal -= item.unit_price;
      } else if (item.quantity > 1) {
        item.quantity--
        this.axis(item)
      }


    },


  },
};
</script>

<style scoped>

#check:checked {
  border-color: red;
  background-color: red;
}

#radio {
  accent-color: red;
}
@media (max-width: 1000px)  {

  .cart-item card {
    height: 50%;
  }

}


</style>
