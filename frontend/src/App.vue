<template>
  <div class="img-wrapper">
    <img src="/src/assets/logo.png" alt="logo" />
  </div>
  <Nav />
  <router-view />
</template>

<script>
import Nav from "./components/Nav.vue";

export default {
  name: "App",
  components: {
    Nav,
  },
};
</script>
<style scoped>
.img-wrapper {
  display: flex;
  justify-content: center;
  margin: 20px;
}
img {
  border-radius: 40%;
}
</style>