<template>
  <link href="src/assets/styles.css" rel="stylesheet">
  <section style=" padding: 50px ; background-color: #ffffff">


    <div class="text-container">
      <h2 style="text-align: center;margin-top: 10px;padding: 30px">Popular Fishes</h2>
      <p style="text-align: center;color: grey; width: 100%; padding-left: 30px; margin-bottom: 50px;">
        These fishes are given positions on taste and which are available in the Pakistan Sea. These all are the
        best fish in
        Pakistan to eat. It’s also based on my experience and my personal point of view. But still, I will try
        to
        keep my pointview
        based on reality. Below I mention the different fishes of fish farm.pk, Pakistani healthy and organic.
      </p>
    </div>

    <div class="grid-container">
      <div class="row" style="margin-left: 3%">
        <div v-for="data in fishStore.products" id="t1" :key="data" class="col-md-4 mb-8" style="padding-bottom: 10px">
          <div class="product-tile">
            <div v-for="image in data.product_relation.product_images" :key="image"
                 :style="{backgroundImage:`url(${image.file_id})`}"
                 class="product-image"></div>
            <div class="product-title">{{ data.product_relation.name }}</div>
            <div class="product-description">{{ data.product_relation.description }}
            </div>
            <div class="product-rating">
              <span class="text-warning">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
            </div>
            <div class="d-flex justify-content-between">
              <div class="product-price" style="color:lightblue; font-weight: bold">RS. {{ data.unit_price }}/kg</div>
              <button class="btn btn-outline-danger" style="border-radius: 30px; margin-right: 10px"
                      @click="getData(data);axis()">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
        <br><br>

        <br><br>

      </div>

    </div>
    <p></p>
  </section>

</template>

<script>

import {singleStore, useFishStore} from "@/productstore";
import axiosInstance from "@/auth";
import axios from "axios";
import keycloak from "@/main";


export default {
  name: 'TilePage',
  setup() {
    const fishStore = useFishStore();
    const single = singleStore();

    return {
      fishStore,
      single,
    };
  },
  data() {
    return {
      quantity: 1,
    };
  },
  methods: {
    getData(fish) {
      this.$emit('item-added-to-cart', fish);
      this.single.setOne(fish)

    },
    axis() {
  const single = singleStore();
  const config = {
    cart_id: 1,
    business_product_id: single.product.business_product_id,
    processing_option_id: single.product.processing_options[0].processing_option_id,
    quantity: this.quantity,
    unit_price: single.product.unit_price
  };

  try {
    if (keycloak.authenticated){
    const response =  axiosInstance.post('cart_item', config);
    console.log(response.data);
    alert("Item Added to cart");}else {
      alert("please Login or signup first")
    }
  } catch (error) {
    console.error('Error:', error);
  }
}
  },

  created() {
    const fishStore = useFishStore();

    axios.get('http://127.0.0.1:8000/all_business_products',)
        .then(response => {
          fishStore.setProducts(response.data); // Update the store with fetched data
        })
        .catch(error => {
          console.error('An error occurred:', error);
        });
  },
};
</script>


<style>
.product-tile {
  border-top: 1px solid gainsboro;
  border-left: solid 1px gainsboro;
  border-right: solid 1px gainsboro;
  border-radius: 20px;
  box-shadow: 0 7px 9px rgba(0, 0, 0, 0.2);
  padding: 0; /* Adjusted padding */
  margin-top: 10px;
  height: 580px;
  width: 400px;
  display: block;


}

.product-image {
  background-size: cover;
  background-position: top; /* Positioned at the top */
  height: 50%; /* Adjusted to fill the upper 50% of the tile */
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.product-title {
  font-size: 18px;
  font-weight: bold;
  margin-top: 10px;
  padding: 10px;
}

.product-description {
  margin-top: -4px;
  padding: 10px;
}

.product-rating {
  margin-top: -4px;
  padding: 10px;
  font-size: 20px;
}

.product-price {
  margin-top: -4px;
  font-weight: bold;
  padding: 10px;
}

/* Adjust to move the button further to the right */


* {
  box-sizing: border-box;
}

@media (max-width: 1409px) {
  .col-md-4 {
    flex: 0 0 auto;
    width: 50%;
  }
}

@media (max-width: 950px) {
  .col-md-4 {
    flex: 0 0 auto;
    width: 100%;
    margin-left: 20%;

  }

  .grid-container {

    align-items: center;
  }


}

@media (max-width: 1265px) {

}

@media (min-width: 1500px) {
  .col-md-4 {
    flex: 0 0 auto;
    width: 33.333%;
  }
}

@media (max-width: 768px) {


  .text-container {
    margin-left: 10%;
    width: 100%;
  }


}


.row:after {
  content: "";
  display: table;
  clear: both;
}

@media (max-width: 984px) {
}


</style>

