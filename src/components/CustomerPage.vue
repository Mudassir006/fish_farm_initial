<template>
  <section class="container-fluid" style="background-color: #edeff1 ; padding: 50px">

    <div style="margin-top: 40px">
      <h1 class="display-5" style="font-weight: bold;text-align: center; margin-top: 40px;padding: 20px">
        What Our Customers Are Saying
      </h1>

      <p>
        I discovered that their fish are quite fresh, and their pricing are cheap, making it very convenient to
        purchase from them. I would also recommend this site to others.

      </p>
    </div>

    <div class="container" style="margin-top: 100px">
      <div class="carousel-wrapper">
        <div id="reviewCarousel" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <div class="row">
                <div class="col-md-3 mb-4">
                  <div class="review-tile">
                    <img alt="Customer 1" class="review-image" src="/sole.jpg">
                    <div class="customer-name">
                    </div>
                    <small>MD Royal Hotel</small>
                    <div class="customer-description" style="color: grey">
                      Absolutely outstanding fish farm located
                      in Ganga pind near Hassan abdal. Easy to
                      post order, user friendly and good price.
                      We will definitely come back with friends
                      and I would highly recommend fishfarm.pk
                    </div>
                    <div class="customer-rating">
                      <span class="text-warning">&#9733;&#9733;&#9733;&#9733;&#9734;</span>
                    </div>
                  </div>
                </div>
                <br><br><br>
                <div class="col-md-3">
                  <div class="review-tile">
                    <img alt="Customer 2" class="review-image" src="/sole.jpg">
                    <div class="customer-name">Doplh Zilgar</div>
                    <small>MD Prince Hotel</small>
                    <div class="customer-description" style="color: grey">
                      Absolutely outstanding fish farm located
                      in Ganga pind near Hassan abdal. Easy to
                      post order, user friendly and good price.
                      We will definitely come back with friends
                      and I would highly recommend fishfarm.pk
                    </div>
                    <div class="customer-rating">
                      <span class="text-warning">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
                    </div>
                  </div>
                </div>
                <br><br><br>
                <div class="col-md-3">
                  <div class="review-tile">
                    <img alt="Customer 3" class="review-image" src="/sole.jpg">
                    <div class="customer-name">Zone Mayes</div>
                    <small>MD Era Hotel</small>
                    <div class="customer-description">
                      Absolutely outstanding fish farm located
                      in Ganga pind near Hassan abdal. Easy to
                      post order, user friendly and good price.
                      We will definitely come back with friends
                      and I would highly recommend fishfarm.pk
                    </div>
                    <div class="customer-rating">
                      <span class="text-warning">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
                    </div>
                  </div>
                </div>
                <div class="col-md-3">
                  <div class="review-tile">
                    <img alt="Customer 3" class="review-image" src="/sole.jpg">
                    <div class="customer-name">Zone Mayes</div>
                    <small>MD Era Hotel</small>
                    <div class="customer-description">
                      Absolutely outstanding fish farm located
                      in Ganga pind near Hassan abdal. Easy to
                      post order, user friendly and good price.
                      We will definitely come back with friends
                      and I would highly recommend fishfarm.pk
                    </div>
                    <div class="customer-rating">
                      <span class="text-warning">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <button class="carousel-control-prev" data-bs-slide="prev"
                  data-bs-target="#reviewCarousel"></button>
          <button class="carousel-control-next" data-bs-slide="next"
                  data-bs-target="#reviewCarousel"></button>
        </div>
      </div>
    </div>


  </section>

</template>

<script>
export default {
  name: "CustomerPage"
}
</script>

<style>
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
  color: gray;
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


</style>