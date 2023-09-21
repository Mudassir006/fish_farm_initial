<template>

  <section id="footer" class="container-fluid"
           style="background-color: #fffff7; margin-top: 40px; margin-bottom: 50px; ">
    <div class="row" style="display: flex;flex-direction: row;padding-left: 10%">
      <div class="column" style="float: left;
  width: 30%;
  padding: 10px;">
        <div>
          <img src="/image.png" style="margin-bottom: 20px; max-width: 100%;">

          <p style="text-align: center; color: grey;">
            Fish farm.pk established late 2016 in beautiful village of Ganga Pind near historical city Hasan
            Abdal -
            Attock
          </p>
          <small style="font-weight: bold">
            <strong>&copy;</strong> 2016-2022 <span style="color: #ff706b;">Fish farm.pk</span> All rights
            reserved
          </small>
        </div>

      </div>
      <div class="column" style="align-items: center;
  width: 50%;
  padding: 50px; position: relative;margin-left: 20%;

 ">
        <strong>
          <p style="font-weight: bold">Also Connect with us on: </p>
        </strong>

        <a href=""> <i class="fab fa-facebook-f fa-2x" style="color: #3b5998; padding: 10px "></i></a>


        <!-- Twitter -->
        <a href=""><i class="fab fa-twitter fa-2x" style="color: #55acee; margin-left: 10px;  padding: 10px"></i></a>

        <!-- Google -->
        <a href=""><i class="fab fa-google fa-2x" style="color: #dd4b39; margin-left: 10px;  padding: 10px"></i></a>

        <!-- Instagram -->
        <a href=""><i class="fab fa-instagram fa-2x" style="color: #ac2bac; margin-left: 10px; padding: 10px"></i></a>
      </div>


    </div>


  </section>


</template>

<script>
export default {
  name: "FooterPage"
}
</script>

<style>
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