<template>
  <div>
    <!-- Include your Navbar component -->
    <NavBar />

    <!-- Include other components you want to render here -->
    <TilePage />
    <AboutUs />
    <CustomerPage />
    <BlogPage />
    <FaqPage />

    <!-- Include your Footer component -->
    <FooterPage />
  </div>
</template>

<script>

import TilePage from "@/components/TilePage.vue";
import AboutUs from "@/components/AboutUs.vue";
import CustomerPage from "@/components/CustomerPage.vue";
import BlogPage from "@/components/BlogPage.vue";
import FaqPage from "@/components/FaqPage.vue";
import FooterPage from "@/components/FooterPage.vue";
import NavBar from "@/components/NavBar";

export default {
  components: {
    NavBar,
    TilePage,
    AboutUs,
    CustomerPage,
    BlogPage,
    FaqPage,
    FooterPage,
  },
};
</script>
