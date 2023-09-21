<template>
  <div>
    <h1 class="summary-header">Summary</h1>
    <div class="summary-item" v-for="c in x.items" :key="c">
      <p v-for="v in c.business_product_relation.processing_options" :key="v">{{v.processing_option_id}}</p>

      <p>{{c.business_product_relation.business_product_id}}</p>
      <p>Name: {{ c.business_product_relation.product_relation.name }}</p>
      <p>Quantity: {{ c.quantity }}</p>
      <p>Unit Price: {{ c.unit_price }}</p>
      <p>Total Amount: {{ c.unit_price * c.quantity }}</p>
      <p>{{user.user.full_name}}</p>
      <p>{{user.user.email}}</p>
      <p>{{user.user.user_id}}</p>






  </div>
        <div  class="grand-total" >Grand Total: {{ calculateGrandTotal() }}</div>

        <div style="text-align: center;border:1px solid slategray" >
      <h5>Address Details</h5>
     <p>Address: {{add.address.address}}</p>
      <p>Phone:  {{add.address.phone}}</p>
      <p>City: {{add.address.city_relations.name}}</p>
      <p>Region: {{add.address.city_relations.region_relation.name}}</p>
    </div>


    <router-link to="/"><button class="btn btn-dark" @click="placeOrder(x.items)">Place Order</button>
    </router-link></div>
</template>

<script>
import {getAddress, getUser, selectedItem} from "@/productstore";
import axios from "axios";

export default {
  name: "SummaryPage",
  mounted() {
    axios.get('http://127.0.0.1:8000/user/id/'+1)
        .then(res => {
          this.user.setOne(res.data)

        }).catch(e => {
          alert(e)
    })
  },

  setup() {
    const x = selectedItem();
    const add = getAddress();
    const user = getUser()



    const calculateGrandTotal = () => {
      return x.items.reduce((total, item) => {
        return total + item.quantity * item.unit_price;
      }, 0);
    };


    const placeOrder = (cartItems) => {

      axios
        .post("http://127.0.0.1:8000/add_order", {

          order_numer: Math.floor(Math.random() * 8976568),
          delivery_charges: 200,
          total_amount: calculateGrandTotal(),
          discount: 100,
          order_total: calculateGrandTotal(),
          instructions: 'Just Leave At door',
          user_id: user.user.user_id,
          business_id: 2,
          delivery_address_id: add.address.address_id,
        })
        .then(function (response) {
          console.log(response);
          if (response.status === 200) {

            deleteCartItems(cartItems)
            addOrderItem(cartItems)
          }
        });
    };

    const deleteCartItems = (cartItems) => {

      cartItems.forEach((cartItem) => {
        axios
          .delete('http://127.0.0.1:8000/delete_citem/' + cartItem.cart_item_id)
          .then(function (response) {
            console.log(response);
            if (response.status === 200) {
              console.log("Item deleted");
            } else {
              console.error("Failed to delete item");
            }
          });
      });
    };

    const addOrderItem = (cartItems) => {
      cartItems.forEach((cartItem)=>{
        axios
    .post('http://127.0.0.1:8000/order_item', {
      quantity: cartItem.quantity,
  unit_price: cartItem.unit_price,
  business_product_id: cartItem.business_product_relation.business_product_id,
  processing_option_id: 2,
  order_id: 10
    })
    .then(function (response) {
      console.log(response);
      if (response.status === 200) {
        alert("Item added");
      } else {
        alert("Failed to add item");
      }
    })
    .catch(function (error) {
      console.error("An error occurred:", error);
    });
      })


};








    return {
      x,
      calculateGrandTotal,
      add,
      placeOrder,
      user,
    };
  },
};
</script>


<style scoped>
.summary-header {
  text-align: center;
  font-size: 24px;
  margin-bottom: 20px;
}

.summary-item {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}

.grand-total {
  text-align: right;
  font-size: 18px;
  margin-top: 20px;
}
</style>
