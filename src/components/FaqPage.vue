<template>
  <section class="FAQ" style="background-color: #fefdf8; padding: 50px">
    <div class="container ">

      <h1 class="display-5" style="text-align: center; margin-top: 40px;">
        Frequently Asked questions
      </h1>

      <div class="container mt-5">

        <div id="faqAccordion" class="accordion">
          <div class="card"
               style="border: 1px solid gray; background-color: white; border-radius: 20px ;   overflow: hidden">
            <div id="headingOne" class="card-header" style="background-color: white; border-bottom: none; ">
              <h2 class="mb-0" style="width: 100%">
                <button aria-controls="collapseOne" aria-expanded="true" aria-haspopup="true"
                        class="btn btn-link" data-target="#collapseOne" data-toggle="collapse"
                        style="color: black; font-weight: bold; text-decoration: none; width: 100%; text-align: left; display: flex; justify-content: space-between; align-items: center;"
                        type="button">

                  Does The Fisheries Department provide the fish seed to farmers?
                  <i class="fa-solid fa-caret-down"></i>
                </button>


              </h2>
            </div>

            <div id="collapseOne" aria-labelledby="headingOne" class="collapse" data-parent="#faqAccordion">
              <div class="card-body">
                Yes, The Department prepares feasibility report for fish farming at district level

                offices without any charging and and technical guidance is provided to the fish

                farmer free of cost
              </div>

            </div>
          </div>
          <div class="card"
               style="border: 1px solid gray; margin-top: 15px; background-color: white; border-radius: 20px; overflow: hidden">
            <div id="headingtwo" class="card-header" style="background-color: white; border-bottom: none">
              <h2 class="mb-0">
                <button aria-controls="collapseOne" aria-expanded="true" class="btn btn-link"
                        data-target="#collapsetwo" data-toggle="collapse"
                        style="color: black; font-weight: bold; text-decoration: none; width: 100%; text-align: left; display: flex; justify-content: space-between; align-items: center;"
                        type="button">
                  Does The Fisheries Department issue the permit for fishing?
                  <i class="fa-solid fa-caret-down"></i>
                </button>
              </h2>
            </div>

            <div id="collapsetwo" aria-labelledby="headingtwo" class="collapse" data-parent="#faqAccordion">
              <div class="card-body">
                Yes, The Department prepares feasibility report for fish farming at district level

                offices without any charging and and technical guidance is provided to the fish

                farmer free of cos
              </div>
            </div>
          </div>
          <div class="card"
               style="border: 1px solid gray; margin-top: 15px;background-color: white; border-radius: 20px;overflow: hidden">
            <div id="headingthree" class="card-header" style="background-color: white; border-bottom: none">
              <h2 class="mb-0">
                <button aria-controls="collapseOne" aria-expanded="true" class="btn btn-link"
                        data-target="#collapsethree" data-toggle="collapse"
                        style="color: black; font-weight: bold; text-decoration: none; width: 100%; text-align: left; display: flex; justify-content: space-between; align-items: center;"
                        type="button">
                  Does Fisheries Department give training to common people?
                  <i class="fa-solid fa-caret-down"></i>
                </button>
              </h2>
            </div>

            <div id="collapsethree" aria-labelledby="headingthree" class="collapse"
                 data-parent="#faqAccordion">
              <div class="card-body">
                Yes, The Department prepares feasibility report for fish farming at district level

                offices without any charging and and technical guidance is provided to the fish

                farmer free of cos
              </div>
            </div>
          </div>
          <div class="card"
               style="border: 1px solid gray; margin-top: 15px;margin-bottom:40px ;background-color: white; border-radius: 20px;overflow: hidden">
            <div id="headingfour" class="card-header" style="background-color: white; border-bottom: none">
              <h2 class="mb-0">
                <button aria-controls="collapseOne" aria-expanded="true" class="btn btn-link"
                        data-target="#collapsefour" data-toggle="collapse"
                        style="color: black; font-weight: bold; text-decoration: none; width: 100%; text-align: left; display: flex; justify-content: space-between; align-items: center;"
                        type="button">
                  Does the department prepare feasibility report fof fish farming?
                  <i class="fa-solid fa-caret-down"></i>
                </button>
              </h2>
            </div>

            <div id="collapsefour" aria-labelledby="headingfour" class="collapse"
                 data-parent="#faqAccordion">
              <div class="card-body">
                Yes, The Department prepares feasibility report for fish farming at district level

                offices without any charging and and technical guidance is provided to the fish

                farmer free of cos
              </div>
            </div>
          </div>


        </div>
      </div>


    </div>

  </section>

</template>

<script>
export default {
  name: "FaqPage"
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