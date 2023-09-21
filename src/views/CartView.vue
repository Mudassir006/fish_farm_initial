<template>
  <div>
    <!-- Include your Navbar component -->
<!--    <NavBar />-->

    <!-- Include the CartPage component -->
    <CartPage />

    <!-- Include your Footer component -->
    <FooterPage />
  </div>
</template>

<script>
import CartPage from "@/components/CartPage.vue";
import FooterPage from "@/components/FooterPage.vue";

export default {
  components: {

    CartPage,
    FooterPage,
  },
};
</script>
