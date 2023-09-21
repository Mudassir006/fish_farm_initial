<template>


  <section id="blog" style="margin-top: 50px;background-color: #ffffff">
    <div class="grid-container">
      <div>
        <h1 class="display-5" style="text-align: center; font-weight: bold; margin-bottom: 20px">
          Latest Blogs
        </h1>
        <p style="text-align: center; color: grey; width: 100%; padding-left: 20px; margin-bottom: 50px">
          Find out the latest news from fishfarm.pk and our work with the fish farming. We also
          publish regular blogs on current topics and issues.
        </p>
      </div>
      <div class="row" style="padding-left: 7%">
        <div v-for="(item, index) in blogs" id="tile" :key="index" class="col-md-4" style="height: max-content">
          <div class="product-tile">
            <div :style="{backgroundImage:`url(${item.image_url})`}" class="product-image"></div>

            <div style="display: flex ; flex-direction: row; margin-top: 20px; margin-left: 20px">
              <img :src="item.author_relation.photo_url" alt="" style="width: 70px; border-radius: 50%">
              <p style="margin-left: 10px; width: 100px">{{ item.author_relation.name }}</p>
            </div>

            <div class="product-title">{{ item.title }}
            </div>
            <div class="product-description" style="margin-top: 2px;color: grey;">

              {{ item.blog.substring(0, 150) + "   ...." }}
            </div>
            <button class=" btn btn-outline-danger" style="margin-bottom: 10px; border: none; "> Learn More
            </button>
          </div>
        </div>

      </div>

      <button class="btn btn-danger"
              style="margin-top: 60px; margin-left: 40%; border-radius: 30px;width: 200px; margin-bottom: 20px;height: 60px;align-self: center">
        Load
        More
      </button>


    </div>
  </section>

</template>

<script>
import axios from "axios";

export default {
  name: "BlogPage",


  blogs: {},

  data() {
    return {

      blogs: null,
      images: null,



    }
  },
  created() {
    axios.get('http://127.0.0.1:8000/all_blogs')

        .then(response => {
          this.blogs = response.data; // Store the response data in the responseData property
          // this.images = response.data
        })
        .catch(error => {
          console.error('An error occurred:', error);
        });

  },


}


</script>

<style>
.product-tile {
  border-top: 1px solid gainsboro;
  border-left: solid 1px gainsboro;
  border-right: solid 1px gainsboro;
  border-radius: 20px;
  box-shadow: 0px 7px 9px rgba(0, 0, 0, 0.2);
  padding: 0px; /* Adjusted padding */
  margin-top: 10px;
  height: 580px;
  width: 400px;
  display: block;


}

.navbar-nav.custom-align {
  margin-left: 60%;
}

.twobuttons {
  display: flex;


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

.carousel-wrapper {
  position: relative;
}

.carousel-control {
  z-index: 1;
}

.review-tile {
  border-radius: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 10px;
  background-color: #f9f9f9;
  text-align: center;
}

.review-image {
  width: 80px;
  height: 80px;
  object-fit: cover;
  border-radius: 50%;
  margin-top: -30px;
}

.customer-name {
  font-size: 18px;
  font-weight: bold;
  margin-top: 10px;
}

.customer-description {
  margin-top: 5px;
}

.customer-rating {
  margin-top: 5px;
}

.review-tile {
  border: 1px solid #ddd;
  border-radius: 10px;
  background-color: #f9f9f9;
  padding: 20px;
  text-align: center;
  margin: 20px;
}

.carousel-control-prev,
.carousel-control-next {
  font-weight: bolder;
  font-size: 40px;
  color: black;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1;
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
  background-color: white;
  width: 25px;
  height: 25px;
}

.carousel-control-prev:before {
  content: '\2039'; /* Left arrow */
  margin-left: -95px; /* Adjust to move the button further to the left */
}

.carousel-control-next:before {


  border-radius: 50%;
  content: '\203A'; /* Right arrow */
  margin-right: -95px;
}

/* Adjust to move the button further to the right */


* {
  box-sizing: border-box;
}

.dropdown-toggle::after {
  display: inline-block;
  margin-left: 3.255em;
}

@media (max-width: 1409px) {
  .col-md-4 {
    flex: 0 0 auto;
    width: 50%;
  }
}

@media (max-width: 950px) {
  .col-md-3 {
    width: 50%;
  }

  .col-md-4 {
    flex: 0 0 auto;
    width: 100%;
    margin-left: 20%;

  }

  .grid-container {

    align-items: center;
  }

  .column {
    width: 50%;
  }


}

@media (max-width: 1265px) {
  .col-md-3 {
    width: 50%;
  }

  .base {
    padding-top: 70px;
  }

}

@media (min-width: 1500px) {
  .col-md-4 {
    flex: 0 0 auto;
    width: 33.333%;
  }
}

@media (max-width: 768px) {


  #footer {
    width: 100%;
  }


  .text-container {
    margin-left: 10%;
    width: 100%;
  }

  .col-md-3 {
    flex: 0 0 auto;
    width: 100%;
    height: 50%;

  }


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

