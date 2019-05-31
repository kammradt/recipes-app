<template>
  <header>
    <div class="text-box">
      <h1 class="display-4">Receitinhas top 😋</h1>
      <p class="mt-3 font-weight-light headline">
        Recipes for the meals we love ❤️
      </p>
      <nuxt-link to="/recipes">
        <v-btn outline color="white">
          View recipes
          <v-icon right dark>trending_flat</v-icon>
        </v-btn>
      </nuxt-link>
    </div>
  </header>
</template>
<script>
export default {
  head() {
    return {
      title: 'Home page'
    }
  }
}
</script>
<style>
header {
  min-height: 100vh;
  background-image: linear-gradient(
      to right,
      rgba(0, 0, 0, 0.9),
      rgba(0, 0, 0, 0.4)
    ),
    url('/images/banner.jpg');
  background-position: center;
  background-size: cover;
  position: relative;
}
.text-box {
  position: absolute;
  top: 50%;
  left: 10%;
  transform: translateY(-50%);
  color: #fff;
}
a {
  text-decoration: none;
}
</style>
